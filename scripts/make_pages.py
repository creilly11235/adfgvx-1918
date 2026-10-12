"""Write one page per message of Childs's log from the data files of the write-up.
usage: public_pages.py PUBLIC_DIR      (PUBLIC_DIR holds data/records.json, keys.json, messages.json)
Reads data/records.json, data/keys.json, data/messages.json and, if present, data/translations.json.
Writes PUBLIC_DIR/messages/<id>.md, each following the message in six steps:
  1 printed (source item, page, log heading)   2 transcribed as printed, a dash for each symbol missing
  3 repaired or edited transcription, each edit marked   4 decrypted as it stands
  5 decrypted after repair, low confidence letters marked   6 English translation, low confidence words marked
Marking convention (also in the README of the public repository):
  ciphertext   - a symbol missing in the print; in step 3 a lowercase symbol was changed, inserted or filled by the repair, and a removed printed symbol is listed under the line
  plaintext    UPPERCASE both symbols of the letter are in the print and unedited; lowercase one or both symbols were repaired or filled, so the letter rests on the repair
               _ a letter not determined; # a digit not determined; X stands for a space or a stop, as the senders used it
  English      a phrase in [square brackets with a question mark] rests on at least one lowercase, _ or # letter
The plaintext of each row comes from records.json, and the ones of the page 153 pair and message 2305 are rebuilt from messages.json."""
import difflib, json, os, sys, textwrap

class A:
    """The few cipher functions needed, copied so that this file also runs alone in the public repository."""
    COORD = 'ADFGVX'
    @staticmethod
    def fractionate(plain, square):
        pos = {ch: A.COORD[i // 6] + A.COORD[i % 6] for i, ch in enumerate(square) if ch != '?'}
        return ''.join(pos[ch] for ch in plain)
    @staticmethod
    def transpose(interim, ranks):
        n = len(ranks); cols = [interim[i::n] for i in range(n)]
        return ''.join(cols[i] for i in sorted(range(n), key=lambda i: ranks[i]))
    @staticmethod
    def untranspose(ct, ranks):
        n, L = len(ranks), len(ct); full, extra = divmod(L, n)
        heights = [full + (1 if i < extra else 0) for i in range(n)]
        cols, p = [None] * n, 0
        for i in sorted(range(n), key=lambda i: ranks[i]):
            cols[i] = ct[p:p + heights[i]]; p += heights[i]
        return ''.join(cols[i][r] for r in range(full + 1) for i in range(n) if r < heights[i])
    @staticmethod
    def defractionate(interim, square):
        out = []
        for k in range(0, len(interim) - 1, 2):
            a, b = interim[k], interim[k + 1]
            out.append(square[A.COORD.index(a) * 6 + A.COORD.index(b)] if a in A.COORD and b in A.COORD else '-')
        if len(interim) % 2: out.append('~')
        return ''.join(out)
    @staticmethod
    def decrypt(ct, square, ranks):
        return A.defractionate(A.untranspose(ct, ranks), square)
    @staticmethod
    def position_map(L, ranks):
        """ciphertext index -> interim index, for a ciphertext of length L."""
        n = len(ranks); full, extra = divmod(L, n)
        heights = [full + (1 if i < extra else 0) for i in range(n)]
        m, p = [0] * L, 0
        for i in sorted(range(n), key=lambda i: ranks[i]):
            for r in range(heights[i]): m[p] = r * n + i; p += 1
        return m

def unsub(interim, square):
    return A.defractionate(interim, square)

def sub(plain, square):
    return A.fractionate(plain, square)

SOURCE = ('J. Rives Childs, *General Solution of the ADFGVX Cipher System*, Aegean Park Press, Cryptographic Series 88 (ISBN 0894122843), '
          'Appendix B, the intercept logs of 1918. The scanned book is the free full text PDF of 248 pages offered by the Aegean Park Press index kept by Richard Bean')
VIEWER = 'https://drive.google.com/file/d/1_JiNMck7eUvdrOTrH7fsj1Yh44t-VSC6/view?usp=sharing'
INDEX = 'https://richardbean.id.au/misc/kryptos/aegean-park-press.html'
OURS_SOURCE = {'p156C3': ('p153', 0), 'p156C6': ('p153', 1), 'p179B1': ('2305', 0)}

def groups(s, n=5):
    return ' '.join(s[i:i + n] for i in range(0, len(s), n))

def rows(s, w):
    return textwrap.wrap(s, w, break_long_words=True, break_on_hyphens=False) or ['']

def reencrypt(plain, square, ranks):
    """Encrypt a reading that may hold '_' or '#' (a letter not determined): such a letter becomes two missing symbols."""
    cell = {ch: A.COORD[i // 6] + A.COORD[i % 6] for i, ch in enumerate(square) if ch != '?'}
    return A.transpose(''.join(cell.get(ch, '--') for ch in plain), ranks)

def runs(items):
    """items: sorted (kind, position, text); join neighbours of the same kind into ranges."""
    out, cur = [], None
    for kind, pos, ch in items:
        if cur and cur[0] == kind and pos == cur[2] + 1:
            cur[2] = pos; cur[3] += ch
        else:
            cur = [kind, pos, pos, ch]; out.append(cur)
    return out

def describe(r):
    kind, p1, p2, txt = r; n = p2 - p1 + 1
    span = 'symbol %d' % p1 if n == 1 else 'symbols %d to %d' % (p1, p2)
    if kind == 'ins': return '%s inserted by the repair (%d symbol%s)' % (span, n, '' if n == 1 else 's')
    if kind == 'del': return 'printed %s removed (%d symbol%s)' % (span, n, '' if n == 1 else 's')
    return '%s changed or filled by the repair (%d symbol%s)' % (span, n, '' if n == 1 else 's')

def align(printed, rep):
    """Mark the repaired line against the print. Returns (marked line, solid flags per repaired position, edit descriptions)."""
    marked, solid, items = list(rep), [False] * len(rep), []
    if len(printed) == len(rep):
        for j, (a, b) in enumerate(zip(printed, rep)):
            if a == b: solid[j] = b != '-'
            else:
                if b != '-': marked[j] = b.lower()
                items.append(('chg', j + 1, b))
    else:
        sm = difflib.SequenceMatcher(None, printed, rep, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal':
                for j in range(j1, j2): solid[j] = rep[j] != '-'
                continue
            for j in range(j1, j2):
                if rep[j] != '-': marked[j] = rep[j].lower()
            n = min(i2 - i1, j2 - j1)
            for t in range(n): items.append(('chg', j1 + t + 1, rep[j1 + t]))
            for t in range(n, j2 - j1): items.append(('ins', j1 + t + 1, rep[j1 + t]))
            for t in range(n, i2 - i1): items.append(('del', i1 + t + 1, printed[i1 + t]))
    edits = [describe(r) for r in runs(sorted(items, key=lambda x: (x[0], x[1])))]
    return ''.join(marked), solid, edits

def mark_plain(plain, rep_len, solid, ranks):
    """UPPERCASE where both symbols of the letter are solid, lowercase otherwise, _ and # kept."""
    pos = A.position_map(rep_len, ranks)          # ciphertext index -> interim index
    where = {v: k for k, v in enumerate(pos)}     # interim index -> ciphertext index
    out = []
    for k, ch in enumerate(plain):
        if ch in '-_': out.append('_'); continue
        if ch == '#': out.append('#'); continue
        ok = all(where.get(2 * k + t) is not None and solid[where[2 * k + t]] for t in (0, 1))
        out.append(ch.upper() if ok else ch.lower())
    return ''.join(out)

def ours_parts(msg, part):
    """Printed symbols, repaired symbols and plaintext (open letters as _) of a published reading (page 153 pair or message 2305)."""
    key = msg['key']; ranks, square = key['transposition'], key['square']
    printed = ''.join(msg['parts'][part]['groups'])
    if 'lost_block' in msg:
        lb = msg['lost_block']; rep = printed[:lb['position']] + lb['fill'] + printed[lb['position']:]
        plain = A.decrypt(rep, square, ranks)
        return printed, rep, ''.join('_' if c in '-?~' else c for c in plain), msg
    interim = A.untranspose(printed, ranks)
    pairs = [interim[k:k + 2] for k in range(0, len(interim) - 1, 2)]
    letters = list(unsub(interim, square))
    for c in msg.get('corrections', []):
        if c['part'] == part: pairs[c['letter']] = c['corrected_pair']; letters[c['letter']] = unsub(c['corrected_pair'], square)
    for f in msg.get('fills', []):
        if f['part'] == part: letters[f['letter']] = f['letter_value']; pairs[f['letter']] = sub(f['letter_value'], square)
    for o in msg.get('open_letters', []):
        if o['part'] == part: letters[o['letter']] = '_'
    rep = A.transpose(''.join(pairs), ranks)
    return printed, rep, ''.join('_' if c in '-?~' else c for c in letters), msg

def english(segs, marked_plain):
    """Join the translated phrases; a phrase whose letters include a lowercase, _ or # letter is bracketed with a question mark."""
    out, k = [], 0
    for de, en in segs:
        part = marked_plain[k:k + len(de)]; k += len(de)
        if not en.strip(): continue
        out.append('[%s?]' % en.strip() if any(c in '_#' or c.islower() for c in part if c.isalpha() or c in '_#') else en.strip())
    return ' '.join(out)

def german(segs, marked_plain):
    out, k = [], 0
    for de, en in segs:
        out.append(marked_plain[k:k + len(de)]); k += len(de)
    return ' '.join(out)

def check_segments(rid, segs, plain):
    joined = ''.join(d for d, _ in segs)
    if joined.upper() != plain.upper().replace('-', '_'):
        raise SystemExit('translation of %s does not cover the plaintext exactly' % rid)

def page(e, keys, msgs, trans, want_plain=False):
    rid = e['id']; L = ['# %s' % rid, '']
    meta = 'Childs page %s, %s' % (e['childs_page'], e['date'])
    L += [(meta + '. ' + ('Key %s' % e['key'] if e['key'] else 'No key found') + '. ' + e['method'][0].upper() + e['method'][1:] + '. Confidence %s.' % e['confidence'] + (' ' + e['credit'] + '.' if e['credit'] else '')).replace('-', ' '), '']
    # step 1
    L += ['## 1 Printed', '',
          '%s. The message is on printed page %s, which is page %s of the PDF. Open the [PDF](%s) and go to PDF page %s. The index is [here](%s). Page images are not republished here.' % (SOURCE, e['childs_page'], e['pdf_page'], VIEWER, e['pdf_page'], INDEX), '',
          'Heading in the log, %s%s. The heading counts %s symbols and the log shows %s.' % ('`%s`' % e['header'] if e['header'] else 'none', (', part %s' % e['part']) if e['part'] not in (None, 'None') else '', e['count_in_log'] if e['count_in_log'] is not None else 'no count', e['symbols_in_log']), '']
    printed = e['printed']
    L += ['## 2 Transcribed as printed', '', 'A dash is a symbol missing in the print.', '', '```'] + rows(groups(printed), 59) + ['```', '']
    # repaired line, plaintext
    key = keys.get(e['key']) if e['key'] else None
    plain = e['plaintext']; rep = None
    if e['id'] in OURS_SOURCE:
        name, part = OURS_SOURCE[e['id']]
        printed2, rep, plain, m = ours_parts(msgs[name], part); key = m['key']
        assert printed2 == printed, rid
    elif plain and e['method'].startswith(('period key', 'known-key repair')):
        rep = reencrypt(plain, key['square'], key['transposition'])
    elif e['ciphertext'].replace(' ', '') != printed or plain:
        rep = e['ciphertext'].replace(' ', '')
    if rep is None or rep == printed:
        L += ['## 3 Repaired or edited transcription', '', 'No edit. The transcription is used as it stands.', '']
        rep, solid, edits, marked = printed, [c != '-' for c in printed], [], printed
    else:
        marked, solid, edits = align(printed, rep)
        L += ['## 3 Repaired or edited transcription', '', 'A lowercase symbol was changed, inserted or filled by the repair.', '', '```'] + rows(groups(marked), 59) + ['```', '']
        if edits: L += ['Edits.', ''] + ['* ' + x for x in edits] + ['']
    # step 4
    if (key is None or e['method'] == 'not read') and want_plain: return None
    if key is None or e['method'] == 'not read':
        L += ['## 4 Decrypted as it stands', '', 'No key reads this message, so there is nothing to show here.', '', '## 5 Decrypted after repair', '', 'Not read.', '', '## 6 English translation', '', 'Not read, so there is no translation.', '']
        return '\n'.join(L)
    sq, rk = key['square'], key['transposition']
    asis = ''.join('_' if c in '-?~' else c for c in A.decrypt(printed, sq, rk))
    L += ['## 4 Decrypted as it stands', '', 'Key %s, %d columns. The printed transcription is decrypted with no repair. A letter that lost a symbol is `_`.' % (e['key'] or 'of this message', len(rk)), '', '```'] + rows(asis, 60) + ['```', '']
    if plain is None and want_plain: return None
    if plain is None:
        L += ['## 5 Decrypted after repair', '', 'Not read.', '', '## 6 English translation', '', 'Not read, so there is no translation.', '']
        return '\n'.join(L)
    mp = mark_plain(plain, len(rep), solid, rk)
    if want_plain: return mp
    L += ['## 5 Decrypted after repair', '', 'Uppercase letters rest on symbols that are in the print. Lowercase letters rest on the repair. `_` is a letter not determined and `#` a digit not determined. X stands for a space or a stop.', '', '```'] + rows(mp, 60) + ['```', '']
    L += ['## 6 English translation', '']
    t = trans.get(rid)
    if t:
        check_segments(rid, t['segments'], mp)
        L += ['German in phrases.', '', '```'] + rows(german(t['segments'], mp), 60) + ['```', '', english(t['segments'], mp), '', t.get('note', '')] if t.get('note') else ['German in phrases.', '', '```'] + rows(german(t['segments'], mp), 60) + ['```', '', english(t['segments'], mp), '']
    else:
        L += ['No translation yet.', '']
    return '\n'.join(L)

def marked_plain_of(e, keys, msgs):
    return page(e, keys, msgs, {}, True)

def batches(pub, outdir, n):
    """Write n work files of {id: marked plaintext} for the translators."""
    D = os.path.join(pub, 'data')
    recs = json.load(open(os.path.join(D, 'records.json')))
    keys = {k['id']: k for k in json.load(open(os.path.join(D, 'keys.json')))}
    msgs = {m['name']: m for m in json.load(open(os.path.join(D, 'messages.json')))['messages']}
    items = {}
    for e in recs:
        txt = marked_plain_of(e, keys, msgs)
        if txt: items[e['id']] = txt
    os.makedirs(outdir, exist_ok=True)
    ids = sorted(items)
    for b in range(n):
        json.dump({i: items[i] for i in ids[b::n]}, open(os.path.join(outdir, 'batch_%02d.json' % b), 'w'), indent=0)
    print(len(items), 'messages in', n, 'batches')

def main(pub):
    D = os.path.join(pub, 'data')
    recs = json.load(open(os.path.join(D, 'records.json')))
    keys = {k['id']: k for k in json.load(open(os.path.join(D, 'keys.json')))}
    msgs = {m['name']: m for m in json.load(open(os.path.join(D, 'messages.json')))['messages']}
    tp = os.path.join(D, 'translations.json')
    trans = json.load(open(tp))['records'] if os.path.exists(tp) else {}
    out = os.path.join(pub, 'messages'); os.makedirs(out, exist_ok=True)
    seen = set()
    for e in recs:
        low = e['id'].lower()
        if low in seen: raise SystemExit('file names collide ignoring case: %s' % e['id'])
        seen.add(low)
        open(os.path.join(out, e['id'] + '.md'), 'w').write(page(e, keys, msgs, trans) + '\n')
    print(len(recs), 'pages,', len(trans), 'translated')

if __name__ == '__main__':
    if sys.argv[1] == '--batches': batches(sys.argv[2], sys.argv[3], int(sys.argv[4]))
    else: main(sys.argv[1])
