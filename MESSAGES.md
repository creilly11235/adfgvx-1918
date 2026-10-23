# Every message in Childs's log

One row per log entry, in log order. The columns are the entry id, Childs's printed page, the date, the key, the status, who found the key and who published a solution.
Each entry id links to its page under `messages`, which follows the message from the printed page to the English translation and carries the detail behind the status.

## Where the entries stand

Every entry is in exactly one row.

| Status | Entries | No published solution found | Meaning |
|---|---|---|---|
| Solved | 550 | 542 | every surviving symbol decrypts under the key and the text reads as German, as transcribed or after a length repair |
| Solved with open letters | 42 | 0 | the whole message reads, with the letters that a reader filled or left open marked in the text |
| Partially solved | 2 | 0 | part of the message reads and the rest is undetermined |
| Unsolved | 87 |  | no solution is published here, and the last column names a solution published elsewhere where we found one |
| No cipher text | 6 |  | the log prints no cipher block for the entry, or only a header that quotes a few symbols of another entry's block |
| Duplicate entry | 1 |  | the log row joins the symbols of two other entries |
| Total | 688 | 542 | |

The third column counts the solved entries for which our search of the 2017 paper and thesis, the comments on Schmeh's posts and the web found no published solution. It records the outcome of that search and nothing more. The 2017 paper reports 618 of 668 cryptograms recovered and gives no list by entry, and the log is split into 688 entries here, so the two totals cannot be matched one to one. Leads and partial repairs that have not passed the project's gate are not published here, so an unsolved row says only that no solution is published.

## How to read a message page

Every entry has a page under `messages`, named by the entry id, for example `messages/p156C3.md`. The first line of a page gives the page in Childs, the date, the key, the status, who found the key and who published a solution, and the second line the detail behind the status. Then come six steps.

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
| [p059A](messages/p059A.md) | 56 | 19 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p059B](messages/p059B.md) | 56 | 19 September | sep19 | Solved, 3 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p059B.2](messages/p059B.2.md) | 56 | 19 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p060A1](messages/p060A1.md) | 57 | 20 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p060A2](messages/p060A2.md) | 57 | 20 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p060A3](messages/p060A3.md) | 57 | 20 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p061_](messages/p061_.md) | 58 | 21 September |  | No cipher text |  |  |
| [p061_.2](messages/p061_.2.md) | 58 | 21 September |  | No cipher text |  |  |
| [p061_.3](messages/p061_.3.md) | 58 | 21 September |  | No cipher text |  |  |
| [p061B](messages/p061B.md) | 58 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p062A](messages/p062A.md) | 59 | 21 September |  | Unsolved |  |  |
| [p062A2](messages/p062A2.md) | 59 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p062A3](messages/p062A3.md) | 59 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p062B](messages/p062B.md) | 59 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p063A1](messages/p063A1.md) | 60 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p063A2](messages/p063A2.md) | 60 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p063B2](messages/p063B2.md) | 60 | 21 September |  | No cipher text |  |  |
| [p063B](messages/p063B.md) | 60 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p064A](messages/p064A.md) | 61 | 21 September | sep19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p065A](messages/p065A.md) | 62 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p065B](messages/p065B.md) | 62 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p066A](messages/p066A.md) | 63 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p067A](messages/p067A.md) | 64 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p067A2](messages/p067A2.md) | 64 | 4 October | oct04 | Solved, 23 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p0674](messages/p0674.md) | 64 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p068A](messages/p068A.md) | 65 | 4 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p069A](messages/p069A.md) | 66 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p069B](messages/p069B.md) | 66 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p069B1](messages/p069B1.md) | 66 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p070A3](messages/p070A3.md) | 67 | 5 October | oct04 | Solved, 27 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p070B](messages/p070B.md) | 67 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p070C](messages/p070C.md) | 67 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p071A1](messages/p071A1.md) | 68 | 5 October |  | Unsolved |  |  |
| [p071A2](messages/p071A2.md) | 68 | 5 October |  | Unsolved |  |  |
| [p072A](messages/p072A.md) | 69 | 5 October |  | Unsolved |  |  |
| [p072B1](messages/p072B1.md) | 69 | 5 October |  | Unsolved |  |  |
| [p072B3](messages/p072B3.md) | 69 | 5 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p073A1](messages/p073A1.md) | 70 | 6 October | oct04 | Solved, 20 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p073A2](messages/p073A2.md) | 70 | 6 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p073B](messages/p073B.md) | 70 | 6 October |  | Unsolved |  |  |
| [p074A](messages/p074A.md) | 71 | 6 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p074A.2](messages/p074A.2.md) | 71 | 6 October |  | Unsolved |  |  |
| [p075A1](messages/p075A1.md) | 72 | 6 October | oct04 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p075A2](messages/p075A2.md) | 72 | 6 October |  | Unsolved |  |  |
| [p075A3](messages/p075A3.md) | 72 | 6 October | oct04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p075B](messages/p075B.md) | 72 | 6 October | oct04 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p076A](messages/p076A.md) | 73 | 26 October |  | Unsolved |  |  |
| [p077A](messages/p077A.md) | 74 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p077B](messages/p077B.md) | 74 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p077C](messages/p077C.md) | 74 | 28 October | oct28 | Solved, 30 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p077C2](messages/p077C2.md) | 74 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p078A](messages/p078A.md) | 75 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p078B](messages/p078B.md) | 75 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p078B.2](messages/p078B.2.md) | 75 | 28 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p07943](messages/p07943.md) | 76 | 28 October | oct28 | Solved, 3 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p080A](messages/p080A.md) | 77 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p080B](messages/p080B.md) | 77 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p081A](messages/p081A.md) | 78 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p081A2](messages/p081A2.md) | 78 | 29 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p082A1](messages/p082A1.md) | 79 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p082A2](messages/p082A2.md) | 79 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p083A](messages/p083A.md) | 80 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p083B1](messages/p083B1.md) | 80 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p083B2](messages/p083B2.md) | 80 | 30 October |  | Unsolved |  |  |
| [p083B](messages/p083B.md) | 80 | 30 October |  | Unsolved |  |  |
| [p084A](messages/p084A.md) | 81 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p084B](messages/p084B.md) | 81 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p084C](messages/p084C.md) | 81 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p085A1](messages/p085A1.md) | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p085A2](messages/p085A2.md) | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p085A3](messages/p085A3.md) | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p085A](messages/p085A.md) | 82 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p086A](messages/p086A.md) | 83 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p086B2](messages/p086B2.md) | 83 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p087A](messages/p087A.md) | 84 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p087B](messages/p087B.md) | 84 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p087C](messages/p087C.md) | 84 | 30 October |  | Unsolved |  |  |
| [p088A](messages/p088A.md) | 85 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p088B](messages/p088B.md) | 85 | 30 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p089A](messages/p089A.md) | 86 | 31 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p089B2](messages/p089B2.md) | 86 | 31 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p089C1](messages/p089C1.md) | 86 | 31 October | oct28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p090A1](messages/p090A1.md) | 87 | 31 October | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p091A1](messages/p091A1.md) | 88 | 1 November | nov01 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p091A3](messages/p091A3.md) | 88 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p091B](messages/p091B.md) | 88 | 1 November | nov01 | Solved, 4 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p091C1](messages/p091C1.md) | 88 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p0924](messages/p0924.md) | 89 | 1 November |  | Unsolved |  |  |
| [p09244](messages/p09244.md) | 89 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p09345](messages/p09345.md) | 90 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p093B1](messages/p093B1.md) | 90 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p094_2](messages/p094_2.md) | 91 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p094_3](messages/p094_3.md) | 91 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p095A](messages/p095A.md) | 92 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p095B1](messages/p095B1.md) | 92 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p096A2](messages/p096A2.md) | 93 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p096A](messages/p096A.md) | 93 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p096A4](messages/p096A4.md) | 93 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p097A5](messages/p097A5.md) | 94 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p097A6](messages/p097A6.md) | 94 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p098A](messages/p098A.md) | 95 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p098A2](messages/p098A2.md) | 95 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p099A](messages/p099A.md) | 96 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p099B](messages/p099B.md) | 96 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p1004](messages/p1004.md) | 97 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p100B](messages/p100B.md) | 97 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p100C](messages/p100C.md) | 97 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p101A](messages/p101A.md) | 98 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p101A2](messages/p101A2.md) | 98 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p101B2](messages/p101B2.md) | 98 | 1 November |  | Unsolved |  |  |
| [p101B](messages/p101B.md) | 98 | 1 November |  | Unsolved |  |  |
| [p102A](messages/p102A.md) | 99 | 1 November |  | Unsolved |  |  |
| [p102B](messages/p102B.md) | 99 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p102C](messages/p102C.md) | 99 | 1 November |  | Unsolved |  |  |
| [p102C3](messages/p102C3.md) | 99 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p102D](messages/p102D.md) | 99 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p103A](messages/p103A.md) | 100 | 1 November | nov01 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | Armin, 2017, claimed |
| [p103B](messages/p103B.md) | 100 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p103C](messages/p103C.md) | 100 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p103D1](messages/p103D1.md) | 100 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p104A2](messages/p104A2.md) | 101 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p104B2](messages/p104B2.md) | 101 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p104_1](messages/p104_1.md) | 101 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p104D2](messages/p104D2.md) | 101 | 1 November |  | Unsolved |  |  |
| [p105D](messages/p105D.md) | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p105B1](messages/p105B1.md) | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p105B2](messages/p105B2.md) | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p105B3](messages/p105B3.md) | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p105C](messages/p105C.md) | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p105D.2](messages/p105D.2.md) | 102 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p106A](messages/p106A.md) | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p106B1](messages/p106B1.md) | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p106B](messages/p106B.md) | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p106C](messages/p106C.md) | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p106D](messages/p106D.md) | 103 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p107A3](messages/p107A3.md) | 104 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p107B](messages/p107B.md) | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p107C](messages/p107C.md) | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p107C2](messages/p107C2.md) | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p107D](messages/p107D.md) | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p107E3](messages/p107E3.md) | 104 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p108A](messages/p108A.md) | 105 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p108BB](messages/p108BB.md) | 105 | 2 November | nov01 | Solved, 5 open | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert and Max Baertl, 2017 |
| [p108C](messages/p108C.md) | 105 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p109A](messages/p109A.md) | 106 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p109A3](messages/p109A3.md) | 106 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p109B](messages/p109B.md) | 106 | 1 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p110A](messages/p110A.md) | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p110B1](messages/p110B1.md) | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p110B2](messages/p110B2.md) | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p110C](messages/p110C.md) | 107 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p110D](messages/p110D.md) | 107 | 2 November |  | Unsolved |  |  |
| [p111A](messages/p111A.md) | 108 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p111B2](messages/p111B2.md) | 108 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p111B2.2](messages/p111B2.2.md) | 108 | 2 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p112A2](messages/p112A2.md) | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p112A3](messages/p112A3.md) | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p112B](messages/p112B.md) | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p112C1](messages/p112C1.md) | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p112C](messages/p112C.md) | 109 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p112D](messages/p112D.md) | 109 | 3 November |  | Unsolved |  | Norbert, 2017, in part |
| [p113A](messages/p113A.md) | 110 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p113B](messages/p113B.md) | 110 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p113C](messages/p113C.md) | 110 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p114A](messages/p114A.md) | 111 | 3 November |  | Unsolved |  |  |
| [p114B](messages/p114B.md) | 111 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p115A1](messages/p115A1.md) | 112 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p115A2](messages/p115A2.md) | 112 | 3 November | nov01 | Solved, 20 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p115A2.2](messages/p115A2.2.md) | 112 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p115B](messages/p115B.md) | 112 | 3 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p1154](messages/p1154.md) | 112 | 4 November |  | Unsolved |  |  |
| [p115D](messages/p115D.md) | 112 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p116A](messages/p116A.md) | 113 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p116B9](messages/p116B9.md) | 113 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p116C](messages/p116C.md) | 113 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p116D1](messages/p116D1.md) | 113 | 3 November | nov01 | Solved, 5 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p117A1](messages/p117A1.md) | 114 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p117A4](messages/p117A4.md) | 114 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p118A5](messages/p118A5.md) | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p118A6](messages/p118A6.md) | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p118A7](messages/p118A7.md) | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p118A8](messages/p118A8.md) | 115 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p119A](messages/p119A.md) | 116 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p119A.2](messages/p119A.2.md) | 116 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p119A.3](messages/p119A.3.md) | 116 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p119A1](messages/p119A1.md) | 116 | 3 November |  | Unsolved |  |  |
| [p120A](messages/p120A.md) | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p120B](messages/p120B.md) | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p120C3](messages/p120C3.md) | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p120C4](messages/p120C4.md) | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p120D](messages/p120D.md) | 117 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p121A](messages/p121A.md) | 118 | 3 November | nov01 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p122A](messages/p122A.md) | 119 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p123A](messages/p123A.md) | 120 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p123B1](messages/p123B1.md) | 120 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p123C](messages/p123C.md) | 120 | 4 November |  | Unsolved |  |  |
| [p124A1](messages/p124A1.md) | 121 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p124A2](messages/p124A2.md) | 121 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p124B1](messages/p124B1.md) | 121 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p125A2](messages/p125A2.md) | 122 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p125B](messages/p125B.md) | 122 | 4 November |  | Unsolved |  |  |
| [p125C](messages/p125C.md) | 122 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p125D1](messages/p125D1.md) | 122 | 4 November |  | Unsolved |  |  |
| [p126A2](messages/p126A2.md) | 123 | 4 November | nov04 | Solved, 18 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p126A3](messages/p126A3.md) | 123 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p126B](messages/p126B.md) | 123 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p127B1](messages/p127B1.md) | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p127B2](messages/p127B2.md) | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p127B3](messages/p127B3.md) | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p127B](messages/p127B.md) | 124 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p128A1](messages/p128A1.md) | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p128A2](messages/p128A2.md) | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p128A3](messages/p128A3.md) | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p128A4](messages/p128A4.md) | 125 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p129A5](messages/p129A5.md) | 126 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p129A6](messages/p129A6.md) | 126 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p129B](messages/p129B.md) | 126 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p130A3](messages/p130A3.md) | 127 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p130B1](messages/p130B1.md) | 127 | 4 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p130B2](messages/p130B2.md) | 127 | 4 November |  | Unsolved |  |  |
| [p131A1](messages/p131A1.md) | 128 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p131A2](messages/p131A2.md) | 128 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p131B1](messages/p131B1.md) | 128 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p132A7](messages/p132A7.md) | 129 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p132A8](messages/p132A8.md) | 129 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p132B1](messages/p132B1.md) | 129 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p133A1](messages/p133A1.md) | 130 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p133A2](messages/p133A2.md) | 130 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p134A3](messages/p134A3.md) | 131 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p134A4](messages/p134A4.md) | 131 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p134B](messages/p134B.md) | 131 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p135_](messages/p135_.md) | 132 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p135B](messages/p135B.md) | 132 | 5 November |  | Unsolved |  | Thomas and Norbert, 2017, in part |
| [p135C](messages/p135C.md) | 132 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p136A2](messages/p136A2.md) | 133 | 5 November | nov04 | Solved, 1 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p136A3](messages/p136A3.md) | 133 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p137A4](messages/p137A4.md) | 134 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p137B](messages/p137B.md) | 134 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p138A](messages/p138A.md) | 135 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p139A1](messages/p139A1.md) | 136 | 5 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p139A2](messages/p139A2.md) | 136 | 5 November |  | Unsolved |  |  |
| [p139B](messages/p139B.md) | 136 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p139B3](messages/p139B3.md) | 136 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p140A4](messages/p140A4.md) | 137 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p140A5](messages/p140A5.md) | 137 | 6 November |  | Unsolved |  |  |
| [p140A6](messages/p140A6.md) | 137 | 6 November |  | Unsolved |  |  |
| [p140B](messages/p140B.md) | 137 | 6 November |  | Unsolved |  |  |
| [p140B4](messages/p140B4.md) | 137 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p140B.2](messages/p140B.2.md) | 137 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p140B.3](messages/p140B.3.md) | 137 | 6 November | nov04 | Solved, 13 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p141A](messages/p141A.md) | 138 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p141A.2](messages/p141A.2.md) | 138 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p141B](messages/p141B.md) | 138 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p141B.2](messages/p141B.2.md) | 138 | 6 November |  | Unsolved |  |  |
| [p142A1](messages/p142A1.md) | 139 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p142A2](messages/p142A2.md) | 139 | 6 November |  | Unsolved |  |  |
| [p142A](messages/p142A.md) | 139 | 6 November |  | Unsolved |  |  |
| [p142A.2](messages/p142A.2.md) | 139 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p143_1](messages/p143_1.md) | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p143_2](messages/p143_2.md) | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p143_3](messages/p143_3.md) | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p143_4](messages/p143_4.md) | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p143B](messages/p143B.md) | 140 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p144A1](messages/p144A1.md) | 141 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p144A2](messages/p144A2.md) | 141 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p144B](messages/p144B.md) | 141 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p145A](messages/p145A.md) | 142 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p145B](messages/p145B.md) | 142 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p145C](messages/p145C.md) | 142 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p146A](messages/p146A.md) | 143 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p147A8](messages/p147A8.md) | 144 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p147B](messages/p147B.md) | 144 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p147C1](messages/p147C1.md) | 144 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p148A](messages/p148A.md) | 145 | 6 November |  | Unsolved |  |  |
| [p148B](messages/p148B.md) | 145 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p148B.2](messages/p148B.2.md) | 145 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p148B.3](messages/p148B.3.md) | 145 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p149A1](messages/p149A1.md) | 146 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p149B](messages/p149B.md) | 146 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017 |
| [p149C1](messages/p149C1.md) | 146 | 6 November | nov04 | Solved, 10 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p150A](messages/p150A.md) | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p150B1](messages/p150B1.md) | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p150C1](messages/p150C1.md) | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p150D1](messages/p150D1.md) | 147 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p151A1](messages/p151A1.md) | 148 | 6 November | nov04 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p151B1](messages/p151B1.md) | 148 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p151C1](messages/p151C1.md) | 148 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p152A2](messages/p152A2.md) | 149 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p152B](messages/p152B.md) | 149 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p152C](messages/p152C.md) | 149 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p153A2](messages/p153A2.md) | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p153B1](messages/p153B1.md) | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p153B2](messages/p153B2.md) | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p153B3](messages/p153B3.md) | 150 | 6 November | nov04 | Solved, 13 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p153B4](messages/p153B4.md) | 150 | 6 November |  | Unsolved |  |  |
| [p153B](messages/p153B.md) | 150 | 6 November |  | Unsolved |  |  |
| [p153B5](messages/p153B5.md) | 150 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p154A1](messages/p154A1.md) | 151 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p154A2](messages/p154A2.md) | 151 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p154B](messages/p154B.md) | 151 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p154C](messages/p154C.md) | 151 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p154_2](messages/p154_2.md) | 151 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p154E2](messages/p154E2.md) | 151 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p155A2](messages/p155A2.md) | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p155B2](messages/p155B2.md) | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p155GC](messages/p155GC.md) | 152 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p155D](messages/p155D.md) | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p155E](messages/p155E.md) | 152 | 7 November |  | Unsolved |  |  |
| [p155E2](messages/p155E2.md) | 152 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p156A3](messages/p156A3.md) | 153 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p156B1](messages/p156B1.md) | 153 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p156C3](messages/p156C3.md) | 153 | 7 November | ours_nov07_18col | Solved | This project, 2026 | This project, 2026 |
| [p156C6](messages/p156C6.md) | 153 | 7 November | ours_nov07_18col | Solved, 3 open | This project, 2026 | This project, 2026 |
| [p156D2](messages/p156D2.md) | 153 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p156E1](messages/p156E1.md) | 153 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p157A2](messages/p157A2.md) | 154 | 7 November |  | Unsolved |  |  |
| [p157B](messages/p157B.md) | 154 | 7 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p158A](messages/p158A.md) | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p158A2](messages/p158A2.md) | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p158B](messages/p158B.md) | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p158C1](messages/p158C1.md) | 155 | 7 November | nov07 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p158C3](messages/p158C3.md) | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p158D](messages/p158D.md) | 155 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p159A](messages/p159A.md) | 156 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p159B1](messages/p159B1.md) | 156 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p159_1](messages/p159_1.md) | 156 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p159D](messages/p159D.md) | 156 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p159E1](messages/p159E1.md) | 156 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p160A](messages/p160A.md) | 157 | 7 November |  | Unsolved |  |  |
| [p160A.2](messages/p160A.2.md) | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p160A3](messages/p160A3.md) | 157 | 7 November | nov07 | Solved, 11 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p160A4](messages/p160A4.md) | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p160A5](messages/p160A5.md) | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p160B](messages/p160B.md) | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p160B2](messages/p160B2.md) | 157 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p161A1](messages/p161A1.md) | 158 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p161A2](messages/p161A2.md) | 158 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p161B1](messages/p161B1.md) | 158 | 7 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p161C3](messages/p161C3.md) | 158 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p161D](messages/p161D.md) | 158 | 8 November |  | Duplicate entry |  |  |
| [p161E](messages/p161E.md) | 158 | 8 November |  | Unsolved |  |  |
| [p162A](messages/p162A.md) | 159 | 8 November | nov07 | Solved, 19 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p162B](messages/p162B.md) | 159 | 8 November |  | Unsolved |  |  |
| [p162B.2](messages/p162B.2.md) | 159 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p162_](messages/p162_.md) | 159 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p163A2](messages/p163A2.md) | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p163B](messages/p163B.md) | 160 | 8 November | nov07 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p163B.2](messages/p163B.2.md) | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p163C](messages/p163C.md) | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p163C2](messages/p163C2.md) | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p163D1](messages/p163D1.md) | 160 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p164_2](messages/p164_2.md) | 161 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p164B1](messages/p164B1.md) | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p164_](messages/p164_.md) | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p164_2.2](messages/p164_2.2.md) | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p164D1](messages/p164D1.md) | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p164D3](messages/p164D3.md) | 161 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p165A1](messages/p165A1.md) | 162 | 8 November |  | Unsolved |  |  |
| [p165B1](messages/p165B1.md) | 162 | 8 November | nov07 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p165C1](messages/p165C1.md) | 162 | 8 November |  | Unsolved |  |  |
| [p165C2](messages/p165C2.md) | 162 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p165D1](messages/p165D1.md) | 162 | 8 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p166A1](messages/p166A1.md) | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p166A1.2](messages/p166A1.2.md) | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p166A](messages/p166A.md) | 163 | 9 November |  | Unsolved |  |  |
| [p166A.2](messages/p166A.2.md) | 163 | 9 November |  | Unsolved |  |  |
| [p166A1.3](messages/p166A1.3.md) | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p166A1.4](messages/p166A1.4.md) | 163 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p167A](messages/p167A.md) | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| [p167A4](messages/p167A4.md) | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p167A5](messages/p167A5.md) | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| [p167_](messages/p167_.md) | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p167C1](messages/p167C1.md) | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p167D](messages/p167D.md) | 164 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p168A1](messages/p168A1.md) | 165 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p168A](messages/p168A.md) | 165 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p168A.2](messages/p168A.2.md) | 165 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p168A5](messages/p168A5.md) | 165 | 9 November | nov07 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p169A](messages/p169A.md) | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p169A2](messages/p169A2.md) | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p169A3](messages/p169A3.md) | 166 | 9 November |  | Unsolved |  |  |
| [p169B](messages/p169B.md) | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p169B2](messages/p169B2.md) | 166 | 9 November |  | Unsolved |  |  |
| [p169C1](messages/p169C1.md) | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p169C3](messages/p169C3.md) | 166 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p170A](messages/p170A.md) | 167 | 9 November | nov07 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p170B](messages/p170B.md) | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p170B3](messages/p170B3.md) | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p170B3.2](messages/p170B3.2.md) | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p170C1](messages/p170C1.md) | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p170D](messages/p170D.md) | 167 | 9 November |  | Unsolved |  |  |
| [p170E](messages/p170E.md) | 167 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p171A](messages/p171A.md) | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p171B](messages/p171B.md) | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p171C](messages/p171C.md) | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p171D](messages/p171D.md) | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p171E](messages/p171E.md) | 168 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p172A](messages/p172A.md) | 169 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p172B](messages/p172B.md) | 169 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p173A](messages/p173A.md) | 170 | 9 November |  | Unsolved |  |  |
| [p173B](messages/p173B.md) | 170 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p173B.2](messages/p173B.2.md) | 170 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p174A1](messages/p174A1.md) | 171 | 9 November | nov07 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017, claimed |
| [p174A3](messages/p174A3.md) | 171 | 9 November |  | Unsolved |  |  |
| [p174A3.2](messages/p174A3.2.md) | 171 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p174B1](messages/p174B1.md) | 171 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p174B](messages/p174B.md) | 171 | 9 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p174C](messages/p174C.md) | 171 | 9 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p175A](messages/p175A.md) | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p175A.2](messages/p175A.2.md) | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p175C1](messages/p175C1.md) | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p175C2](messages/p175C2.md) | 172 | 10 November |  | No cipher text |  |  |
| [p175C3](messages/p175C3.md) | 172 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p175D1](messages/p175D1.md) | 172 | 10 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p175D8](messages/p175D8.md) | 172 | 10 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p175E](messages/p175E.md) | 172 | 10 November |  | Unsolved |  |  |
| [p176A1](messages/p176A1.md) | 173 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p176A3](messages/p176A3.md) | 173 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p177A1](messages/p177A1.md) | 174 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p177A](messages/p177A.md) | 174 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p177A3](messages/p177A3.md) | 174 | 10 November |  | Unsolved |  |  |
| [p177B](messages/p177B.md) | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p177C](messages/p177C.md) | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p177D](messages/p177D.md) | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p177E](messages/p177E.md) | 174 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p178A1](messages/p178A1.md) | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p178A](messages/p178A.md) | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p178B2](messages/p178B2.md) | 175 | 10 November | nov07 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p178C](messages/p178C.md) | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p178C2](messages/p178C2.md) | 175 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p178C3](messages/p178C3.md) | 175 | 10 November | nov10 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p179A](messages/p179A.md) | 176 | 10 November |  | Unsolved |  | Norbert, 2017, in part |
| [p179A3](messages/p179A3.md) | 176 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p179A6](messages/p179A6.md) | 176 | 10 November |  | Unsolved |  |  |
| [p179B1](messages/p179B1.md) | 176 | 10 November | nov10 | Solved, 6 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p179B](messages/p179B.md) | 176 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p179B3](messages/p179B3.md) | 176 | 10 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p180A](messages/p180A.md) | 177 | 11 November | nov10 | Solved, 8 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p180B](messages/p180B.md) | 177 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p180B.2](messages/p180B.2.md) | 177 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p180B3](messages/p180B3.md) | 177 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p181A](messages/p181A.md) | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p181A2](messages/p181A2.md) | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p181A3](messages/p181A3.md) | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p181A4](messages/p181A4.md) | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p181A5](messages/p181A5.md) | 178 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p182A](messages/p182A.md) | 179 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p182B](messages/p182B.md) | 179 | 11 November | nov10 | Solved, 9 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p182C](messages/p182C.md) | 179 | 11 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p182D](messages/p182D.md) | 179 | 11 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p182D3](messages/p182D3.md) | 179 | 11 November |  | No cipher text |  |  |
| [p182D.2](messages/p182D.2.md) | 179 | 11 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p183A](messages/p183A.md) | 180 | ? November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p183B2](messages/p183B2.md) | 180 | ? November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p183B](messages/p183B.md) | 180 | ? November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p183D1](messages/p183D1.md) | 180 | ? November | nov10 | Solved, 20 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p183E](messages/p183E.md) | 180 | ? November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p184A](messages/p184A.md) | 181 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p184B](messages/p184B.md) | 181 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p185A](messages/p185A.md) | 182 | 12 November |  | Unsolved |  |  |
| [p185B](messages/p185B.md) | 182 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p185C](messages/p185C.md) | 182 | 12 November |  | Unsolved |  |  |
| [p186A](messages/p186A.md) | 183 | 12 November | nov10 | Solved, 2 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p186B](messages/p186B.md) | 183 | 12 November | nov10 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p186C](messages/p186C.md) | 183 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p186D](messages/p186D.md) | 183 | 12 November |  | Unsolved |  |  |
| [p186E](messages/p186E.md) | 183 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p186F](messages/p186F.md) | 183 | 12 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p187_](messages/p187_.md) | 184 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p187B](messages/p187B.md) | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p187B2](messages/p187B2.md) | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p187B3](messages/p187B3.md) | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p187C1](messages/p187C1.md) | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p187C](messages/p187C.md) | 184 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p187C3](messages/p187C3.md) | 184 | 13 November |  | Unsolved |  |  |
| [p188_2](messages/p188_2.md) | 185 | 13 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p188_](messages/p188_.md) | 185 | 13 November | nov13_20 | Solved, 32 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p188_.2](messages/p188_.2.md) | 185 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p188_.3](messages/p188_.3.md) | 185 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p189A](messages/p189A.md) | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p189A2](messages/p189A2.md) | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p189B1](messages/p189B1.md) | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p189B3](messages/p189B3.md) | 186 | 13 November |  | Unsolved |  |  |
| [p189C1](messages/p189C1.md) | 186 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p190A1](messages/p190A1.md) | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| [p190A](messages/p190A.md) | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| [p190B](messages/p190B.md) | 187 | 13 November |  | Unsolved |  |  |
| [p190G](messages/p190G.md) | 187 | 13 November |  | Unsolved |  |  |
| [p190D1](messages/p190D1.md) | 187 | 13 November |  | Unsolved |  |  |
| [p191A](messages/p191A.md) | 188 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p191B2](messages/p191B2.md) | 188 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p191_1](messages/p191_1.md) | 188 | 13 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p192A](messages/p192A.md) | 189 | 14 November |  | Unsolved |  |  |
| [p192B](messages/p192B.md) | 189 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p192C](messages/p192C.md) | 189 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p192D](messages/p192D.md) | 189 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p192E](messages/p192E.md) | 189 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p193A](messages/p193A.md) | 190 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p193B](messages/p193B.md) | 190 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p193C](messages/p193C.md) | 190 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p193D](messages/p193D.md) | 190 | 14 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p193_](messages/p193_.md) | 190 | 14 November | nov13_20 | Solved, 10 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p194A](messages/p194A.md) | 191 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert and Max Baertl, 2017 |
| [p194A.2](messages/p194A.2.md) | 191 | 14 November |  | Unsolved |  |  |
| [p195A2](messages/p195A2.md) | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p195A](messages/p195A.md) | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p195A.2](messages/p195A.2.md) | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p195_](messages/p195_.md) | 192 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p196A](messages/p196A.md) | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p196B](messages/p196B.md) | 193 | 14 November |  | Unsolved |  |  |
| [p196C](messages/p196C.md) | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p196D](messages/p196D.md) | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p196E](messages/p196E.md) | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p196F](messages/p196F.md) | 193 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p197A](messages/p197A.md) | 194 | 14 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p197B](messages/p197B.md) | 194 | 14 November | nov13_20 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p197C](messages/p197C.md) | 194 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p197D1](messages/p197D1.md) | 194 | 15 November |  | Unsolved |  |  |
| [p197E](messages/p197E.md) | 194 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p198A2](messages/p198A2.md) | 195 | 15 November | nov10 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p199A](messages/p199A.md) | 196 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p199B](messages/p199B.md) | 196 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p200A1](messages/p200A1.md) | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p200A3](messages/p200A3.md) | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p200B](messages/p200B.md) | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p200C](messages/p200C.md) | 197 | 15 November |  | Unsolved |  |  |
| [p200D](messages/p200D.md) | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p200E](messages/p200E.md) | 197 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p201A](messages/p201A.md) | 198 | 15 November |  | Unsolved |  |  |
| [p201B](messages/p201B.md) | 198 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p201C](messages/p201C.md) | 198 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p201D](messages/p201D.md) | 198 | 15 November |  | Unsolved |  |  |
| [p201E](messages/p201E.md) | 198 | 15 November |  | Unsolved |  |  |
| [p202A1](messages/p202A1.md) | 199 | 15 November |  | Unsolved |  |  |
| [p202A3](messages/p202A3.md) | 199 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p202A](messages/p202A.md) | 199 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p202_](messages/p202_.md) | 199 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p203A](messages/p203A.md) | 200 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p203B1](messages/p203B1.md) | 200 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p203B3](messages/p203B3.md) | 200 | 15 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p204A1](messages/p204A1.md) | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p204A2](messages/p204A2.md) | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p204B](messages/p204B.md) | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p204B2](messages/p204B2.md) | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p204C](messages/p204C.md) | 201 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p205A1](messages/p205A1.md) | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p205A2](messages/p205A2.md) | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p205B](messages/p205B.md) | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p205B2](messages/p205B2.md) | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p205B3](messages/p205B3.md) | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p205B4](messages/p205B4.md) | 202 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p206A2](messages/p206A2.md) | 203 | 16 November | nov13_16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p206_](messages/p206_.md) | 203 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p206_.2](messages/p206_.2.md) | 203 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p207A](messages/p207A.md) | 204 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p207B](messages/p207B.md) | 204 | 17 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p207_](messages/p207_.md) | 204 | 17 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p207_2](messages/p207_2.md) | 204 | 17 November |  | Unsolved |  |  |
| [p207D](messages/p207D.md) | 204 | 17 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p208A4](messages/p208A4.md) | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p208A2](messages/p208A2.md) | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p208A3](messages/p208A3.md) | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p208A4.2](messages/p208A4.2.md) | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p208B](messages/p208B.md) | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p208B8](messages/p208B8.md) | 205 | 16 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p209A](messages/p209A.md) | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p209A.2](messages/p209A.2.md) | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p209A3](messages/p209A3.md) | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p209B](messages/p209B.md) | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p209B.2](messages/p209B.2.md) | 206 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p210A](messages/p210A.md) | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p210A.2](messages/p210A.2.md) | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p210B](messages/p210B.md) | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p210C1](messages/p210C1.md) | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p210C](messages/p210C.md) | 207 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p211A](messages/p211A.md) | 208 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p211A.2](messages/p211A.2.md) | 208 | 18 November | nov16 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p212A1](messages/p212A1.md) | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p212B](messages/p212B.md) | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p212B2](messages/p212B2.md) | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p212C1](messages/p212C1.md) | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p212C](messages/p212C.md) | 209 | 19 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p213A1](messages/p213A1.md) | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p213A](messages/p213A.md) | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p213B](messages/p213B.md) | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p213C](messages/p213C.md) | 210 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p213D](messages/p213D.md) | 210 | 20 November |  | Unsolved |  |  |
| [p214A](messages/p214A.md) | 211 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p214B](messages/p214B.md) | 211 | 20 November | nov19 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p214B1](messages/p214B1.md) | 211 | 19 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p214B2](messages/p214B2.md) | 211 | 19 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p214B.2](messages/p214B.2.md) | 211 | 19 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p215A](messages/p215A.md) | 212 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p215A2](messages/p215A2.md) | 212 | 22 November |  | Unsolved |  |  |
| [p215A.2](messages/p215A.2.md) | 212 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p215A.3](messages/p215A.3.md) | 212 | 22 November |  | Unsolved |  |  |
| [p215A.4](messages/p215A.4.md) | 212 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p216A6](messages/p216A6.md) | 213 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p216A7](messages/p216A7.md) | 213 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p216_1](messages/p216_1.md) | 213 | 23 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p216_2](messages/p216_2.md) | 213 | 23 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p216_3](messages/p216_3.md) | 213 | 23 November | nov22 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p217A1](messages/p217A1.md) | 214 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p217B](messages/p217B.md) | 214 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p217C](messages/p217C.md) | 214 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p218A](messages/p218A.md) | 215 | 22 November |  | Unsolved |  |  |
| [p218B1](messages/p218B1.md) | 215 | 22 November |  | Unsolved |  |  |
| [p218B4](messages/p218B4.md) | 215 | 22 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p218B3](messages/p218B3.md) | 215 | 22 November |  | Unsolved |  |  |
| [p218C](messages/p218C.md) | 215 | 22 November |  | Unsolved |  | Norbert and Max Baertl, 2017, in part |
| [p219A1](messages/p219A1.md) | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p219A](messages/p219A.md) | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p219A.2](messages/p219A.2.md) | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p219A4](messages/p219A4.md) | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p219B1](messages/p219B1.md) | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p219B](messages/p219B.md) | 216 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p220A](messages/p220A.md) | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p220A.2](messages/p220A.2.md) | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p220A3](messages/p220A3.md) | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p220A4](messages/p220A4.md) | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p220A.3](messages/p220A.3.md) | 217 | 24 November | nov22 | Solved, 14 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p220B](messages/p220B.md) | 217 | 24 November |  | Unsolved |  |  |
| [p220B2](messages/p220B2.md) | 217 | 24 November | nov22 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p220C](messages/p220C.md) | 217 | 24 November |  | Unsolved |  |  |
| [p220C.2](messages/p220C.2.md) | 217 | 24 November | dec09_history | Solved | Childs, 1919 | Prinz, 2026 |
| [p221A](messages/p221A.md) | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p221A2](messages/p221A2.md) | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p221A6](messages/p221A6.md) | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p221B2](messages/p221B2.md) | 218 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p221B3](messages/p221B3.md) | 218 | 25 November | nov25 | Solved, 4 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p222A1](messages/p222A1.md) | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p222A2](messages/p222A2.md) | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p222B](messages/p222B.md) | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p222C](messages/p222C.md) | 219 | 25 November |  | Unsolved |  |  |
| [p222D1](messages/p222D1.md) | 219 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p223A2](messages/p223A2.md) | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p223B](messages/p223B.md) | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p223C1](messages/p223C1.md) | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p223C2](messages/p223C2.md) | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p223C3](messages/p223C3.md) | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p223C4](messages/p223C4.md) | 220 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p224A5](messages/p224A5.md) | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p224A6](messages/p224A6.md) | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p224B1](messages/p224B1.md) | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p224B2](messages/p224B2.md) | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p224B](messages/p224B.md) | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p224B4](messages/p224B4.md) | 221 | 25 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p225A](messages/p225A.md) | 222 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p225A2](messages/p225A2.md) | 222 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p226A1](messages/p226A1.md) | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p226A](messages/p226A.md) | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p226A3](messages/p226A3.md) | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p226B](messages/p226B.md) | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p226B.2](messages/p226B.2.md) | 223 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p227A1](messages/p227A1.md) | 224 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p227A2](messages/p227A2.md) | 224 | 27 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p227B](messages/p227B.md) | 224 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p227C1](messages/p227C1.md) | 224 | 26 November | nov25 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p227C2](messages/p227C2.md) | 224 | 26 November | nov25 | Solved, 12 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p228A](messages/p228A.md) | 225 | 28 November | nov28 | Solved, 6 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p228B1](messages/p228B1.md) | 225 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p228B](messages/p228B.md) | 225 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p229A2](messages/p229A2.md) | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p229B2](messages/p229B2.md) | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p229B1](messages/p229B1.md) | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p229B2.2](messages/p229B2.2.md) | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p229B](messages/p229B.md) | 226 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p230A4](messages/p230A4.md) | 227 | 29 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p230B](messages/p230B.md) | 227 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p230D](messages/p230D.md) | 227 | 28 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p231A](messages/p231A.md) | 228 | 30 November | nov28 | Solved, 52 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| [p231B1](messages/p231B1.md) | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p231B2](messages/p231B2.md) | 228 | 30 November |  | Unsolved |  |  |
| [p231B3](messages/p231B3.md) | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p231C1](messages/p231C1.md) | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p231C2](messages/p231C2.md) | 228 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p232A1](messages/p232A1.md) | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p232A](messages/p232A.md) | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p232A3](messages/p232A3.md) | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p232B](messages/p232B.md) | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p232B2](messages/p232B2.md) | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p232_](messages/p232_.md) | 229 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p233A3](messages/p233A3.md) | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p233A4](messages/p233A4.md) | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p233B](messages/p233B.md) | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p233C](messages/p233C.md) | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p233D](messages/p233D.md) | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |
| [p233D.2](messages/p233D.2.md) | 230 | 30 November | nov28 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 |  |

## The 22 entries on Schmeh's list

Klaus Schmeh's list of unsolved ADFGVX messages has 22 entries. Each was matched to an entry of the log by its opening groups. Entry 10 turned out to be a log row that joins two other messages. A solution of entries 18 and 19 under a new key was published in the comments on Schmeh's post in May 2017, by George Lasry and Norbert.

| Schmeh | Entry | Page | Date | Key | Status | Key found by | Solution published by |
|---|---|---|---|---|---|---|---|
| 1 | [p076A](messages/p076A.md) | 73 | 26 October |  | Unsolved |  |  |
| 2 | [p103A](messages/p103A.md) | 100 | 1 November | nov01 | Solved, 7 open | Lasry, Niebel, Kopal and Wacker, 2017 | Armin, 2017, claimed |
| 3 | [p108BB](messages/p108BB.md) | 105 | 2 November | nov01 | Solved, 5 open | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert and Max Baertl, 2017 |
| 4 | [p112D](messages/p112D.md) | 109 | 3 November |  | Unsolved |  | Norbert, 2017, in part |
| 5 | [p135B](messages/p135B.md) | 132 | 5 November |  | Unsolved |  | Thomas and Norbert, 2017, in part |
| 6 | [p149B](messages/p149B.md) | 146 | 6 November | nov04 | Solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017 |
| 7 | [p155E](messages/p155E.md) | 152 | 7 November |  | Unsolved |  |  |
| 8 and 9 | [p156C3](messages/p156C3.md) | 153 | 7 November | ours_nov07_18col | Solved | This project, 2026 | This project, 2026 |
| 8 and 9 | [p156C6](messages/p156C6.md) | 153 | 7 November | ours_nov07_18col | Solved, 3 open | This project, 2026 | This project, 2026 |
| 10 | [p161D](messages/p161D.md) | 158 | 8 November |  | Duplicate entry |  |  |
| 11 and 12 | [p167A](messages/p167A.md) | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| 11 and 12 | [p167A5](messages/p167A5.md) | 164 | 9 November |  | Unsolved |  | Norbert, 2017, in part |
| 13 | [p173A](messages/p173A.md) | 170 | 9 November |  | Unsolved |  |  |
| 14 | [p174A1](messages/p174A1.md) | 171 | 9 November | nov07 | Partially solved | Lasry, Niebel, Kopal and Wacker, 2017 | Norbert, 2017, claimed |
| 15 | [p179A](messages/p179A.md) | 176 | 10 November |  | Unsolved |  | Norbert, 2017, in part |
| 16 | [p179B1](messages/p179B1.md) | 176 | 10 November | nov10 | Solved, 6 open | Lasry, Niebel, Kopal and Wacker, 2017 | This project, 2026 |
| 17 | [p218C](messages/p218C.md) | 215 | 22 November |  | Unsolved |  | Norbert and Max Baertl, 2017, in part |
| 18 and 19 | [p190A1](messages/p190A1.md) | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| 18 and 19 | [p190A](messages/p190A.md) | 187 | 13 November | chi_2017_comments | Solved | Lasry and Norbert, 2017 | Lasry and Norbert, 2017 |
| 20 | [p192A](messages/p192A.md) | 189 | 14 November |  | Unsolved |  |  |
| 21 | [p201D](messages/p201D.md) | 198 | 15 November |  | Unsolved |  |  |
| 22 | [p220C.2](messages/p220C.2.md) | 217 | 24 November | dec09_history | Solved | Childs, 1919 | Prinz, 2026 |
