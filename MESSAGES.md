# Every message in Childs's log

One row per log entry, in log order. The columns are the entry (its label and, in code type, its internal id), Childs's printed page, the date, the key, the status, who found the key and who published a solution.
Each entry label links to its page under `messages`, which follows the message from the printed page to the English translation and carries the detail behind the status.

## Printed page and entry id

Cite an entry by its printed page and block, for example `p.153 C3`. That is the page number in Childs's book, the one that Schmeh's list and other researchers use. Each entry also has an internal id, here `p156C3`, which is the page of the scanned PDF plus the block. The PDF page is exactly 3 more than the printed page on all 688 entries, so the id `p156C3` is on printed page 153. The id is the file name, the link target and the key in the data files, and it never changes. A `?` in place of a block letter stands for the `_` that the id uses where it records no block letter; the log's heading for that entry may still show a mark, and step 1 of its page gives the heading, and a digit in brackets such as `(4)` is a block whose letter the log's heading reads as a digit. `python3 scripts/verify_labels.py` checks that the 688 labels are distinct and map one to one to the ids.

## Where the entries stand

Every entry is in exactly one row.

| Status | Entries | No published solution found | Meaning |
|---|---|---|---|
| Solved | 550 | 542 | every surviving symbol decrypts under the key and the text reads as German, as transcribed or after a length repair |
| Solved with open letters | 44 | 0 | the whole message reads, with the letters that a reader filled or left open marked in the text |
| Partially solved | 4 | 0 | part of the message reads and the rest is undetermined |
| Unsolved | 83 |  | no solution is published here, and the last column names a solution published elsewhere where we found one |
| No cipher text | 6 |  | the log prints no cipher block for the entry, or only a header that quotes a few symbols of another entry's block |
| Duplicate entry | 1 |  | the log row joins the symbols of two other entries |
| Total | 688 | 542 | |

The third column counts the solved entries for which our search of the 2017 paper and thesis, the comments on Schmeh's posts and the web found no published solution. It records the outcome of that search and nothing more. The 2017 paper reports 618 of 668 cryptograms recovered and gives no list by entry, and the log is split into 688 entries here, so the two totals cannot be matched one to one. Leads and partial repairs that have not passed the project's gate are not published here, so an unsolved row says only that no solution is published.

## How to read a message page

Every entry has a page under `messages`, named by the entry id, for example `messages/p156C3.md`. The heading of a page is the printed-page label, for example `p.153 C3`, and the next line gives the internal id. The line after that gives the page in Childs, the date, the key, the status, who found the key and who published a solution, and the second line the detail behind the status. Then come six steps.

1. **Printed.** The book, the printed page, the PDF page and the heading that Childs's log gives the message.
2. **Transcribed as printed.** The intercept symbols exactly as the log prints them, in groups of five. A dash is a symbol that is missing or unreadable in the print.
3. **Repaired or edited transcription.** The symbols after any repair, such as a symbol put back, a symbol taken out, or a block moved. A symbol that the repair changed, inserted or filled is written in lowercase, and the edits are listed in words under the line. If nothing was edited the page says so.
4. **Decrypted as it stands.** The printed transcription decrypted with the key and no repair, so that a reader can see what the repair bought.
5. **Decrypted after repair.** The solution from the repaired transcription.
6. **English translation.** A machine translation of the German, not yet checked by a German reader. The German is repeated in phrases above the English.

Unsolved entries show steps 1 to 3 only. Where the log holds no symbols for an entry, steps 2 and 4 say so and step 3 comes from the page reading.

One marking convention is used on every page. In the ciphertext a dash is a symbol missing in the print, and in step 3 a lowercase symbol was changed, inserted or filled by the repair. In the German an UPPERCASE letter has both of its symbols in the print and unedited, a lowercase letter has one or both symbols supplied by the repair, an underscore is a letter that could not be determined, a hash mark is a digit that could not be determined, and X stands for a space or a full stop, as the German operators used it. In the English a phrase in square brackets followed by a question mark rests on at least one lowercase, underscore or hash character, so its translation is uncertain.

The pages are written by `scripts/make_pages.py` from `data/records.json`, `data/keys.json`, `data/messages.json` and `data/translations.json`. Run `python3 scripts/make_pages.py .` to rebuild them.

## The table

| Entry | Page | Date | Key | Status | Key found by | Solution published by |
|---|---|---|---|---|---|---|
| [p.56 A](messages/p059A.md) `p059A` | 56 | 19 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.56 B](messages/p059B.md) `p059B` | 56 | 19 September | sep19 | Solved, 3 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.56 B.2](messages/p059B.2.md) `p059B.2` | 56 | 19 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.57 A1](messages/p060A1.md) `p060A1` | 57 | 20 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.57 A2](messages/p060A2.md) `p060A2` | 57 | 20 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.57 A3](messages/p060A3.md) `p060A3` | 57 | 20 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.58 ?](messages/p061_.md) `p061_` | 58 | 21 September |  | No cipher text |  |  |
| [p.58 ?.2](messages/p061_.2.md) `p061_.2` | 58 | 21 September |  | No cipher text |  |  |
| [p.58 ?.3](messages/p061_.3.md) `p061_.3` | 58 | 21 September |  | No cipher text |  |  |
| [p.58 B](messages/p061B.md) `p061B` | 58 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.59 A](messages/p062A.md) `p062A` | 59 | 21 September |  | Unsolved |  |  |
| [p.59 A2](messages/p062A2.md) `p062A2` | 59 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.59 A3](messages/p062A3.md) `p062A3` | 59 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.59 B](messages/p062B.md) `p062B` | 59 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.60 A1](messages/p063A1.md) `p063A1` | 60 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.60 A2](messages/p063A2.md) `p063A2` | 60 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.60 B2](messages/p063B2.md) `p063B2` | 60 | 21 September |  | No cipher text |  |  |
| [p.60 B](messages/p063B.md) `p063B` | 60 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.61 A](messages/p064A.md) `p064A` | 61 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.62 A](messages/p065A.md) `p065A` | 62 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.62 B](messages/p065B.md) `p065B` | 62 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.63 A](messages/p066A.md) `p066A` | 63 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.64 A](messages/p067A.md) `p067A` | 64 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.64 A2](messages/p067A2.md) `p067A2` | 64 | 4 October | oct04 | Solved, 23 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.64 (4)](messages/p0674.md) `p0674` | 64 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.65 A](messages/p068A.md) `p068A` | 65 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.66 A](messages/p069A.md) `p069A` | 66 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.66 B](messages/p069B.md) `p069B` | 66 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.66 B1](messages/p069B1.md) `p069B1` | 66 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.67 A3](messages/p070A3.md) `p070A3` | 67 | 5 October | oct04 | Solved, 27 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.67 B](messages/p070B.md) `p070B` | 67 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.67 C](messages/p070C.md) `p070C` | 67 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.68 A1](messages/p071A1.md) `p071A1` | 68 | 5 October |  | Unsolved |  |  |
| [p.68 A2](messages/p071A2.md) `p071A2` | 68 | 5 October |  | Unsolved |  |  |
| [p.69 A](messages/p072A.md) `p072A` | 69 | 5 October |  | Unsolved |  |  |
| [p.69 B1](messages/p072B1.md) `p072B1` | 69 | 5 October |  | Unsolved |  |  |
| [p.69 B3](messages/p072B3.md) `p072B3` | 69 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.70 A1](messages/p073A1.md) `p073A1` | 70 | 6 October | oct04 | Solved, 20 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.70 A2](messages/p073A2.md) `p073A2` | 70 | 6 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.70 B](messages/p073B.md) `p073B` | 70 | 6 October |  | Unsolved |  |  |
| [p.71 A](messages/p074A.md) `p074A` | 71 | 6 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.71 A.2](messages/p074A.2.md) `p074A.2` | 71 | 6 October |  | Unsolved |  |  |
| [p.72 A1](messages/p075A1.md) `p075A1` | 72 | 6 October | oct04 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.72 A2](messages/p075A2.md) `p075A2` | 72 | 6 October | oct04 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.72 A3](messages/p075A3.md) `p075A3` | 72 | 6 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.72 B](messages/p075B.md) `p075B` | 72 | 6 October | oct04 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.73 A](messages/p076A.md) `p076A` | 73 | 26 October |  | Unsolved |  |  |
| [p.74 A](messages/p077A.md) `p077A` | 74 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.74 B](messages/p077B.md) `p077B` | 74 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.74 C](messages/p077C.md) `p077C` | 74 | 28 October | oct28 | Solved, 30 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.74 C2](messages/p077C2.md) `p077C2` | 74 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.75 A](messages/p078A.md) `p078A` | 75 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.75 B](messages/p078B.md) `p078B` | 75 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.75 B.2](messages/p078B.2.md) `p078B.2` | 75 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.76 (4)3](messages/p07943.md) `p07943` | 76 | 28 October | oct28 | Solved, 3 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.77 A](messages/p080A.md) `p080A` | 77 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.77 B](messages/p080B.md) `p080B` | 77 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.78 A](messages/p081A.md) `p081A` | 78 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.78 A2](messages/p081A2.md) `p081A2` | 78 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.79 A1](messages/p082A1.md) `p082A1` | 79 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.79 A2](messages/p082A2.md) `p082A2` | 79 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.80 A](messages/p083A.md) `p083A` | 80 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.80 B1](messages/p083B1.md) `p083B1` | 80 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.80 B2](messages/p083B2.md) `p083B2` | 80 | 30 October |  | Unsolved |  |  |
| [p.80 B](messages/p083B.md) `p083B` | 80 | 30 October |  | Unsolved |  |  |
| [p.81 A](messages/p084A.md) `p084A` | 81 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.81 B](messages/p084B.md) `p084B` | 81 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.81 C](messages/p084C.md) `p084C` | 81 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.82 A1](messages/p085A1.md) `p085A1` | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.82 A2](messages/p085A2.md) `p085A2` | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.82 A3](messages/p085A3.md) `p085A3` | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.82 A](messages/p085A.md) `p085A` | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.83 A](messages/p086A.md) `p086A` | 83 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.83 B2](messages/p086B2.md) `p086B2` | 83 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.84 A](messages/p087A.md) `p087A` | 84 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.84 B](messages/p087B.md) `p087B` | 84 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.84 C](messages/p087C.md) `p087C` | 84 | 30 October |  | Unsolved |  |  |
| [p.85 A](messages/p088A.md) `p088A` | 85 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.85 B](messages/p088B.md) `p088B` | 85 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.86 A](messages/p089A.md) `p089A` | 86 | 31 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.86 B2](messages/p089B2.md) `p089B2` | 86 | 31 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.86 C1](messages/p089C1.md) `p089C1` | 86 | 31 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.87 A1](messages/p090A1.md) `p090A1` | 87 | 31 October | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.88 A1](messages/p091A1.md) `p091A1` | 88 | 1 November | nov01 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.88 A3](messages/p091A3.md) `p091A3` | 88 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.88 B](messages/p091B.md) `p091B` | 88 | 1 November | nov01 | Solved, 4 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.88 C1](messages/p091C1.md) `p091C1` | 88 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.89 (4)](messages/p0924.md) `p0924` | 89 | 1 November |  | Unsolved |  |  |
| [p.89 (4)4](messages/p09244.md) `p09244` | 89 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.90 (4)5](messages/p09345.md) `p09345` | 90 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.90 B1](messages/p093B1.md) `p093B1` | 90 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.91 ?2](messages/p094_2.md) `p094_2` | 91 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.91 ?3](messages/p094_3.md) `p094_3` | 91 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.92 A](messages/p095A.md) `p095A` | 92 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.92 B1](messages/p095B1.md) `p095B1` | 92 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.93 A2](messages/p096A2.md) `p096A2` | 93 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.93 A](messages/p096A.md) `p096A` | 93 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.93 A4](messages/p096A4.md) `p096A4` | 93 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.94 A5](messages/p097A5.md) `p097A5` | 94 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.94 A6](messages/p097A6.md) `p097A6` | 94 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.95 A](messages/p098A.md) `p098A` | 95 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.95 A2](messages/p098A2.md) `p098A2` | 95 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.96 A](messages/p099A.md) `p099A` | 96 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.96 B](messages/p099B.md) `p099B` | 96 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.97 (4)](messages/p1004.md) `p1004` | 97 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.97 B](messages/p100B.md) `p100B` | 97 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.97 C](messages/p100C.md) `p100C` | 97 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.98 A](messages/p101A.md) `p101A` | 98 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.98 A2](messages/p101A2.md) `p101A2` | 98 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.98 B2](messages/p101B2.md) `p101B2` | 98 | 1 November |  | Unsolved |  |  |
| [p.98 B](messages/p101B.md) `p101B` | 98 | 1 November |  | Unsolved |  |  |
| [p.99 A](messages/p102A.md) `p102A` | 99 | 1 November |  | Unsolved |  |  |
| [p.99 B](messages/p102B.md) `p102B` | 99 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.99 C](messages/p102C.md) `p102C` | 99 | 1 November |  | Unsolved |  |  |
| [p.99 C3](messages/p102C3.md) `p102C3` | 99 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.99 D](messages/p102D.md) `p102D` | 99 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.100 A](messages/p103A.md) `p103A` | 100 | 1 November | nov01 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | Armin, 2017, claimed |
| [p.100 B](messages/p103B.md) `p103B` | 100 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.100 C](messages/p103C.md) `p103C` | 100 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.100 D1](messages/p103D1.md) `p103D1` | 100 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.101 A2](messages/p104A2.md) `p104A2` | 101 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.101 B2](messages/p104B2.md) `p104B2` | 101 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.101 ?1](messages/p104_1.md) `p104_1` | 101 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.101 D2](messages/p104D2.md) `p104D2` | 101 | 1 November |  | Unsolved |  |  |
| [p.102 D](messages/p105D.md) `p105D` | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.102 B1](messages/p105B1.md) `p105B1` | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.102 B2](messages/p105B2.md) `p105B2` | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.102 B3](messages/p105B3.md) `p105B3` | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.102 C](messages/p105C.md) `p105C` | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.102 D.2](messages/p105D.2.md) `p105D.2` | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.103 A](messages/p106A.md) `p106A` | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.103 B1](messages/p106B1.md) `p106B1` | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.103 B](messages/p106B.md) `p106B` | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.103 C](messages/p106C.md) `p106C` | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.103 D](messages/p106D.md) `p106D` | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.104 A3](messages/p107A3.md) `p107A3` | 104 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.104 B](messages/p107B.md) `p107B` | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.104 C](messages/p107C.md) `p107C` | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.104 C2](messages/p107C2.md) `p107C2` | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.104 D](messages/p107D.md) `p107D` | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.104 E3](messages/p107E3.md) `p107E3` | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.105 A](messages/p108A.md) `p108A` | 105 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.105 BB](messages/p108BB.md) `p108BB` | 105 | 2 November | nov01 | Solved, 5 open | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert and Max Baertl, 2017 |
| [p.105 C](messages/p108C.md) `p108C` | 105 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.106 A](messages/p109A.md) `p109A` | 106 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.106 A3](messages/p109A3.md) `p109A3` | 106 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.106 B](messages/p109B.md) `p109B` | 106 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.107 A](messages/p110A.md) `p110A` | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.107 B1](messages/p110B1.md) `p110B1` | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.107 B2](messages/p110B2.md) `p110B2` | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.107 C](messages/p110C.md) `p110C` | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.107 D](messages/p110D.md) `p110D` | 107 | 2 November |  | Unsolved |  |  |
| [p.108 A](messages/p111A.md) `p111A` | 108 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.108 B2](messages/p111B2.md) `p111B2` | 108 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.108 B2.2](messages/p111B2.2.md) `p111B2.2` | 108 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.109 A2](messages/p112A2.md) `p112A2` | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.109 A3](messages/p112A3.md) `p112A3` | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.109 B](messages/p112B.md) `p112B` | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.109 C1](messages/p112C1.md) `p112C1` | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.109 C](messages/p112C.md) `p112C` | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.109 D](messages/p112D.md) `p112D` | 109 | 3 November |  | Unsolved |  | Norbert, 2017, in part |
| [p.110 A](messages/p113A.md) `p113A` | 110 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.110 B](messages/p113B.md) `p113B` | 110 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.110 C](messages/p113C.md) `p113C` | 110 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.111 A](messages/p114A.md) `p114A` | 111 | 3 November |  | Unsolved |  |  |
| [p.111 B](messages/p114B.md) `p114B` | 111 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.112 A1](messages/p115A1.md) `p115A1` | 112 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.112 A2](messages/p115A2.md) `p115A2` | 112 | 3 November | nov01 | Solved, 20 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.112 A2.2](messages/p115A2.2.md) `p115A2.2` | 112 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.112 B](messages/p115B.md) `p115B` | 112 | 3 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.112 (4)](messages/p1154.md) `p1154` | 112 | 4 November |  | Unsolved |  |  |
| [p.112 D](messages/p115D.md) `p115D` | 112 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.113 A](messages/p116A.md) `p116A` | 113 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.113 B9](messages/p116B9.md) `p116B9` | 113 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.113 C](messages/p116C.md) `p116C` | 113 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.113 D1](messages/p116D1.md) `p116D1` | 113 | 3 November | nov01 | Solved, 5 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.114 A1](messages/p117A1.md) `p117A1` | 114 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.114 A4](messages/p117A4.md) `p117A4` | 114 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.115 A5](messages/p118A5.md) `p118A5` | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.115 A6](messages/p118A6.md) `p118A6` | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.115 A7](messages/p118A7.md) `p118A7` | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.115 A8](messages/p118A8.md) `p118A8` | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.116 A](messages/p119A.md) `p119A` | 116 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.116 A.2](messages/p119A.2.md) `p119A.2` | 116 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.116 A.3](messages/p119A.3.md) `p119A.3` | 116 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.116 A1](messages/p119A1.md) `p119A1` | 116 | 3 November |  | Unsolved |  |  |
| [p.117 A](messages/p120A.md) `p120A` | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.117 B](messages/p120B.md) `p120B` | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.117 C3](messages/p120C3.md) `p120C3` | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.117 C4](messages/p120C4.md) `p120C4` | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.117 D](messages/p120D.md) `p120D` | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.118 A](messages/p121A.md) `p121A` | 118 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.119 A](messages/p122A.md) `p122A` | 119 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.120 A](messages/p123A.md) `p123A` | 120 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.120 B1](messages/p123B1.md) `p123B1` | 120 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.120 C](messages/p123C.md) `p123C` | 120 | 4 November |  | Unsolved |  |  |
| [p.121 A1](messages/p124A1.md) `p124A1` | 121 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.121 A2](messages/p124A2.md) `p124A2` | 121 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.121 B1](messages/p124B1.md) `p124B1` | 121 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.122 A2](messages/p125A2.md) `p125A2` | 122 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.122 B](messages/p125B.md) `p125B` | 122 | 4 November |  | Unsolved |  |  |
| [p.122 C](messages/p125C.md) `p125C` | 122 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.122 D1](messages/p125D1.md) `p125D1` | 122 | 4 November |  | Unsolved |  |  |
| [p.123 A2](messages/p126A2.md) `p126A2` | 123 | 4 November | nov04 | Solved, 18 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.123 A3](messages/p126A3.md) `p126A3` | 123 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.123 B](messages/p126B.md) `p126B` | 123 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.124 B1](messages/p127B1.md) `p127B1` | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.124 B2](messages/p127B2.md) `p127B2` | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.124 B3](messages/p127B3.md) `p127B3` | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.124 B](messages/p127B.md) `p127B` | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.125 A1](messages/p128A1.md) `p128A1` | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.125 A2](messages/p128A2.md) `p128A2` | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.125 A3](messages/p128A3.md) `p128A3` | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.125 A4](messages/p128A4.md) `p128A4` | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.126 A5](messages/p129A5.md) `p129A5` | 126 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.126 A6](messages/p129A6.md) `p129A6` | 126 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.126 B](messages/p129B.md) `p129B` | 126 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.127 A3](messages/p130A3.md) `p130A3` | 127 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.127 B1](messages/p130B1.md) `p130B1` | 127 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.127 B2](messages/p130B2.md) `p130B2` | 127 | 4 November |  | Unsolved |  |  |
| [p.128 A1](messages/p131A1.md) `p131A1` | 128 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.128 A2](messages/p131A2.md) `p131A2` | 128 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.128 B1](messages/p131B1.md) `p131B1` | 128 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.129 A7](messages/p132A7.md) `p132A7` | 129 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.129 A8](messages/p132A8.md) `p132A8` | 129 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.129 B1](messages/p132B1.md) `p132B1` | 129 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.130 A1](messages/p133A1.md) `p133A1` | 130 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.130 A2](messages/p133A2.md) `p133A2` | 130 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.131 A3](messages/p134A3.md) `p134A3` | 131 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.131 A4](messages/p134A4.md) `p134A4` | 131 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.131 B](messages/p134B.md) `p134B` | 131 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.132 ?](messages/p135_.md) `p135_` | 132 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.132 B](messages/p135B.md) `p135B` | 132 | 5 November | nov04 | Solved, 23 open | Lasry, Niebel, Kopal and Wacker, 2017 | Thomas and Norbert, 2017, in part |
| [p.132 C](messages/p135C.md) `p135C` | 132 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.133 A2](messages/p136A2.md) `p136A2` | 133 | 5 November | nov04 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.133 A3](messages/p136A3.md) `p136A3` | 133 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.134 A4](messages/p137A4.md) `p137A4` | 134 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.134 B](messages/p137B.md) `p137B` | 134 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.135 A](messages/p138A.md) `p138A` | 135 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.136 A1](messages/p139A1.md) `p139A1` | 136 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.136 A2](messages/p139A2.md) `p139A2` | 136 | 5 November |  | Unsolved |  |  |
| [p.136 B](messages/p139B.md) `p139B` | 136 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.136 B3](messages/p139B3.md) `p139B3` | 136 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.137 A4](messages/p140A4.md) `p140A4` | 137 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.137 A5](messages/p140A5.md) `p140A5` | 137 | 6 November |  | Unsolved |  |  |
| [p.137 A6](messages/p140A6.md) `p140A6` | 137 | 6 November |  | Unsolved |  |  |
| [p.137 B](messages/p140B.md) `p140B` | 137 | 6 November |  | Unsolved |  |  |
| [p.137 B4](messages/p140B4.md) `p140B4` | 137 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.137 B.2](messages/p140B.2.md) `p140B.2` | 137 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.137 B.3](messages/p140B.3.md) `p140B.3` | 137 | 6 November | nov04 | Solved, 13 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.138 A](messages/p141A.md) `p141A` | 138 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.138 A.2](messages/p141A.2.md) `p141A.2` | 138 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.138 B](messages/p141B.md) `p141B` | 138 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.138 B.2](messages/p141B.2.md) `p141B.2` | 138 | 6 November |  | Unsolved |  |  |
| [p.139 A1](messages/p142A1.md) `p142A1` | 139 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.139 A2](messages/p142A2.md) `p142A2` | 139 | 6 November |  | Unsolved |  |  |
| [p.139 A](messages/p142A.md) `p142A` | 139 | 6 November |  | Unsolved |  |  |
| [p.139 A.2](messages/p142A.2.md) `p142A.2` | 139 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.140 ?1](messages/p143_1.md) `p143_1` | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.140 ?2](messages/p143_2.md) `p143_2` | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.140 ?3](messages/p143_3.md) `p143_3` | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.140 ?4](messages/p143_4.md) `p143_4` | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.140 B](messages/p143B.md) `p143B` | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.141 A1](messages/p144A1.md) `p144A1` | 141 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.141 A2](messages/p144A2.md) `p144A2` | 141 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.141 B](messages/p144B.md) `p144B` | 141 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.142 A](messages/p145A.md) `p145A` | 142 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.142 B](messages/p145B.md) `p145B` | 142 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.142 C](messages/p145C.md) `p145C` | 142 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.143 A](messages/p146A.md) `p146A` | 143 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.144 A8](messages/p147A8.md) `p147A8` | 144 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.144 B](messages/p147B.md) `p147B` | 144 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.144 C1](messages/p147C1.md) `p147C1` | 144 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.145 A](messages/p148A.md) `p148A` | 145 | 6 November |  | Unsolved |  |  |
| [p.145 B](messages/p148B.md) `p148B` | 145 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.145 B.2](messages/p148B.2.md) `p148B.2` | 145 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.145 B.3](messages/p148B.3.md) `p148B.3` | 145 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.146 A1](messages/p149A1.md) `p149A1` | 146 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.146 B](messages/p149B.md) `p149B` | 146 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017 |
| [p.146 C1](messages/p149C1.md) `p149C1` | 146 | 6 November | nov04 | Solved, 10 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.147 A](messages/p150A.md) `p150A` | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.147 B1](messages/p150B1.md) `p150B1` | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.147 C1](messages/p150C1.md) `p150C1` | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.147 D1](messages/p150D1.md) `p150D1` | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.148 A1](messages/p151A1.md) `p151A1` | 148 | 6 November | nov04 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.148 B1](messages/p151B1.md) `p151B1` | 148 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.148 C1](messages/p151C1.md) `p151C1` | 148 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.149 A2](messages/p152A2.md) `p152A2` | 149 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.149 B](messages/p152B.md) `p152B` | 149 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.149 C](messages/p152C.md) `p152C` | 149 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.150 A2](messages/p153A2.md) `p153A2` | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.150 B1](messages/p153B1.md) `p153B1` | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.150 B2](messages/p153B2.md) `p153B2` | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.150 B3](messages/p153B3.md) `p153B3` | 150 | 6 November | nov04 | Solved, 13 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.150 B4](messages/p153B4.md) `p153B4` | 150 | 6 November |  | Unsolved |  |  |
| [p.150 B](messages/p153B.md) `p153B` | 150 | 6 November |  | Unsolved |  |  |
| [p.150 B5](messages/p153B5.md) `p153B5` | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.151 A1](messages/p154A1.md) `p154A1` | 151 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.151 A2](messages/p154A2.md) `p154A2` | 151 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.151 B](messages/p154B.md) `p154B` | 151 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.151 C](messages/p154C.md) `p154C` | 151 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.151 ?2](messages/p154_2.md) `p154_2` | 151 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.151 E2](messages/p154E2.md) `p154E2` | 151 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.152 A2](messages/p155A2.md) `p155A2` | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.152 B2](messages/p155B2.md) `p155B2` | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.152 GC](messages/p155GC.md) `p155GC` | 152 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.152 D](messages/p155D.md) `p155D` | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.152 E](messages/p155E.md) `p155E` | 152 | 7 November |  | Unsolved |  |  |
| [p.152 E2](messages/p155E2.md) `p155E2` | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.153 A3](messages/p156A3.md) `p156A3` | 153 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.153 B1](messages/p156B1.md) `p156B1` | 153 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.153 C3](messages/p156C3.md) `p156C3` | 153 | 7 November | ours_nov07_18col | Solved | This project, 2026 | This project, 2026 |
| [p.153 C6](messages/p156C6.md) `p156C6` | 153 | 7 November | ours_nov07_18col | Solved, 3 open | This project, 2026 | This project, 2026 |
| [p.153 D2](messages/p156D2.md) `p156D2` | 153 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.153 E1](messages/p156E1.md) `p156E1` | 153 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.154 A2](messages/p157A2.md) `p157A2` | 154 | 7 November |  | Unsolved |  |  |
| [p.154 B](messages/p157B.md) `p157B` | 154 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.155 A](messages/p158A.md) `p158A` | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.155 A2](messages/p158A2.md) `p158A2` | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.155 B](messages/p158B.md) `p158B` | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.155 C1](messages/p158C1.md) `p158C1` | 155 | 7 November | nov07 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.155 C3](messages/p158C3.md) `p158C3` | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.155 D](messages/p158D.md) `p158D` | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.156 A](messages/p159A.md) `p159A` | 156 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.156 B1](messages/p159B1.md) `p159B1` | 156 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.156 ?1](messages/p159_1.md) `p159_1` | 156 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.156 D](messages/p159D.md) `p159D` | 156 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.156 E1](messages/p159E1.md) `p159E1` | 156 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.157 A](messages/p160A.md) `p160A` | 157 | 7 November |  | Unsolved |  |  |
| [p.157 A.2](messages/p160A.2.md) `p160A.2` | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.157 A3](messages/p160A3.md) `p160A3` | 157 | 7 November | nov07 | Solved, 11 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.157 A4](messages/p160A4.md) `p160A4` | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.157 A5](messages/p160A5.md) `p160A5` | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.157 B](messages/p160B.md) `p160B` | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.157 B2](messages/p160B2.md) `p160B2` | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.158 A1](messages/p161A1.md) `p161A1` | 158 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.158 A2](messages/p161A2.md) `p161A2` | 158 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.158 B1](messages/p161B1.md) `p161B1` | 158 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.158 C3](messages/p161C3.md) `p161C3` | 158 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.158 D](messages/p161D.md) `p161D` | 158 | 8 November |  | Duplicate entry |  |  |
| [p.158 E](messages/p161E.md) `p161E` | 158 | 8 November |  | Unsolved |  |  |
| [p.159 A](messages/p162A.md) `p162A` | 159 | 8 November | nov07 | Solved, 19 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.159 B](messages/p162B.md) `p162B` | 159 | 8 November |  | Unsolved |  |  |
| [p.159 B.2](messages/p162B.2.md) `p162B.2` | 159 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.159 ?](messages/p162_.md) `p162_` | 159 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.160 A2](messages/p163A2.md) `p163A2` | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.160 B](messages/p163B.md) `p163B` | 160 | 8 November | nov07 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.160 B.2](messages/p163B.2.md) `p163B.2` | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.160 C](messages/p163C.md) `p163C` | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.160 C2](messages/p163C2.md) `p163C2` | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.160 D1](messages/p163D1.md) `p163D1` | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.161 ?2](messages/p164_2.md) `p164_2` | 161 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.161 B1](messages/p164B1.md) `p164B1` | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.161 ?](messages/p164_.md) `p164_` | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.161 ?2.2](messages/p164_2.2.md) `p164_2.2` | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.161 D1](messages/p164D1.md) `p164D1` | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.161 D3](messages/p164D3.md) `p164D3` | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.162 A1](messages/p165A1.md) `p165A1` | 162 | 8 November |  | Unsolved |  |  |
| [p.162 B1](messages/p165B1.md) `p165B1` | 162 | 8 November | nov07 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.162 C1](messages/p165C1.md) `p165C1` | 162 | 8 November |  | Unsolved |  |  |
| [p.162 C2](messages/p165C2.md) `p165C2` | 162 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.162 D1](messages/p165D1.md) `p165D1` | 162 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.163 A1](messages/p166A1.md) `p166A1` | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.163 A1.2](messages/p166A1.2.md) `p166A1.2` | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.163 A](messages/p166A.md) `p166A` | 163 | 9 November |  | Unsolved |  |  |
| [p.163 A.2](messages/p166A.2.md) `p166A.2` | 163 | 9 November |  | Unsolved |  |  |
| [p.163 A1.3](messages/p166A1.3.md) `p166A1.3` | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.163 A1.4](messages/p166A1.4.md) `p166A1.4` | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.164 A](messages/p167A.md) `p167A` | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| [p.164 A4](messages/p167A4.md) `p167A4` | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.164 A5](messages/p167A5.md) `p167A5` | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| [p.164 ?](messages/p167_.md) `p167_` | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.164 C1](messages/p167C1.md) `p167C1` | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.164 D](messages/p167D.md) `p167D` | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.165 A1](messages/p168A1.md) `p168A1` | 165 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.165 A](messages/p168A.md) `p168A` | 165 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.165 A.2](messages/p168A.2.md) `p168A.2` | 165 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.165 A5](messages/p168A5.md) `p168A5` | 165 | 9 November | nov07 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.166 A](messages/p169A.md) `p169A` | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.166 A2](messages/p169A2.md) `p169A2` | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.166 A3](messages/p169A3.md) `p169A3` | 166 | 9 November |  | Unsolved |  |  |
| [p.166 B](messages/p169B.md) `p169B` | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.166 B2](messages/p169B2.md) `p169B2` | 166 | 9 November |  | Unsolved |  |  |
| [p.166 C1](messages/p169C1.md) `p169C1` | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.166 C3](messages/p169C3.md) `p169C3` | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.167 A](messages/p170A.md) `p170A` | 167 | 9 November | nov07 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.167 B](messages/p170B.md) `p170B` | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.167 B3](messages/p170B3.md) `p170B3` | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.167 B3.2](messages/p170B3.2.md) `p170B3.2` | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.167 C1](messages/p170C1.md) `p170C1` | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.167 D](messages/p170D.md) `p170D` | 167 | 9 November |  | Unsolved |  |  |
| [p.167 E](messages/p170E.md) `p170E` | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.168 A](messages/p171A.md) `p171A` | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.168 B](messages/p171B.md) `p171B` | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.168 C](messages/p171C.md) `p171C` | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.168 D](messages/p171D.md) `p171D` | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.168 E](messages/p171E.md) `p171E` | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.169 A](messages/p172A.md) `p172A` | 169 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.169 B](messages/p172B.md) `p172B` | 169 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.170 A](messages/p173A.md) `p173A` | 170 | 9 November |  | Unsolved |  |  |
| [p.170 B](messages/p173B.md) `p173B` | 170 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.170 B.2](messages/p173B.2.md) `p173B.2` | 170 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.171 A1](messages/p174A1.md) `p174A1` | 171 | 9 November | nov07 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017, claimed |
| [p.171 A3](messages/p174A3.md) `p174A3` | 171 | 9 November |  | Unsolved |  |  |
| [p.171 A3.2](messages/p174A3.2.md) `p174A3.2` | 171 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.171 B1](messages/p174B1.md) `p174B1` | 171 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.171 B](messages/p174B.md) `p174B` | 171 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.171 C](messages/p174C.md) `p174C` | 171 | 9 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.172 A](messages/p175A.md) `p175A` | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.172 A.2](messages/p175A.2.md) `p175A.2` | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.172 C1](messages/p175C1.md) `p175C1` | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.172 C2](messages/p175C2.md) `p175C2` | 172 | 10 November |  | No cipher text |  |  |
| [p.172 C3](messages/p175C3.md) `p175C3` | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.172 D1](messages/p175D1.md) `p175D1` | 172 | 10 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.172 D8](messages/p175D8.md) `p175D8` | 172 | 10 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.172 E](messages/p175E.md) `p175E` | 172 | 10 November |  | Unsolved |  |  |
| [p.173 A1](messages/p176A1.md) `p176A1` | 173 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.173 A3](messages/p176A3.md) `p176A3` | 173 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.174 A1](messages/p177A1.md) `p177A1` | 174 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.174 A](messages/p177A.md) `p177A` | 174 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.174 A3](messages/p177A3.md) `p177A3` | 174 | 10 November |  | Unsolved |  |  |
| [p.174 B](messages/p177B.md) `p177B` | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.174 C](messages/p177C.md) `p177C` | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.174 D](messages/p177D.md) `p177D` | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.174 E](messages/p177E.md) `p177E` | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.175 A1](messages/p178A1.md) `p178A1` | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.175 A](messages/p178A.md) `p178A` | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.175 B2](messages/p178B2.md) `p178B2` | 175 | 10 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.175 C](messages/p178C.md) `p178C` | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.175 C2](messages/p178C2.md) `p178C2` | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.175 C3](messages/p178C3.md) `p178C3` | 175 | 10 November | nov10 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.176 A](messages/p179A.md) `p179A` | 176 | 10 November |  | Unsolved |  | Norbert, 2017, in part |
| [p.176 A3](messages/p179A3.md) `p179A3` | 176 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.176 A6](messages/p179A6.md) `p179A6` | 176 | 10 November |  | Unsolved |  |  |
| [p.176 B1](messages/p179B1.md) `p179B1` | 176 | 10 November | nov10 | Solved, 6 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.176 B](messages/p179B.md) `p179B` | 176 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.176 B3](messages/p179B3.md) `p179B3` | 176 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.177 A](messages/p180A.md) `p180A` | 177 | 11 November | nov10 | Solved, 8 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.177 B](messages/p180B.md) `p180B` | 177 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.177 B.2](messages/p180B.2.md) `p180B.2` | 177 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.177 B3](messages/p180B3.md) `p180B3` | 177 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.178 A](messages/p181A.md) `p181A` | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.178 A2](messages/p181A2.md) `p181A2` | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.178 A3](messages/p181A3.md) `p181A3` | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.178 A4](messages/p181A4.md) `p181A4` | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.178 A5](messages/p181A5.md) `p181A5` | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.179 A](messages/p182A.md) `p182A` | 179 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.179 B](messages/p182B.md) `p182B` | 179 | 11 November | nov10 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.179 C](messages/p182C.md) `p182C` | 179 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.179 D](messages/p182D.md) `p182D` | 179 | 11 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.179 D3](messages/p182D3.md) `p182D3` | 179 | 11 November |  | No cipher text |  |  |
| [p.179 D.2](messages/p182D.2.md) `p182D.2` | 179 | 11 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.180 A](messages/p183A.md) `p183A` | 180 | ? November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.180 B2](messages/p183B2.md) `p183B2` | 180 | ? November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.180 B](messages/p183B.md) `p183B` | 180 | ? November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.180 D1](messages/p183D1.md) `p183D1` | 180 | ? November | nov10 | Solved, 20 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.180 E](messages/p183E.md) `p183E` | 180 | ? November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.181 A](messages/p184A.md) `p184A` | 181 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.181 B](messages/p184B.md) `p184B` | 181 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.182 A](messages/p185A.md) `p185A` | 182 | 12 November |  | Unsolved |  |  |
| [p.182 B](messages/p185B.md) `p185B` | 182 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.182 C](messages/p185C.md) `p185C` | 182 | 12 November |  | Unsolved |  |  |
| [p.183 A](messages/p186A.md) `p186A` | 183 | 12 November | nov10 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.183 B](messages/p186B.md) `p186B` | 183 | 12 November | nov10 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.183 C](messages/p186C.md) `p186C` | 183 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.183 D](messages/p186D.md) `p186D` | 183 | 12 November |  | Unsolved |  |  |
| [p.183 E](messages/p186E.md) `p186E` | 183 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.183 F](messages/p186F.md) `p186F` | 183 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.184 ?](messages/p187_.md) `p187_` | 184 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.184 B](messages/p187B.md) `p187B` | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.184 B2](messages/p187B2.md) `p187B2` | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.184 B3](messages/p187B3.md) `p187B3` | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.184 C1](messages/p187C1.md) `p187C1` | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.184 C](messages/p187C.md) `p187C` | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.184 C3](messages/p187C3.md) `p187C3` | 184 | 13 November |  | Unsolved |  |  |
| [p.185 ?2](messages/p188_2.md) `p188_2` | 185 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.185 ?](messages/p188_.md) `p188_` | 185 | 13 November | nov13_20 | Solved, 32 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.185 ?.2](messages/p188_.2.md) `p188_.2` | 185 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.185 ?.3](messages/p188_.3.md) `p188_.3` | 185 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.186 A](messages/p189A.md) `p189A` | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.186 A2](messages/p189A2.md) `p189A2` | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.186 B1](messages/p189B1.md) `p189B1` | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.186 B3](messages/p189B3.md) `p189B3` | 186 | 13 November |  | Unsolved |  |  |
| [p.186 C1](messages/p189C1.md) `p189C1` | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.187 A1](messages/p190A1.md) `p190A1` | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| [p.187 A](messages/p190A.md) `p190A` | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| [p.187 B](messages/p190B.md) `p190B` | 187 | 13 November |  | Unsolved |  |  |
| [p.187 G](messages/p190G.md) `p190G` | 187 | 13 November |  | Unsolved |  |  |
| [p.187 D1](messages/p190D1.md) `p190D1` | 187 | 13 November | nov13_20 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.188 A](messages/p191A.md) `p191A` | 188 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.188 B2](messages/p191B2.md) `p191B2` | 188 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.188 ?1](messages/p191_1.md) `p191_1` | 188 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.189 A](messages/p192A.md) `p192A` | 189 | 14 November |  | Unsolved |  |  |
| [p.189 B](messages/p192B.md) `p192B` | 189 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.189 C](messages/p192C.md) `p192C` | 189 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.189 D](messages/p192D.md) `p192D` | 189 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.189 E](messages/p192E.md) `p192E` | 189 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.190 A](messages/p193A.md) `p193A` | 190 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.190 B](messages/p193B.md) `p193B` | 190 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.190 C](messages/p193C.md) `p193C` | 190 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.190 D](messages/p193D.md) `p193D` | 190 | 14 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.190 ?](messages/p193_.md) `p193_` | 190 | 14 November | nov13_20 | Solved, 10 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.191 A](messages/p194A.md) `p194A` | 191 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert and Max Baertl, 2017 |
| [p.191 A.2](messages/p194A.2.md) `p194A.2` | 191 | 14 November |  | Unsolved |  |  |
| [p.192 A2](messages/p195A2.md) `p195A2` | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.192 A](messages/p195A.md) `p195A` | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.192 A.2](messages/p195A.2.md) `p195A.2` | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.192 ?](messages/p195_.md) `p195_` | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.193 A](messages/p196A.md) `p196A` | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.193 B](messages/p196B.md) `p196B` | 193 | 14 November |  | Unsolved |  |  |
| [p.193 C](messages/p196C.md) `p196C` | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.193 D](messages/p196D.md) `p196D` | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.193 E](messages/p196E.md) `p196E` | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.193 F](messages/p196F.md) `p196F` | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.194 A](messages/p197A.md) `p197A` | 194 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.194 B](messages/p197B.md) `p197B` | 194 | 14 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.194 C](messages/p197C.md) `p197C` | 194 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.194 D1](messages/p197D1.md) `p197D1` | 194 | 15 November |  | Unsolved |  |  |
| [p.194 E](messages/p197E.md) `p197E` | 194 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.195 A2](messages/p198A2.md) `p198A2` | 195 | 15 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.196 A](messages/p199A.md) `p199A` | 196 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.196 B](messages/p199B.md) `p199B` | 196 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.197 A1](messages/p200A1.md) `p200A1` | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.197 A3](messages/p200A3.md) `p200A3` | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.197 B](messages/p200B.md) `p200B` | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.197 C](messages/p200C.md) `p200C` | 197 | 15 November |  | Unsolved |  |  |
| [p.197 D](messages/p200D.md) `p200D` | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.197 E](messages/p200E.md) `p200E` | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.198 A](messages/p201A.md) `p201A` | 198 | 15 November |  | Unsolved |  |  |
| [p.198 B](messages/p201B.md) `p201B` | 198 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.198 C](messages/p201C.md) `p201C` | 198 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.198 D](messages/p201D.md) `p201D` | 198 | 15 November |  | Unsolved |  |  |
| [p.198 E](messages/p201E.md) `p201E` | 198 | 15 November |  | Unsolved |  |  |
| [p.199 A1](messages/p202A1.md) `p202A1` | 199 | 15 November | nov13_16 | Solved, 32 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.199 A3](messages/p202A3.md) `p202A3` | 199 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.199 A](messages/p202A.md) `p202A` | 199 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.199 ?](messages/p202_.md) `p202_` | 199 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.200 A](messages/p203A.md) `p203A` | 200 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.200 B1](messages/p203B1.md) `p203B1` | 200 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.200 B3](messages/p203B3.md) `p203B3` | 200 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.201 A1](messages/p204A1.md) `p204A1` | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.201 A2](messages/p204A2.md) `p204A2` | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.201 B](messages/p204B.md) `p204B` | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.201 B2](messages/p204B2.md) `p204B2` | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.201 C](messages/p204C.md) `p204C` | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.202 A1](messages/p205A1.md) `p205A1` | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.202 A2](messages/p205A2.md) `p205A2` | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.202 B](messages/p205B.md) `p205B` | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.202 B2](messages/p205B2.md) `p205B2` | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.202 B3](messages/p205B3.md) `p205B3` | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.202 B4](messages/p205B4.md) `p205B4` | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.203 A2](messages/p206A2.md) `p206A2` | 203 | 16 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.203 ?](messages/p206_.md) `p206_` | 203 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.203 ?.2](messages/p206_.2.md) `p206_.2` | 203 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.204 A](messages/p207A.md) `p207A` | 204 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.204 B](messages/p207B.md) `p207B` | 204 | 17 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.204 ?](messages/p207_.md) `p207_` | 204 | 17 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.204 ?2](messages/p207_2.md) `p207_2` | 204 | 17 November |  | Unsolved |  |  |
| [p.204 D](messages/p207D.md) `p207D` | 204 | 17 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.205 A4](messages/p208A4.md) `p208A4` | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.205 A2](messages/p208A2.md) `p208A2` | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.205 A3](messages/p208A3.md) `p208A3` | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.205 A4.2](messages/p208A4.2.md) `p208A4.2` | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.205 B](messages/p208B.md) `p208B` | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.205 B8](messages/p208B8.md) `p208B8` | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.206 A](messages/p209A.md) `p209A` | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.206 A.2](messages/p209A.2.md) `p209A.2` | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.206 A3](messages/p209A3.md) `p209A3` | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.206 B](messages/p209B.md) `p209B` | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.206 B.2](messages/p209B.2.md) `p209B.2` | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.207 A](messages/p210A.md) `p210A` | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.207 A.2](messages/p210A.2.md) `p210A.2` | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.207 B](messages/p210B.md) `p210B` | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.207 C1](messages/p210C1.md) `p210C1` | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.207 C](messages/p210C.md) `p210C` | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.208 A](messages/p211A.md) `p211A` | 208 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.208 A.2](messages/p211A.2.md) `p211A.2` | 208 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.209 A1](messages/p212A1.md) `p212A1` | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.209 B](messages/p212B.md) `p212B` | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.209 B2](messages/p212B2.md) `p212B2` | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.209 C1](messages/p212C1.md) `p212C1` | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.209 C](messages/p212C.md) `p212C` | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.210 A1](messages/p213A1.md) `p213A1` | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.210 A](messages/p213A.md) `p213A` | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.210 B](messages/p213B.md) `p213B` | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.210 C](messages/p213C.md) `p213C` | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.210 D](messages/p213D.md) `p213D` | 210 | 20 November |  | Unsolved |  |  |
| [p.211 A](messages/p214A.md) `p214A` | 211 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.211 B](messages/p214B.md) `p214B` | 211 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.211 B1](messages/p214B1.md) `p214B1` | 211 | 19 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.211 B2](messages/p214B2.md) `p214B2` | 211 | 19 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.211 B.2](messages/p214B.2.md) `p214B.2` | 211 | 19 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.212 A](messages/p215A.md) `p215A` | 212 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.212 A2](messages/p215A2.md) `p215A2` | 212 | 22 November |  | Unsolved |  |  |
| [p.212 A.2](messages/p215A.2.md) `p215A.2` | 212 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.212 A.3](messages/p215A.3.md) `p215A.3` | 212 | 22 November |  | Unsolved |  |  |
| [p.212 A.4](messages/p215A.4.md) `p215A.4` | 212 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.213 A6](messages/p216A6.md) `p216A6` | 213 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.213 A7](messages/p216A7.md) `p216A7` | 213 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.213 ?1](messages/p216_1.md) `p216_1` | 213 | 23 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.213 ?2](messages/p216_2.md) `p216_2` | 213 | 23 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.213 ?3](messages/p216_3.md) `p216_3` | 213 | 23 November | nov22 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.214 A1](messages/p217A1.md) `p217A1` | 214 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.214 B](messages/p217B.md) `p217B` | 214 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.214 C](messages/p217C.md) `p217C` | 214 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.215 A](messages/p218A.md) `p218A` | 215 | 22 November |  | Unsolved |  |  |
| [p.215 B1](messages/p218B1.md) `p218B1` | 215 | 22 November |  | Unsolved |  |  |
| [p.215 B4](messages/p218B4.md) `p218B4` | 215 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.215 B3](messages/p218B3.md) `p218B3` | 215 | 22 November |  | Unsolved |  |  |
| [p.215 C](messages/p218C.md) `p218C` | 215 | 22 November |  | Unsolved |  | Norbert and Max Baertl, 2017, in part |
| [p.216 A1](messages/p219A1.md) `p219A1` | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.216 A](messages/p219A.md) `p219A` | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.216 A.2](messages/p219A.2.md) `p219A.2` | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.216 A4](messages/p219A4.md) `p219A4` | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.216 B1](messages/p219B1.md) `p219B1` | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.216 B](messages/p219B.md) `p219B` | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.217 A](messages/p220A.md) `p220A` | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.217 A.2](messages/p220A.2.md) `p220A.2` | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.217 A3](messages/p220A3.md) `p220A3` | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.217 A4](messages/p220A4.md) `p220A4` | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.217 A.3](messages/p220A.3.md) `p220A.3` | 217 | 24 November | nov22 | Solved, 14 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.217 B](messages/p220B.md) `p220B` | 217 | 24 November |  | Unsolved |  |  |
| [p.217 B2](messages/p220B2.md) `p220B2` | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.217 C](messages/p220C.md) `p220C` | 217 | 24 November |  | Unsolved |  |  |
| [p.217 C.2](messages/p220C.2.md) `p220C.2` | 217 | 24 November | dec09_history | Solved | Childs, 1919 | Prinz, 2026 |
| [p.218 A](messages/p221A.md) `p221A` | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.218 A2](messages/p221A2.md) `p221A2` | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.218 A6](messages/p221A6.md) `p221A6` | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.218 B2](messages/p221B2.md) `p221B2` | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.218 B3](messages/p221B3.md) `p221B3` | 218 | 25 November | nov25 | Solved, 4 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.219 A1](messages/p222A1.md) `p222A1` | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.219 A2](messages/p222A2.md) `p222A2` | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.219 B](messages/p222B.md) `p222B` | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.219 C](messages/p222C.md) `p222C` | 219 | 25 November |  | Unsolved |  |  |
| [p.219 D1](messages/p222D1.md) `p222D1` | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.220 A2](messages/p223A2.md) `p223A2` | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.220 B](messages/p223B.md) `p223B` | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.220 C1](messages/p223C1.md) `p223C1` | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.220 C2](messages/p223C2.md) `p223C2` | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.220 C3](messages/p223C3.md) `p223C3` | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.220 C4](messages/p223C4.md) `p223C4` | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.221 A5](messages/p224A5.md) `p224A5` | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.221 A6](messages/p224A6.md) `p224A6` | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.221 B1](messages/p224B1.md) `p224B1` | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.221 B2](messages/p224B2.md) `p224B2` | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.221 B](messages/p224B.md) `p224B` | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.221 B4](messages/p224B4.md) `p224B4` | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.222 A](messages/p225A.md) `p225A` | 222 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.222 A2](messages/p225A2.md) `p225A2` | 222 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.223 A1](messages/p226A1.md) `p226A1` | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.223 A](messages/p226A.md) `p226A` | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.223 A3](messages/p226A3.md) `p226A3` | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.223 B](messages/p226B.md) `p226B` | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.223 B.2](messages/p226B.2.md) `p226B.2` | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.224 A1](messages/p227A1.md) `p227A1` | 224 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.224 A2](messages/p227A2.md) `p227A2` | 224 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.224 B](messages/p227B.md) `p227B` | 224 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.224 C1](messages/p227C1.md) `p227C1` | 224 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.224 C2](messages/p227C2.md) `p227C2` | 224 | 26 November | nov25 | Solved, 12 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.225 A](messages/p228A.md) `p228A` | 225 | 28 November | nov28 | Solved, 6 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.225 B1](messages/p228B1.md) `p228B1` | 225 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.225 B](messages/p228B.md) `p228B` | 225 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.226 A2](messages/p229A2.md) `p229A2` | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.226 B2](messages/p229B2.md) `p229B2` | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.226 B1](messages/p229B1.md) `p229B1` | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.226 B2.2](messages/p229B2.2.md) `p229B2.2` | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.226 B](messages/p229B.md) `p229B` | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.227 A4](messages/p230A4.md) `p230A4` | 227 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.227 B](messages/p230B.md) `p230B` | 227 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.227 D](messages/p230D.md) `p230D` | 227 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.228 A](messages/p231A.md) `p231A` | 228 | 30 November | nov28 | Solved, 52 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p.228 B1](messages/p231B1.md) `p231B1` | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.228 B2](messages/p231B2.md) `p231B2` | 228 | 30 November |  | Unsolved |  |  |
| [p.228 B3](messages/p231B3.md) `p231B3` | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.228 C1](messages/p231C1.md) `p231C1` | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.228 C2](messages/p231C2.md) `p231C2` | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.229 A1](messages/p232A1.md) `p232A1` | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.229 A](messages/p232A.md) `p232A` | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.229 A3](messages/p232A3.md) `p232A3` | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.229 B](messages/p232B.md) `p232B` | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.229 B2](messages/p232B2.md) `p232B2` | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.229 ?](messages/p232_.md) `p232_` | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.230 A3](messages/p233A3.md) `p233A3` | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.230 A4](messages/p233A4.md) `p233A4` | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.230 B](messages/p233B.md) `p233B` | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.230 C](messages/p233C.md) `p233C` | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.230 D](messages/p233D.md) `p233D` | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p.230 D.2](messages/p233D.2.md) `p233D.2` | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |

## The 22 entries on Schmeh's list

Klaus Schmeh's list of unsolved ADFGVX messages has 22 entries. Each was matched to an entry of the log by its opening groups. Entry 10 turned out to be a log row that joins two other messages. A solution of entries 18 and 19 under a new key was published in the comments on Schmeh's post in May 2017, by George Lasry and Norbert.

| Schmeh | Entry | Page | Date | Key | Status | Key found by | Solution published by |
|---|---|---|---|---|---|---|---|
| 1 | [p.73 A](messages/p076A.md) `p076A` | 73 | 26 October |  | Unsolved |  |  |
| 2 | [p.100 A](messages/p103A.md) `p103A` | 100 | 1 November | nov01 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | Armin, 2017, claimed |
| 3 | [p.105 BB](messages/p108BB.md) `p108BB` | 105 | 2 November | nov01 | Solved, 5 open | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert and Max Baertl, 2017 |
| 4 | [p.109 D](messages/p112D.md) `p112D` | 109 | 3 November |  | Unsolved |  | Norbert, 2017, in part |
| 5 | [p.132 B](messages/p135B.md) `p135B` | 132 | 5 November | nov04 | Solved, 23 open | Lasry, Niebel, Kopal and Wacker, 2017 | Thomas and Norbert, 2017, in part |
| 6 | [p.146 B](messages/p149B.md) `p149B` | 146 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017 |
| 7 | [p.152 E](messages/p155E.md) `p155E` | 152 | 7 November |  | Unsolved |  |  |
| 8 and 9 | [p.153 C3](messages/p156C3.md) `p156C3` | 153 | 7 November | ours_nov07_18col | Solved | This project, 2026 | This project, 2026 |
| 8 and 9 | [p.153 C6](messages/p156C6.md) `p156C6` | 153 | 7 November | ours_nov07_18col | Solved, 3 open | This project, 2026 | This project, 2026 |
| 10 | [p.158 D](messages/p161D.md) `p161D` | 158 | 8 November |  | Duplicate entry |  |  |
| 11 and 12 | [p.164 A](messages/p167A.md) `p167A` | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| 11 and 12 | [p.164 A5](messages/p167A5.md) `p167A5` | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| 13 | [p.170 A](messages/p173A.md) `p173A` | 170 | 9 November |  | Unsolved |  |  |
| 14 | [p.171 A1](messages/p174A1.md) `p174A1` | 171 | 9 November | nov07 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017, claimed |
| 15 | [p.176 A](messages/p179A.md) `p179A` | 176 | 10 November |  | Unsolved |  | Norbert, 2017, in part |
| 16 | [p.176 B1](messages/p179B1.md) `p179B1` | 176 | 10 November | nov10 | Solved, 6 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| 17 | [p.215 C](messages/p218C.md) `p218C` | 215 | 22 November |  | Unsolved |  | Norbert and Max Baertl, 2017, in part |
| 18 and 19 | [p.187 A1](messages/p190A1.md) `p190A1` | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| 18 and 19 | [p.187 A](messages/p190A.md) `p190A` | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| 20 | [p.189 A](messages/p192A.md) `p192A` | 189 | 14 November |  | Unsolved |  |  |
| 21 | [p.198 D](messages/p201D.md) `p201D` | 198 | 15 November |  | Unsolved |  |  |
| 22 | [p.217 C.2](messages/p220C.2.md) `p220C.2` | 217 | 24 November | dec09_history | Solved | Childs, 1919 | Prinz, 2026 |
