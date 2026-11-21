"""The printed-page label of a log entry, shared by make_pages.py and build_site_data.py.

An entry id is `p` + the PDF page of the scanned book (three digits) + a block suffix, for example `p156C3`.
The PDF page is 3 more than the page printed in Childs's book, so `p156C3` is on printed page 153, the page
that Schmeh's list, outside researchers and the book itself use. The label puts the printed page first:

    label = 'p.' + childs_page + ' ' + block

`childs_page` comes from data/records.json. `block` is the id with its `p` and three PDF-page digits removed
(`p156C3` -> `C3`, `p059B.2` -> `B.2`, `p108BB` -> `BB`), with two shapes handled so the label does not mislead:
  * a leading `_` is the id's placeholder where no block letter was recorded in the id, and is written `?`
    (`p188_` -> `p.185 ?`, `p216_3` -> `p.213 ?3`, `p220A.3` is unchanged). It does not say the log shows no
    mark: most of these headings do show one, which step 1 of the entry's page gives. A bare underscore would
    also read as Markdown italics;
  * a suffix of digits only (`p0924`, `p09244`) is a block whose letter the log's heading reads as a digit; that
    first digit is put in brackets, so it is not read as a number (`p0924` -> `p.89 (4)`, `p09244` -> `p.89 (4)4`,
    block `(4)` and part 4, as `p156C3` is block C and part 3).
The entry id itself never changes. It stays the file name, the link target and the key in every data file.
"""
import re

ID = re.compile(r'^p(\d{3})(.*)$')


def block(rid):
    m = ID.match(rid)
    if not m:
        raise ValueError('not an entry id: %s' % rid)
    suffix = m.group(2)
    if suffix.isdigit():
        return '(%s)%s' % (suffix[0], suffix[1:])
    if suffix.startswith('_'):
        return '?' + suffix[1:]
    return suffix


def label(rec):
    """The label of one record of data/records.json, for example 'p.153 C3'."""
    if not rec['id'].startswith('p%03d' % rec['pdf_page']):
        raise ValueError('%s does not start with its PDF page %s' % (rec['id'], rec['pdf_page']))
    return 'p.%d %s' % (rec['childs_page'], block(rec['id']))
