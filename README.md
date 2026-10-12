# New readings of German ADFGVX messages from November 1918

In the last months of the First World War, the German army enciphered its radio traffic between
Berlin and its outposts in the Balkans, the Black Sea and the Middle East with the ADFGVX cipher.
British and American listening posts intercepted hundreds of these messages. James Rives Childs,
the American officer who worked on them, kept the intercept logs, and they were published as an
appendix to his book in 2000. In 2017 George Lasry, Ingo Niebel, Nils Kopal and Arno Wacker
recovered the keys by computer and read 618 of the 668 cryptograms. A few dozen stayed unread.
Klaus Schmeh lists the remaining ones, 22 messages in all, as #46 on his list of the Top 50
unsolved encrypted messages.

This repository holds readings of two of those messages, the keys and code behind them, and the
checks.

| Childs page | Date (1918) | Call signs | What was done | Status |
|---|---|---|---|---|
| 176, message B part 1 ("2305") | sent 10 Nov at 23.05, intercepted 11 Nov at 03.38 | LP v ZON | Under the known key for 10 to 12 Nov, with four groups (20 symbols) lost in transmission. We located the gap and filled the missing letters back in | **Read.** No earlier published reading found |
| 153, message C parts 5 and 6 | logged under 7 Nov (its header says 3 Nov) | FKR v CGH | Found a new 18 column key that no published key list contains | **Read**, apart from three letters of the signature. No earlier published reading found |

## Contents

- [How ADFGVX works](#how-adfgvx-works)
- [Message 2305, filling in four lost groups](#message-2305-filling-in-four-lost-groups)
- [Page 153, a new key](#page-153-a-new-key)
- [Where the 22 messages stand](#where-the-22-messages-stand)
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
  call signs outside the main network, that George Lasry read in 2017 with a new 16 column key.
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

### Has anyone read it before?

We have not found an earlier reading. Schmeh lists the pair as unsolved. In the 2017 comments on
his blog one commenter only suggests trying Lasry's method on it, and a 2026 repository of claimed
solutions marks it unsolved. Lasry's 2018 thesis, which expands the 2017 paper, contains none of
the reading's phrases. We also searched the web for phrases from the reading, without a hit. That is
not every possible source (Childs's own narrative and Lasry's talks were not checked), so this is
"no earlier reading found", not proof that it is the first.

## Where the 22 messages stand

Klaus Schmeh's list of unsolved ADFGVX messages has 22 entries. We matched each one to Childs's
log by its opening groups. Page numbers are Childs's printed pages.

| Schmeh entry | Page | Date (1918) | Symbols in log | Status | Who, and how |
|---|---|---|---|---|---|
| 1 | 73 | 26 Oct (header says intercepted 8 Nov) | 178 | Unread | None found |
| 2 | 100 | 1 Nov | 122 of 123 | Claimed | Armin, 2017 blog comment, after fixing one group; not checked |
| 3 | 105 | 2 Nov | 290 | Read by others | Norbert, 2017 blog comment, with corrections; spaced version by Max Baertl |
| 4 | 109 | 3 Nov | 258 | Mostly read by others | Norbert, 2017 blog comment, with some garbling |
| 5 | 132 | 5 Nov | 155 (odd) | Partly read by others | Partial readings by Thomas and Norbert, 2017; a full reading is claimed in a 2026 repository, not checked |
| 6 | 146 | 6 Nov | 244 | Read by others | Norbert, 2017 blog comment |
| 7 | 152 | 7 Nov | 104 | Unread | None found |
| 8 and 9 | 153 (two parts) | 7 Nov | 132 + 108 | **Read, apart from three letters of the signature (this repository)** | New 18 column key, October 2026 |
| 10 | 158 | 8 Nov | 241 of 242 | Unread | None found; one symbol short |
| 11 and 12 | 164 (two parts) | 9 Nov | 187 of 242, 131 of 177 | Partly reconstructed by others | Norbert, March 2017; many symbols missing |
| 13 | 170 | 9 Nov | 106 | Unread | None found |
| 14 | 171 | 9 Nov | 315 of 314 | Claimed | Norbert, 2017, transcript corrupted; also claimed in a 2026 repository; not checked |
| 15 | 176 (first) | 10 Nov | 214 of 224 | Partly read by others | Norbert suggested a reading needing corrections, 2017 |
| 16 | 176 (second, message 2305) | 10 Nov | 220 of 240 | **Read (this repository)** | Lost groups filled under the known key, October 2026 |
| 17 | 215 | 22 Nov | 248 | Unread | A 2026 repository calls it probably known; no reading published |
| 18 and 19 | 187 (two parts) | 13 Nov | 212 + 142 | Read by others | George Lasry, May 2017 |
| 20 | 189 | 14 Nov | 90 (header 46) | Unread | None found; transcription unclear |
| 21 | 198 | 15 Nov | 165 of 170 | Unread | None found |
| 22 | 217 | 24 Nov | 170 | Read by others | Prinz, September 2026, with a key from Childs's 1919 typescript |

Readings marked "claimed" were reported in 2017 blog comments or a 2026 repository and have not
been checked here.

Outside Schmeh's list, every other message in Childs's log that reads under one of Lasry's 14
published keys does so in our own run (543 of 688 records). Most of the rest are damaged intercepts
with groups jammed or missing.

## Every message in the log

In October 2026 we decoded everything in Childs's log that we could, with the published keys, and wrote down
one row for each of the 688 log entries. We did this because George Lasry's list of which messages his team
read in 2017 was never published, so nobody outside that team can say which messages are still unread. The
numbers below come from `data/records.json`, and the one line per entry table is [MESSAGES.md](MESSAGES.md).
The decoded text of each entry is under [readings](readings).

| Result | Entries |
|---|---|
| Reads under a published period key exactly as transcribed | 465 |
| Reads under a published period key after repairing the length | 79 |
| Reads after a known key repair of a damaged intercept | 14 reads, 13 partly |
| Leads from filling unread symbols under the window key, some after rereading the page image | 24 |
| Read by this project (page 153 pair and message 2305) | 3, described above |
| Clears its shuffled nulls under a known key but does not read, so no text is given | 16 |
| Not read | 74 |

Twenty six rows are marked pending recheck in the confidence column. A blind reread of the printed pages found that the log row we used differs from the page by more than 5 symbols for those records, so any repair outcome shown for them was computed on the wrong ciphertext. They will be scored again on the page symbols. The earlier confidence stays in brackets.

The log has 688 entries here, while the 2017 paper counts 668 cryptograms. We split a few multipart messages
differently, so the two counts cannot be matched one to one.

How to read the confidence column.

- **high** means the intercept decrypts to German under the period key with nothing changed, or after a
  length repair of the kind Lasry's team described. The decoder here is a few lines of Python and the
  `scripts/verify_all.py` check reproduces all 465 unchanged readings and encrypts them again symbol by symbol.
- **reads, repaired** and **partial reading** are decodes of damaged intercepts under a published key after
  inserting or removing a few symbols. They are scored against shuffled nulls and read by eye.
- **strong, moderate and weak lead** are fills of the unread symbols under the key for that date, scored against a
  thousand shuffled transposition keys with a German letter model. Strong means the margin over the best null
  is at least 40, moderate at least 15. A control test on records others had read showed that about one genuine key
  in nine does not come first, and that a margin below about 20 cannot be told from chance by the score alone.
  A lead is not a confirmed reading.
- Every key here comes from Lasry's 2017 table or Childs's appendix, except the page 153 key.

Credit. Where the entry reads under a period key, the key was found by Lasry, Niebel, Kopal and Wacker in 2017.
This table regenerated the decodes and did not check which messages they published, and their team reports having
left 50 unread. We count 74 not read plus 16 that do not read. Nobody outside that team can say which of those they read. Messages that Norbert, Armin and others read in the 2017 blog comments
are credited to them where the accounting records that.

Sources besides Childs are in [SOURCES.md](SOURCES.md).

## Check it yourself

```
python3 scripts/verify.py
python3 scripts/verify_all.py
```

The second script checks all the decodes in `data/records.json` against their keys in `data/keys.json`.

Python 3.6 or later, standard library only. For each message the script decrypts the intercept
under the stated key, prints the reading in the rows of the transposition block, encrypts it again,
and checks that every surviving intercepted symbol comes back.

`scripts/adfgvx.py` is the cipher itself (about 60 lines), and `data/messages.json` holds the
intercepts as transcribed from Childs's log, with the keys.

The searches that found these keys used the letter count score described above, and
long hill climbing runs (about one CPU hour per search, plus the planted tests and shuffled
controls). They are described above but are not packaged here.

## What this does and does not establish

- **Message 2305 is read.** The gap's position and the message are not in doubt. A few of the
  restored letters and three digits (which depend on the blank cells of the square) could take
  other values without changing the meaning; a second copy of the message would settle them.
- **Page 153 is read, apart from three letters of the signature.** The key is new and the text reads as German.
  Two letters rest on corrections to the log and twelve lost letters were filled by reading; all
  are listed in `data/messages.json`. The prior publication check covered the obvious sources but
  not every possible one.
- **Encrypting again proves consistency, not correctness.** Any reading that uses the key and the
  candidates passes it. The evidence that the readings are right is that they read, beat every
  control, and, for page 153, were found twice independently.

## Sources and credits

- J. Rives Childs, *General Solution of the ADFGVX Cipher System*, reprinted with the intercept logs
  as Appendix B (Aegean Park Press, 2000). All ciphertexts here are transcribed from it.
- George Lasry, Ingo Niebel, Nils Kopal and Arno Wacker, "Deciphering ADFGVX messages from the
  Eastern Front of World War I", *Cryptologia* volume 41, issue 2 (2017). The keys for 10 to 12 November come from
  its key table.
- Klaus Schmeh, ["The Top 50 unsolved encrypted messages, 46. Unsolved ADFGVX cryptograms from
  World War 1"](https://scienceblogs.de/klausis-krypto-kolumne/2017/02/23/the-top-50-unsolved-encrypted-messages-46-unsolved-adfgvx-cryptograms-from-world-war-1/)
  (2017) and its comments, including the digit completion;
  ["Unsolved ADFGVX messages from World War I"](https://scienceblogs.de/klausis-krypto-kolumne/unsolved-adfxvx-messages-from-world-war-i/).

The project was run by Colin Reilly as an amateur experiment in AI assisted codebreaking. Claude
(Anthropic) wrote the search code and found the readings; a second, independent Claude run
reproduced the page 153 key blind.

## License

The code is under the MIT License (see `LICENSE`). The ciphertexts are transcriptions of historical
intercepts.
