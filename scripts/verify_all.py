"""Check every decode in data/records.json against its ciphertext and key.

Run from anywhere: python3 scripts/verify_all.py
Standard library only. For each record with a reading it
  1. decrypts the intercept under the stated key (records marked "as transcribed" must match the stored reading exactly),
  2. encrypts the stored reading again and counts how many surviving intercept symbols come back in place.
Records whose method says repair or fill changed the intercept (a lost symbol put back, a group inserted or removed),
so the second check is reported as a percentage rather than required to be exact.
Exits non-zero only if a record marked "as transcribed" fails, or an unchanged intercept does not round trip.
"""
import json
import os
import sys
import difflib

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import adfgvx as A  # noqa: E402

DATA = os.path.join(HERE, '..', 'data')
records = json.load(open(os.path.join(DATA, 'records.json')))
keys = {k['id']: k for k in json.load(open(os.path.join(DATA, 'keys.json')))}


def symbols(ct):
    return ''.join(c if c in A.COORD else '-' for c in ct.replace(' ', ''))


def reencrypt(plain, square, ranks):
    """Encrypt a reading that may contain '-' (an unknown letter); an unknown letter becomes two unknown symbols."""
    cell = {ch: A.COORD[i // 6] + A.COORD[i % 6] for i, ch in enumerate(square) if ch != '?'}
    interim = ''.join('-' if ch == '~' else cell.get(ch, '--') for ch in plain)
    return A.transpose(interim, ranks)


bad, n_exact, n_rt, n_rep = [], 0, 0, 0
align = []
for r in records:
    if not r.get('plaintext') or not r.get('key') or r['key'] not in keys:
        continue
    k = keys[r['key']]
    ct = symbols(r['ciphertext'])
    back = reencrypt(r['plaintext'].replace('#', '-') + ('~' if len(ct) % 2 else ''), k['square'], k['transposition'])
    if r['method'] == 'period key, as transcribed':
        n_exact += 1
        if A.decrypt(ct, k['square'], k['transposition']) != r['plaintext']:
            bad.append(r['id'] + ' decrypt')
    if r['method'] in ('period key, as transcribed',) or r['method'].startswith('known-key fill'):
        n_rt += 1
        if len(back) != len(ct) or any(a != b for a, b in zip(ct, back) if a in A.COORD and b in A.COORD):
            bad.append(r['id'] + ' round trip')
    else:
        if r['method'] == 'period key, length repaired' or r['method'].startswith('known-key repair'):
            n_rep += 1
            sm = difflib.SequenceMatcher(None, ct, back, autojunk=False)
            same = sum(m.size for m in sm.get_matching_blocks())
            known = sum(c in A.COORD for c in ct)
            align.append((r['id'], r['method'], 100.0 * same / max(1, known), known))
print('decrypt exactly to the stored reading: %d records (as transcribed)' % n_exact)
print('every surviving symbol re-encrypts in place: %d records (as transcribed or fill)' % n_rt)
print('repaired records, share of surviving symbols that align after re-encryption: %d records' % n_rep)
for i, m, p, n in align:
    print('  %-8s %-30s %5.1f%% of %d' % (i, m, p, n))
if bad:
    print('FAILED:', bad)
    sys.exit(1)
print('ok')
