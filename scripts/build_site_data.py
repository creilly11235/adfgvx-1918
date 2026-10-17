"""Write docs/story-data.js, the data behind the GitHub Pages article, from the data files.

The article never carries a result of its own. Every count, status, key and reading on the page
comes from data/records.json, data/keys.json, data/messages.json and data/schmeh_list.json, so
when a result changes, edit the data file, run this script and the page follows.

Run from the repository root:  python3 scripts/build_site_data.py
"""
import json, sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))
import adfgvx  # noqa: E402

records = json.loads((ROOT / 'data/records.json').read_text(encoding='utf-8'))
keys = json.loads((ROOT / 'data/keys.json').read_text(encoding='utf-8'))
messages = json.loads((ROOT / 'data/messages.json').read_text(encoding='utf-8'))
schmeh = json.loads((ROOT / 'data/schmeh_list.json').read_text(encoding='utf-8'))

OURS = 'This project, 2026'


def status_group(status):
    """The public status vocabulary folded into the groups the page colours."""
    if status == 'Solved':
        return 'solved'
    if status.startswith('Solved'):
        return 'open'
    if status == 'Partially solved':
        return 'partial'
    if status in ('No cipher text', 'Duplicate entry'):
        return 'none'
    return 'unsolved'


def count_groups(rows):
    counts = {}
    for row in rows:
        group = status_group(row['status'])
        counts[group] = counts.get(group, 0) + 1
    return counts


# One compact row per log entry, in log order, for the grid of the whole log.
by_id = {row['id']: row for row in records}
schmeh_of = {}
for entry in schmeh['entries']:
    for rid in entry['ids']:
        schmeh_of[rid] = entry['schmeh']
        if rid not in by_id:
            sys.exit(f'schmeh_list.json names {rid}, which is not in records.json')

grid = []
for row in records:
    grid.append({
        'id': row['id'],
        'page': row['childs_page'],
        'date': row['date'].replace(' 1918', ''),
        'status': row['status'],
        'group': status_group(row['status']),
        'key': row['key'] or '',
        'schmeh': schmeh_of.get(row['id'], ''),
        'ours': row['published_by'] == OURS,
        'oursKey': row['published_by'] == OURS and row['key_by'].startswith('Lasry, Niebel'),
    })

counts = count_groups(records)
counts['total'] = len(records)
counts['ours'] = sum(1 for row in records if row['published_by'] == OURS)
counts['oursNewKey'] = sum(1 for row in records if row['key_by'] == OURS)
counts['oursKey'] = sum(1 for row in records if row['published_by'] == OURS and row['key_by'].startswith('Lasry, Niebel'))
counts['noPublished'] = sum(1 for row in records if status_group(row['status']) in ('solved', 'open') and not row['published_by'])
counts['lasryKey'] = sum(1 for row in records if row['key_by'].startswith('Lasry, Niebel'))
counts['schmehEntries'] = len(schmeh['entries'])
counts['schmehRecords'] = len(schmeh_of)
counts['schmehOurs'] = sum(1 for rid in schmeh_of if by_id[rid]['published_by'] == OURS)
counts['schmehSolvedByOthers'] = sum(1 for rid in schmeh_of if status_group(by_id[rid]['status']) in ('solved', 'open') and by_id[rid]['published_by'] != OURS)
counts['schmehUnsolved'] = sum(1 for rid in schmeh_of if status_group(by_id[rid]['status']) == 'unsolved')
counts['readable'] = counts.get('solved', 0) + counts.get('open', 0)
counts['months'] = {}
for row in records:
    month = row['date'].split(' ', 1)[1] if ' ' in row['date'] else row['date']
    counts['months'][month] = counts['months'].get(month, 0) + 1

# Schmeh's list, one row per entry, with the status of each matched log entry.
schmeh_rows = []
for entry in schmeh['entries']:
    rows = [by_id[rid] for rid in entry['ids']]
    schmeh_rows.append({
        'schmeh': entry['schmeh'],
        'ids': entry['ids'],
        'page': rows[0]['childs_page'],
        'date': rows[0]['date'].replace(' 1918', ''),
        'status': ' and '.join(dict.fromkeys(r['status'] for r in rows)),
        'group': 'ours' if any(r['published_by'] == OURS for r in rows) else status_group(rows[0]['status']),
        'keyBy': ' and '.join(dict.fromkeys(r['key_by'] for r in rows if r['key_by'])),
        'publishedBy': ' and '.join(dict.fromkeys(r['published_by'] for r in rows if r['published_by'])),
    })

# The period keys, for the chapter on how the cipher works.
periods = [{'id': k['id'], 'period': k['period'], 'width': k['width'], 'source': k['source']} for k in keys]

# The two featured solutions, worked out from messages.json with the cipher itself so that the
# animation and the repository can never disagree.
def ciphertext(part):
    return ''.join(part['groups'])


def message_2305(msg):
    part = msg['parts'][0]
    ct = ciphertext(part)
    key = msg['key']
    gap = msg['lost_block']
    width = len(key['transposition'])
    restored = ct[:gap['position']] + '-' * gap['length'] + ct[gap['position']:]
    interim_blank = adfgvx.untranspose(restored, key['transposition'])
    plain_blank = adfgvx.unsubstitute(interim_blank, key['square'])
    filled = ct[:gap['position']] + gap['fill'] + ct[gap['position']:]
    plain = adfgvx.decrypt(filled, key['square'], key['transposition'])
    assert adfgvx.encrypt(plain, key['square'], key['transposition']) == filled
    # Each lost letter kept one of its two symbols, so it has six candidates.
    candidates = []
    for i, ch in enumerate(plain_blank):
        if ch != '-':
            continue
        a, b = interim_blank[2 * i], interim_blank[2 * i + 1]
        if a in adfgvx.COORD:
            cells = [key['square'][adfgvx.COORD.index(a) * 6 + j] for j in range(6)]
            kind = 'row ' + a
        else:
            cells = [key['square'][j * 6 + adfgvx.COORD.index(b)] for j in range(6)]
            kind = 'column ' + b
        candidates.append({'letter': i, 'kind': kind, 'cells': cells, 'chosen': plain[i]})
    return {
        'name': msg['name'], 'title': msg['title'],
        'header': part['log_header'], 'partLabel': part['part_label'],
        'symbolsInHeader': part['symbols_in_header'], 'symbolsInLog': part['symbols_in_log'],
        'groups': part['groups'], 'groupsPerLine': 8,
        'key': key['transposition'], 'width': width, 'square': key['square'],
        'keySource': key['source'],
        'gap': {'position': gap['position'], 'length': gap['length'], 'fill': gap['fill'], 'groupIndex': gap['position'] // 5, 'groupCount': gap['length'] // 5},
        'plainBlank': plain_blank, 'plain': plain, 'rowWidth': 8,
        'candidates': candidates,
        'lostLetters': plain_blank.count('-'),
        'placements': 194756,
        'reading': 'AN X O X H X L XX 11 X ARMEE X ALPENKORPS RAUM X PETERREVE X VERBASZ XX 217 X 216 X 9 X R X D X LINIE X NAGYBESKIEREK X VERSECZ X VERSECZ X VON SERBEN BESETZT X',
        'german': 'An O.H.L. 11. Armee. Alpenkorps Raum Péterréve und Verbász. 217., 216., 9. R.D. Linie Nagybecskerek bis Versecz. Versecz von Serben besetzt.',
        'english': 'To the Supreme Army Command. 11th Army. Alpine Corps in the area of Péterréve and Verbász. 217th, 216th and 9th Reserve Divisions on the line from Nagybecskerek to Versecz. Versecz occupied by the Serbs.',
        'checks': {
            'realScore': -2.11, 'shuffledScores': [-3.45, -4.05], 'plantedRight': 54, 'plantedTotal': 60, 'plantedMedian': -2.09,
            'nextPlacementGap': 5.9, 'nextPlacementOdds': 370,
        },
    }


def message_p153(msg):
    key = msg['key']
    width = len(key['transposition'])
    parts = []
    for index, part in enumerate(msg['parts']):
        ct = ciphertext(part)
        interim = adfgvx.untranspose(ct, key['transposition'])
        # Columns of the transposition block, each of one kind: row labels or column labels.
        n = width
        columns = [ct[i::n] for i in range(n)]  # placeholder, replaced below by block columns
        block_rows = adfgvx.rows(interim, 2 * width)
        plain_as_is = adfgvx.unsubstitute(interim, key['square'])
        parts.append({
            'label': part['label'], 'symbolsInLog': part['symbols_in_log'], 'groups': part['groups'],
            'interimRows': block_rows, 'plainAsIs': plain_as_is,
        })
    # The reading, with the fills and corrections applied.
    part6 = parts[1]
    plain6 = list(part6['plainAsIs'])
    fills = {f['letter']: f['letter_value'] for f in msg['fills']}
    corrections = {c['letter']: c for c in msg['corrections']}
    open_letters = [o['letter'] for o in msg['open_letters']]
    for letter, value in fills.items():
        plain6[letter] = value.lower()
    for letter, c in corrections.items():
        # The corrected pair decrypts to the letter the word needs.
        a, b = c['corrected_pair']
        plain6[letter] = key['square'][adfgvx.COORD.index(a) * 6 + adfgvx.COORD.index(b)].lower()
    for letter in open_letters:
        plain6[letter] = '_'
    part6['plain'] = ''.join(plain6)
    parts[0]['plain'] = parts[0]['plainAsIs']
    return {
        'name': msg['name'], 'title': msg['title'],
        'header': msg['parts'][0]['log_header'],
        'key': key['transposition'], 'width': width, 'square': key['square'], 'keySource': key['source'],
        'knownCells': sum(1 for ch in key['square'] if ch != '?'),
        'parts': parts, 'rowWidth': width // 2,
        'fills': msg['fills'], 'corrections': msg['corrections'], 'openLetters': open_letters,
        'letters': sum(len(p['plainAsIs']) for p in parts),
        'lostSymbols': sum(''.join(p['groups']).count('-') for p in parts),
        'reading': 'ANORDNUNGEN VOM 2TEN 11TEN NR 858 BEZIEHEN LASSEN SOWEIT NOCH NICHT GESCHEHEN MUNITIONSBESTAND DER NACHHUT ARTILLERIE MELDEN X 8 X G X R _ _ _ B X A',
        'german': 'Anordnungen vom 2. 11., Nr. 858, beziehen lassen, soweit noch nicht geschehen. Munitionsbestand der Nachhutartillerie melden. 8 G R . . . B A',
        'english': 'Have the orders of 2 November, No. 858, drawn, as far as this has not yet been done. Report the ammunition stock of the rear guard artillery. [8 G R ... B A]',
        'checks': {
            'winner': -266.7, 'next': -283.4, 'shuffledBest': -301.1, 'plantedBar': -268.0,
            'plantedRecovered': 10, 'plantedTotal': 24,
            'blindAgreement': {'cells': 17, 'compared': 25},
            'page187': {'ours': -283.4, 'next': -429.0, 'cells': 22},
            'otherUnread': 40, 'publishedSquares': 19, 'widths': [15, 25],
        },
    }


featured = {}
for msg in messages['messages']:
    if msg['name'] == '2305':
        featured['m2305'] = message_2305(msg)
    elif msg['name'] == 'p153':
        featured['p153'] = message_p153(msg)

# The worked example from the README, computed rather than typed.
example_square = next(k for k in keys if k['id'] == 'nov10')['square']
example_square = ''.join(ch if ch != '?' else fill for ch, fill in zip(example_square, '4ARUT1OIFSKN35BZPVLD6JMXCWHQ2E7G08Y9'))
example_key = [3, 1, 4, 2]
example_word = 'ANGRIFF'
example_interim = adfgvx.substitute(example_word, example_square)
example_ct = adfgvx.transpose(example_interim, example_key)
example = {
    'word': example_word, 'square': example_square, 'key': example_key,
    'interim': example_interim, 'rows': adfgvx.rows(example_interim, len(example_key)),
    'columns': [example_interim[i::len(example_key)] for i in range(len(example_key))],
    'cipher': example_ct, 'groups': [example_ct[i:i + 5] for i in range(0, len(example_ct), 5)],
}

data = {
    'generated': date.today().isoformat(),
    'counts': counts,
    'grid': grid,
    'schmeh': schmeh_rows,
    'periods': periods,
    'example': example,
    'featured': featured,
    'ours': [row['id'] for row in records if row['published_by'] == OURS],
}

out = ROOT / 'docs/story-data.js'
out.write_text('/* Generated by scripts/build_site_data.py from the data files. Do not edit by hand. */\n'
               'window.STORY_DATA = ' + json.dumps(data, ensure_ascii=False, separators=(',', ':')) + ';\n', encoding='utf-8')
print(f'wrote {out.relative_to(ROOT)}: {len(grid)} entries, {counts["readable"]} readable, {counts["ours"]} published here')
