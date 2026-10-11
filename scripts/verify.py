"""Decrypt, display and re-encrypt every reading in data/messages.json.

Run from anywhere: python3 scripts/verify.py
Standard library only. Exits non-zero if any check fails.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import adfgvx as A  # noqa: E402

DATA = json.load(open(os.path.join(HERE, '..', 'data', 'messages.json')))
failures = []


def check(name, ok):
    print('  [%s] %s' % ('ok' if ok else 'FAIL', name))
    if not ok:
        failures.append(name)


def matches(intercept, regenerated):
    """True if every symbol the log preserves comes back on re-encryption."""
    return len(intercept) == len(regenerated) and all(
        c == r for c, r in zip(intercept, regenerated) if c in A.COORD)


def show(text, width):
    for row in A.rows(text, width):
        print('    ' + row)


for m in DATA['messages']:
    key = m['key']
    ranks, square = key['transposition'], key['square']
    print('=' * 72)
    print(m['title'])
    print('key: %d columns %s' % (len(ranks), ' '.join(map(str, ranks))))
    print('square: %s' % square)

    if 'lost_block' in m:
        intercept = ''.join(m['parts'][0]['groups'])
        lb = m['lost_block']
        print('\n  As intercepted (%d symbols), decrypted as it stands:' % len(intercept))
        print('    ' + A.decrypt(intercept, square, ranks))
        gapped = intercept[:lb['position']] + '-' * lb['length'] + intercept[lb['position']:]
        print('\n  With %d lost symbols restored as blanks at position %d (%s marks a lost letter):'
              % (lb['length'], lb['position'], '-'))
        show(A.decrypt(gapped, square, ranks), len(ranks) // 2)
        full = intercept[:lb['position']] + lb['fill'] + intercept[lb['position']:]
        plain = A.decrypt(full, square, ranks)
        print('\n  Reading with the lost letters filled:')
        show(plain, len(ranks) // 2)
        regen = A.encrypt(plain, square, ranks)
        check('re-encrypts to the restored %d symbols' % len(full), regen == full)
        check('the %d intercepted symbols come back unchanged' % len(intercept),
              regen[:lb['position']] + regen[lb['position'] + lb['length']:] == intercept)
        continue

    corrections = m.get('corrections', [])
    fills = m.get('fills', [])
    opened = {(o['part'], o['letter']) for o in m.get('open_letters', [])}
    for p, part in enumerate(m['parts']):
        ct = ''.join(part['groups'])
        interim = A.untranspose(ct, ranks)
        pairs = [interim[k:k + 2] for k in range(0, len(interim), 2)]
        print('\n  %s (%d symbols), decrypted as it stands:' % (part['label'], len(ct)))
        show(A.unsubstitute(interim, square), len(ranks) // 2)

        # The reading: source corrections and reading fills applied, open letters left as '-'.
        letters = list(A.unsubstitute(interim, square))
        changed = {}
        for c in corrections:
            if c['part'] == p:
                assert pairs[c['letter']] == c['log_pair'], c
                letters[c['letter']] = A.unsubstitute(c['corrected_pair'], square)
                changed[c['letter']] = c['corrected_pair']
                print('    correction: letter %d, log %s -> %s (%s)'
                      % (c['letter'], c['log_pair'], c['corrected_pair'], c['why']))
        for f in fills:
            if f['part'] == p:
                letters[f['letter']] = f['letter_value']
        if any(f['part'] == p for f in fills):
            print('  Reading, with lost letters filled (%d) and open letters as -:'
                  % sum(f['part'] == p for f in fills))
            show(''.join(letters), len(ranks) // 2)

        # Re-encrypt every read letter and compare with each surviving symbol.
        exact = differ = unchecked = 0
        for j, ch in enumerate(letters):
            if (p, j) in opened or ch in '-?':
                unchecked += sum(s in A.COORD for s in pairs[j])
                continue
            back = A.substitute(ch, square)
            for s, b in zip(pairs[j], back):
                if s not in A.COORD:
                    continue
                if s == b:
                    exact += 1
                else:
                    differ += 1
        print('    surviving symbols: %d re-encrypt exactly, %d differ, %d unchecked (open letters)'
              % (exact, differ, unchecked))
        expected = sum(2 - sum(a == b for a, b in zip(c['log_pair'], c['corrected_pair']))
                       for c in corrections if c['part'] == p)
        check('%s: every read letter re-encrypts to its surviving symbols, except the %d listed '
              'correction(s)' % (part['label'], len(changed)), differ == expected)

print('=' * 72)
print('%d check(s) failed' % len(failures) if failures else 'all checks passed')
sys.exit(1 if failures else 0)
