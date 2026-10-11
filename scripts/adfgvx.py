"""ADFGVX encryption and decryption, standard library only.

The German system of 1918, as described by Lasry, Niebel, Kopal and Wacker (2017):

1. Substitution. Each plaintext letter or digit is replaced by its row and column
   label in a 6x6 square. Rows and columns are labelled A, D, F, G, V, X.
   The square is given as a 36-character string, read row by row.
2. Transposition. The letters from step 1 are written in rows under a numbered
   key of width n. The columns are read off top to bottom in the order of their
   numbers. The last row may be short; nothing is padded.

`ranks[i]` is the number written above column i, counting from 1.
An unknown square cell is '?'. A ciphertext symbol that is missing in the
intercept is '-', and decrypts to '-'.
"""
COORD = 'ADFGVX'


def _check(ranks):
    if sorted(ranks) != list(range(1, len(ranks) + 1)):
        raise ValueError('the transposition key must be a permutation of 1..n')


def substitute(plain, square):
    cell = {ch: COORD[i // 6] + COORD[i % 6] for i, ch in enumerate(square) if ch != '?'}
    return ''.join(cell[ch] for ch in plain)


def transpose(interim, ranks):
    _check(ranks)
    n = len(ranks)
    columns = [interim[i::n] for i in range(n)]
    return ''.join(columns[i] for i in sorted(range(n), key=lambda i: ranks[i]))


def untranspose(ct, ranks):
    _check(ranks)
    n = len(ranks)
    full, extra = divmod(len(ct), n)
    heights = [full + (i < extra) for i in range(n)]
    columns, p = [None] * n, 0
    for i in sorted(range(n), key=lambda i: ranks[i]):
        columns[i] = ct[p:p + heights[i]]
        p += heights[i]
    return ''.join(columns[i][r] for r in range(full + 1) for i in range(n) if r < heights[i])


def unsubstitute(interim, square):
    out = []
    for k in range(0, len(interim) - 1, 2):
        a, b = interim[k], interim[k + 1]
        out.append(square[COORD.index(a) * 6 + COORD.index(b)] if a in COORD and b in COORD else '-')
    return ''.join(out)


def encrypt(plain, square, ranks):
    return transpose(substitute(plain, square), ranks)


def decrypt(ct, square, ranks):
    return unsubstitute(untranspose(ct, ranks), square)


def rows(text, width):
    """The plaintext as it sits in the transposition block, for display."""
    return [text[i:i + width] for i in range(0, len(text), width)]
