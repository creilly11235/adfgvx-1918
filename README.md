# German ADFGVX messages from November 1918, solved and accounted for

In the last months of the First World War, the German army enciphered its radio traffic between
Berlin and its outposts in the Balkans, the Black Sea and the Middle East with the ADFGVX cipher.
British and American listening posts intercepted hundreds of these messages. James Rives Childs,
the American officer who worked on them, kept the intercept logs, and they were published as an
appendix to his book in 2000. In 2017 George Lasry, Ingo Niebel, Nils Kopal and Arno Wacker
recovered the keys by computer and solved 618 of the 668 cryptograms. A few dozen stayed unsolved.
Klaus Schmeh lists the remaining ones, 22 messages in all, as #46 on his list of the Top 50
unsolved encrypted messages.

This repository holds solutions of two of those messages, the keys and code behind them, and the
checks. It also holds a row and a page for every one of the 688 entries in Childs's log, so that
every message can be followed in one place from the printed page to a translation, with its
status, who found the key and who published the solution.

| Childs page | Date (1918) | Call signs | What was done | Status |
|---|---|---|---|---|
| 176, message B part 1 ("2305") | sent 10 Nov at 23.05, intercepted 11 Nov at 03.38 | LP v ZON | Under the known key for 10 to 12 Nov, with four groups (20 symbols) lost in transmission. We located the gap and filled the missing letters back in | **Solved.** No earlier published solution found |
| 153, message C parts 5 and 6 | logged under 7 Nov (its header says 3 Nov) | FKR v CGH | Found a new 18 column key that no published key list contains | **Solved**, apart from three letters of the signature. No earlier published solution found |

## Contents

- [How ADFGVX works](#how-adfgvx-works)
- [Message 2305, filling in four lost groups](#message-2305-filling-in-four-lost-groups)
- [Page 153, a new key](#page-153-a-new-key)
- [Every message in the log](#every-message-in-the-log)
- [Check it yourself](#check-it-yourself)
- [What this does and does not establish](#what-this-does-and-does-not-establish)
- [Sources and credits](#sources-and-credits)

## How ADFGVX works

The cipher is named after the six letters it transmits. They were chosen because they sound
different in Morse code. Encryption has two steps.

**1. Substitution.** Each plaintext letter or digit is looked up in a 6x6 square and replaced by
its row label and its column label. Here is the square the Germans used from 10 to 12 November 1918.

```
    A D F G V X
A   4 A R U T 1
D   O I F S K N
F   3 5 B Z P V
G   L D 6 J M X
V   C W H Q 2 E
X   7 G 0 8 Y 9
```

ANGRIFF ("attack") becomes `AD DX XD AF DD DF DF`. A is row A column D, N is row D column X, and so on.

**2. Transposition.** The symbols are written in rows under a numbered key, then each column
is read off from top to bottom, in the order of the numbers. Here is a four column key, 3 1 4 2.

```
3 1 4 2

A D D X
X D A F
D D D F
D F
```

Column 1 gives `DDDF`, column 2 `XFF`, column 3 `AXDD`, column 4 `DAD`. The cryptogram is
`DDDFX FFAXD DDAD`. The real keys had 15 to 25 columns and were changed every few days. Each part
of a long message was transposed on its own.

To read a message you need both halves of the key, the order of the columns and the 36 cells of
the square. Neither half on its own produces anything readable, which is what made the cipher hard
in 1918 and still makes short messages hard now.

## Message 2305, filling in four lost groups

### The problem

On page 176 Childs's log has a three part message from LP to ZON. The operator's note says it was
handed in at 23.05 on 10 November and announces three parts. It was intercepted at 03.38 on
11 November, the morning of the Armistice. Parts 2 and 3 read under the key for 10 to 12 November.
Part 1 has stayed unread.

The reason is in the log itself. The header of part 1 says 240 symbols, but the intercept has
only 220, in 44 groups of five. Nothing marks where the missing four groups were. In a transposition
cipher a missing stretch of ciphertext does not just remove a few letters from the end. It shifts
every later column of the block, so decrypting the 220 symbols as they stand gives nothing
readable.

```
GGDAA FXAVD FFFDG XXAGV XXXDV XAAFV GAGAF VFAGA
VDDDD AVXGF FAFXG XXXXX GAVAA AAGDV GGGVA AXDVX
XXFAD FXXXX DGVDG FDVGD DAADV XXXFV XGXXD XGGGG
AGVDG VAGGG DVVDF VAFAV VVXDF DFFFF XXXAX XGVDX
XFXDF FXXDX XXXXV GGGDA FGGDX VVVAA FDVFX XVXXF
VGGFG DAAFV GGGGX AVVVV
```

The key is known. It is Lasry's 16 column transposition for 10 to 12 November,
`9 12 7 11 3 8 16 6 14 2 10 15 5 13 1 4`, and his square. Five cells of his square are blank,
because those digits never occurred in the messages he read. We filled them with the digits
5, 6, 7, 8 and 9 as a commenter on Schmeh's blog proposed in 2017.

### Finding the gap

Lasry's team handled messages with missing symbols by trying groups of blanks at different
places and keeping the place that gave the best German. We did the same thing exhaustively. Every possible position
of the 20 missing symbols was tried, either one block of 20 anywhere in the message, or four separate
groups of five, 194,756 placements in all. For each placement the decryption has 20 known gaps,
and the rest of the message can be scored as German.

One placement stands out. The missing symbols are one block of four groups at position 160,
between the last group of the fourth line of the log and the first group of the fifth. The log
was written eight groups to a line, so these are the first half of the fifth line, an ordinary
half line skip by the operator. The next best placement scores far lower (5.9 natural log units
behind, about 370 times less likely), and it puts 99% of the probability on this one.

Once the gap is placed, the damage is very regular. Under this key the lost symbols are the first
letter of every row of the transposition block, and the second letter of rows 10 to 14. Here
they are shown as underscores.

```
_NXOXHXL _X11XARM _EXALPEN _ORPSRAU _XPETERR _VEXVERB _SZXX217 _216X9XR
_DXLINIE _NAGYBES __EREKXV __SECZXV __SECZXV __SERBEN __SETZTX
```

### Finding the missing letters

Each missing letter has lost one of its two symbols. The surviving symbol still names a row or a
column of the square, so each gap has exactly six candidates, not 36. For the first letter of the
message, for instance, the candidates are the six cells of row A, which are 4, A, R, U, T and 1.

Twenty gaps with six choices each is 6^20, about 3.7 million billion combinations. That is too
many to try one at a time, and it does not need to be. A dynamic program over the message finds
the best scoring combination exactly, along with the runner up and the probability of each
letter. The score is plain counting, the same kind Lasry's team used. It is a table of how often each
run of five letters (ARMEE, XVERS and so on) occurs in the 544 messages of the collection that were
already read, plus ordinary German books. A fill whose letter runs are common in real German
telegrams scores high; one full of rare runs scores low. A person then reads the best fill.

The result reads as German telegram text from start to finish.

```
AN X O X H X L XX 11 X ARMEE X ALPENKORPS RAUM X PETERREVE X VERBASZ XX 217 X 216 X 9 X R X D X
LINIE X NAGYBESKIEREK X VERSECZ X VERSECZ X VON SERBEN BESETZT X
```

("X" is the Germans' full stop and word separator.) Here it is expanded, with the Hungarian place names.

> An O.H.L. 11. Armee. Alpenkorps Raum Péterréve und Verbász. 217., 216., 9. R.D. Linie
> Nagybecskerek bis Versecz. Versecz von Serben besetzt.

> To the Supreme Army Command. 11th Army. Alpine Corps in the area of Péterréve and Verbász.
> 217th, 216th and 9th Reserve Divisions on the line from Nagybecskerek to Versecz. Versecz occupied by the Serbs.

Péterréve (Bačko Petrovo Selo) and Verbász (Vrbas) are in the Bácska. Nagybecskerek (Zrenjanin)
and Versecz (Vršac) are in the Banat. In early November 1918 the German 11th Army was retreating
north out of Serbia across the Danube, and this is its position report on the last night of the
war. Part 2 of the same message carries on with "FEHERTEMPLOM X FOLGEN FRANZOSEN XX
BESATZUNGSHEER ..." (Fehértemplom, now Bela Crkva, is also in the Banat). None of this context
was used in the search.

The reading was checked in several ways.

- **Against shuffled versions of the same message.** Under 12 wrong keys, with the 220 symbols
  shuffled, or with the known letters shuffled, the best fill scores −3.45 to −4.05 per letter.
  The real message scores −2.11.
- **Against planted messages.** We took 60 messages that do read, deleted 20 symbols from each,
  and ran the same procedure. It put the gap in the right place 54 times in 60. The real message
  scores like those (−2.11, against a median of −2.09).
- **By encrypting it again.** The reading, encrypted with the key, gives back all 220 intercepted
  symbols exactly, and the four lost groups come out as `DFFXX DXXVV XDXXX VXXAF`. This only
  proves the reading is consistent with the key, since any choice of the six candidates would
  also pass, but it rules out arithmetic mistakes.
- **Several of the place names appear nowhere else in the collection.** PETERREVE, VERSECZ,
  VON SERBEN and the 216th Division were not in the counted text, so the score could not
  simply have copied them.

## Page 153, a new key

### The messages

Page 153 of Childs's log, under the heading 7 November, has two parts of a message from FKR to CGH,
call signs that appear nowhere else in the collection. The message's own header gives 11.55 p.m. on
"November 3th", and the text refers to an order of 2 November, so it may belong to 3 November.
Parts 1 to 4 are missing. The surviving parts are labelled 5 and 6.

```
Part 5 (132 symbols)
VFVAX FXDAD ADVGX FAVGD VDDDA DXGAA AXVGV FVDAD DXADA DVVAV GFXDA GDDDG DXGGG VVXDX
FVVAV VVFAX FXDXA FAVVG GXAVX VFVXV FGFVA XGAAV XXGDX XFVXF XGGVA DAVAF DG

Part 6 (108 symbols, three groups lost, shown as underscores)
AXVAA _____ _____ _____ DDAFF VAXAG GADAF DXAXX XVDGD XVXFF GXFAV VAADA GXXXA XDDGV
AVAXV AXAAV VXVAV GXAXX FGXXF AAAFX VADFD XVF
```

Both parts have the right length for their headers. Neither reads under any of the 14 keys Lasry
published, nor under Childs's keys. The key on the main network for 7 to 9 November had 20
columns. Lasry's team reported 14 cryptograms of the right length that no key opened, and suspected
most of them had been wrongly encrypted. This pair shows that at least some were simply under a
key nobody had recovered.

### Why this is hard

Together the two parts give 240 symbols, 120 letters, and 15 of those symbols are lost. That is
very short for an ADFGVX key search. Lasry's method recovered keys from a day's worth of
traffic, often thousands of symbols. With 120 letters the usual statistics (letter frequencies and
coincidence counts) carry almost no signal, and a plain hill climb over both halves of the key
never found a planted key of this size in our tests.

### The method

The search uses one structural fact. When the transposition key has an even number of columns,
every column of the block holds only row labels or only column labels, because the symbols
alternate row, column, row, column along each row. In German telegrams some rows and some columns
of the square are used much more than others, so the two kinds of column have different mixtures of
A, D, F, G, V and X. That makes it possible to sort the cryptogram's columns into the two kinds
before knowing anything else about the key.

1. **Split.** Try every way of cutting each part into columns of the right lengths, and keep the
   splits whose columns fall cleanly into two groups by symbol counts. In tests the true split
   was usually among the top few of tens of thousands.
2. **Pair and order.** Each row label column must sit next to a column label column. Try the
   pairings and orders, ranking them by how repetitive the resulting letter stream is (its index
   of coincidence).
3. **Solve the square.** For each surviving column order, find the best square by hill climbing
   against the same letter count score, first briefly for all candidates and then at length for
   the best 200.

The search was tested before it was run on page 153. We planted 24 messages with the same
geometry (two parts, 66 and 54 letters, 15 symbols lost in the second) under random 18 column keys.
The search recovered the exact key in 10 of 24, and every exact recovery scored at least −268.0.

### The key

Transposition, 18 columns, `16 7 13 4 15 8 17 3 1 12 14 2 5 9 10 18 11 6`

Square, with the 24 cells the two parts use (the other 12 never occur, so they stay unknown).

```
    A D F G V X
A   . T X U G I
D   . . . . 8 .
F   2 W O . C M
G   B 1 . S Z .
V   5 N D H . V
X   E A . . L R
```

This is a different key from every one in Lasry's table and in Childs's appendix. The only other
18 column key in Lasry's table, for 28 to 31 October, has a different order and square.

### The reading

Part 5 decrypts cleanly, every letter. Part 6 has 15 letters that each lost one of their two
symbols in the three blank groups. As with message 2305, each of these has six candidates. Twelve
of them are fixed by the words around them, and three, near the end, stay open. Two other letters
in part 6 need a correction to the log. In each, the first symbol is written A where the German
needs X (the details are in `data/messages.json`). Laid out in the rows of the transposition
block, with the filled letters in lower case and the open ones as underscores.

```
Part 5              Part 6
ANORDNUNG           MuNiTiONS
ENVOM2TEN           BeStAnDDE
11TENNR85           RNAcHhUTA
8BEZIEHEN           RTIlLeRIE
LASSENSOW           MELdEnX8X
EITNOCHNI           GXR___BXA
CHTGESCHE
HEN
```

The second L of ARTILLERIE and the E of MELDEN are the two corrected letters. With word breaks it reads as follows.

```
ANORDNUNGEN VOM 2TEN 11TEN NR 858 BEZIEHEN LASSEN SOWEIT NOCH NICHT GESCHEHEN
MUNITIONSBESTAND DER NACHHUT ARTILLERIE MELDEN X 8 X G X R _ _ _ B X A
```

> Anordnungen vom 2. 11., Nr. 858, beziehen lassen, soweit noch nicht geschehen.
> Munitionsbestand der Nachhutartillerie melden. 8 G R . . . B A

> Have the orders of 2 November, No. 858, drawn, as far as this has not yet been done. Report the
> ammunition stock of the rear guard artillery. [8 G R ... B A]

The closing letters are probably a unit and a signature; with three letters open we do not try to
expand them. The open letters each have six candidates. The first and third are in row A of the
square (T, X, U, G, I, or the unknown cell AA), the second in column V (G, 8, C, Z, L, or the
unknown cell VV).

Parts 1 to 4 are not in Childs's log, so the start of the message is lost. What survives is a
routine order from the retreat, to pass on an earlier order and report how much ammunition the
artillery of the rear guard still has.

### How we know it is right

- **It reads.** Part 5 reads as German from the first letter to the last under the key, with no
  help. Part 6 reads once the lost letters are filled, and every fill is one of its six candidates.
- **It beats everything else by a wide margin.** The winning key scores −266.7. The next distinct
  key scores −283.4. The same search run on ten shuffled copies of the pair, with the same symbols
  in random order, never scored better than −301.1.
- **It scores like a genuine message.** The planted test messages that the search recovered scored
  −268.0 or better; the real pair scores −266.7.
- **A second, independent search found the same key.** A separate run, written without seeing the
  first result and using its own version of the method, recovered the identical 18 column order.
  The two squares agreed on 17 of the 25 cells compared. The cells they disagreed on were settled
  by words that repeat in part 5 (ANORDNUNGEN and GESCHEHEN fix G, VOM fixes M and V, BEZIEHEN
  fixes B).
- **The same method finds known keys.** Page 187 has a two part message of 13 November, also on
  call signs outside the main network, whose reading George Lasry published in 2017 with a new 16 column key.
  Run blind on that pair, with nothing to go on but the ciphertext, the search returned Lasry's key
  exactly, with the same column order (`3 13 2 12 1 11 15 8 9 4 5 14 6 10 7 16`) and the same 22
  square cells he published, scoring −283.4 against −429.0 for the next key.
- **It reproduces.** Rerunning the search from scratch for this write up gave the same key and
  the same score.
- **The key fits nowhere else.** It does not decrypt any of 40 other unread messages from
  6 to 9 November, and none of the 19 published squares fits page 153 at any width from 15 to 25.
- **Encrypting it again.** Of the 225 surviving symbols in the two parts, 220 come back exactly when
  the reading is encrypted again. The other five are the two corrected symbols and the three open
  letters.

### Has anyone solved it before?

We looked for an earlier solution of this pair and found none. Schmeh lists it as unsolved, the
2017 comments on his post only suggest trying a key search on it, the 2018 thesis that expands
the 2017 paper holds none of its phrases, and a web search for phrases from the reading found
nothing. Not every source was checked, so this is a solution with no earlier solution found, not a
claim to be the first.

## Every message in the log

The two solutions above are two entries out of 688 in Childs's log. In October 2026 we decrypted
every entry we could with the published keys and with our own, repaired the damaged intercepts
where a repair could be scored against shuffled copies of itself, read the pages again where the
log and the print disagreed, and wrote one row for each entry. Here is where the entries stand.

| Status | Entries | No published solution found | Meaning |
|---|---|---|---|
| Solved | 550 | 543 | every surviving symbol decrypts under the key and the text reads as German, as transcribed or after a length repair |
| Solved with open letters | 12 | 0 | the whole message reads, with the letters that a reader filled or left open marked in the text |
| Partially solved | 1 | 0 | part of the message reads and the rest is undetermined |
| Unsolved | 120 |  | no solution is published here, and the last column names a solution published elsewhere where we found one |
| No cipher text | 4 |  | the log prints no symbols for the entry |
| Duplicate entry | 1 |  | the log row joins the symbols of two other entries |
| Total | 688 | 543 | |

[MESSAGES.md](MESSAGES.md) has the row for every entry, a section that matches the 22 entries on
Schmeh's list to the log, and the key to the message pages. Each row names who found the key and
who published the solution. Each entry has its own page under [messages](messages), which follows
it from the printed book to an English translation in six steps and carries the detail behind its
status, the edits, the scores and the open letters.

The third column counts the solved entries for which our search of the 2017 paper and thesis, the
comments on Schmeh's posts and the web found no published solution. It records the outcome of that
search and nothing more. The 2017 paper reports 618 of 668 cryptograms recovered and gives no list
by entry, and the log is split into 688 entries here, so the two totals cannot be matched one to
one. All but three of the solved entries use a key from the 2017 paper, and the key column on each
row says so.

Solved means that every surviving symbol decrypts under the key and the text reads as German. Where
a reader filled or left open a few letters, the row says how many, and the text on the page marks
them. Partially solved means that part of the message reads and the rest is undetermined. A digit
or a signature letter that could take another value does not make a message partial, since there
is no word behind it to decide. Leads that have not passed the project's gate, repairs read by eye,
and rows whose log text differs from the printed page are not published here, so an unsolved row
says only that no solution is published here. Where someone else published a solution, the last
column of the row names them.

## Check it yourself

```
python3 scripts/verify.py
python3 scripts/verify_all.py
python3 scripts/make_pages.py .
```

The first script reproduces the two solutions above. The second checks every decode in
`data/records.json` against its key in `data/keys.json`. The third rebuilds the message pages
from the data files.

Python 3.6 or later, standard library only. For each message the scripts decrypt the intercept
under the stated key, print the reading in the rows of the transposition block, encrypt it again,
and check that every surviving intercepted symbol comes back.

`scripts/adfgvx.py` is the cipher itself (about 60 lines), and `data/messages.json` holds the two
solutions' intercepts as transcribed from Childs's log, with their keys. Every key in `data/keys.json`
comes from Lasry's 2017 table or Childs's appendix, except the page 153 key.

The searches that found the page 153 key used the letter count score described above and long
hill climbing runs (about one CPU hour per search, plus the planted tests and shuffled controls).
They are described above but are not packaged here.

## What this does and does not establish

- **Message 2305 is solved.** The gap's position and the message are not in doubt. A few of the
  restored letters and three digits (which depend on the blank cells of the square) could take
  other values without changing the meaning; a second copy of the message would settle them.
- **Page 153 is solved, apart from three letters of the signature.** The key is new and the text reads as German.
  Two letters rest on corrections to the log and twelve lost letters were filled by reading; all
  are listed in `data/messages.json`. The prior publication check covered the obvious sources but
  not every possible one.
- **The table is an account of what is solved, not of who solved it first.** Each row names who
  found its key. Whether anyone published the solution of a given entry is confirmed only where
  a name stands in the last column.
- **Encrypting again proves consistency, not correctness.** Any reading that uses the key and the
  candidates passes it. The evidence that the solutions are right is that they read, beat every
  control, and, for page 153, were found twice independently.

## Sources and credits

- J. Rives Childs, *General Solution of the ADFGVX Cipher System*, reprinted with the intercept logs
  as Appendix B (Aegean Park Press, 2000). All ciphertexts here are transcribed from it. The scan
  is the free PDF offered through [Richard Bean's index of Aegean Park Press books](https://richardbean.id.au/misc/kryptos/aegean-park-press.html).
- George Lasry, Ingo Niebel, Nils Kopal and Arno Wacker, "Deciphering ADFGVX messages from the
  Eastern Front of World War I", *Cryptologia* volume 41, issue 2 (2017). Every period key in the
  table comes from its key table, and every entry solved under one names the authors as the finders of its key.
- Klaus Schmeh, ["The Top 50 unsolved encrypted messages, 46. Unsolved ADFGVX cryptograms from
  World War 1"](https://scienceblogs.de/klausis-krypto-kolumne/2017/02/23/the-top-50-unsolved-encrypted-messages-46-unsolved-adfgvx-cryptograms-from-world-war-1/)
  (2017) and its comments, including the digit completion;
  ["Unsolved ADFGVX messages from World War I"](https://scienceblogs.de/klausis-krypto-kolumne/unsolved-adfxvx-messages-from-world-war-i/).
  Solutions of entries on that list published in its comments in 2017 by Norbert, Armin, Thomas,
  Max Baertl and George Lasry, and in 2026 by Prinz, are credited to them on their rows.

Other sources, and the archives where more messages could still be found, are in [SOURCES.md](SOURCES.md).

The project was run by Colin Reilly as an amateur experiment in AI assisted codebreaking. Claude
(Anthropic) wrote the search code and found the solutions; a second, independent Claude run
reproduced the page 153 key blind.

## License

The code is under the MIT License (see `LICENSE`). The ciphertexts are transcriptions of historical
intercepts.
