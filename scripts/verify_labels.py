"""Check that the printed-page labels of data/records.json are unique and map one to one to the entry ids.

Run from anywhere: python3 scripts/verify_labels.py
Exits non-zero on any failure. It checks that
  1. the PDF page is exactly 3 more than childs_page on every record, and every id starts with its PDF page,
  2. all labels are distinct, also ignoring case and spaces,
  3. a label read back (page, block) gives the id again, so the mapping is one to one,
  4. MESSAGES.md and every messages/<id>.md carry the label of the id they are named for.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from labels import label  # noqa: E402

ROOT = os.path.join(HERE, '..')
records = json.load(open(os.path.join(ROOT, 'data', 'records.json'), encoding='utf-8'))
fail = []


def inverse(lab, pdf_offset=3):
    """Rebuild the id from a label alone: page + 3 is the PDF page; '(d)' is the first of bare digits; '?' is a leading '_'."""
    m = re.fullmatch(r'p\.(\d+) (.+)', lab)
    page, blk = int(m.group(1)), m.group(2)
    if blk.startswith('('):
        blk = blk[1] + blk[3:]
    elif blk.startswith('?'):
        blk = '_' + blk[1:]
    return 'p%03d%s' % (page + pdf_offset, blk)


ids = [r['id'] for r in records]
if len(ids) != len(set(ids)):
    fail.append('record ids are not unique')
labels = {}
for r in records:
    if r['pdf_page'] - r['childs_page'] != 3:
        fail.append('%s: PDF page minus printed page is %d, not 3' % (r['id'], r['pdf_page'] - r['childs_page']))
    lab = label(r)
    if lab in labels:
        fail.append('label %s is used by %s and %s' % (lab, labels[lab], r['id']))
    labels[lab] = r['id']
    if inverse(lab) != r['id']:
        fail.append('%s -> %s does not read back to the id' % (r['id'], lab))
folded = {}
for lab, rid in labels.items():
    k = re.sub(r'\s', '', lab).lower()
    if k in folded:
        fail.append('labels %s and %s differ only in case or spaces' % (lab, folded[k]))
    folded[k] = lab

table = open(os.path.join(ROOT, 'MESSAGES.md'), encoding='utf-8').read()
for r in records:
    lab = label(r)
    if '[%s](messages/%s.md)' % (lab, r['id']) not in table:
        fail.append('MESSAGES.md has no row linking %s to %s' % (lab, r['id']))
    page = open(os.path.join(ROOT, 'messages', r['id'] + '.md'), encoding='utf-8').read()
    if not page.startswith('# %s\n' % lab):
        fail.append('messages/%s.md does not start with the heading # %s' % (r['id'], lab))

print('%d records, %d distinct labels, %d ids read back from their labels' % (len(records), len(labels), len(set(inverse(l) for l in labels))))
if fail:
    print('\n'.join(fail[:40]))
    sys.exit('FAILED: %d problems' % len(fail))
print('OK: labels are unique and map one to one to the ids')
