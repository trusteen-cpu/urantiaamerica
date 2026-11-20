# doctrine menu ("Core Doctrines of The Urantia Book"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\doctrine\`.
The English web edition you are translating: `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\doctrine\` (read only; open
a chapter page to see how blocks look). The book (Jay Han): Preface (ch00), 32 chapters in 7 parts, Afterword (ch33). A doctrinal study
that explains the logic of each teaching (definition → grounds → structure → consequences) and grounds every step in quotations.
Each chapter = paragraphs and numbered section headings, Urantia Book quotations, tables (4–5 per chapter), and a box of three
"Questions for Reflection".

## Files
- `work/src_cNN.json` — **your source**: every English unit of chunk cNN except the quotations. Read only.
  Chunks: c01 = part titles, audiobook titles, Preface, ch01–05 · c02 ch06–11 · c03 ch12–16 · c04 ch17–22 · c05 ch23–27 · c06 ch28–32 + Afterword.
- `<l>/cNN.json` — **your output**: a JSON object with exactly the same keys (same order) and the same shape, every value translated.
  Write it from a Python script: `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc or a PowerShell command line. Put your own scripts only in `scratch/<l>_cNN/` (create it;
  nobody else uses it). Load your output file if it exists, add/replace units, dump again (save after every chapter or so).
- `<l>/quotes_cNN.json` — **your second output**: the quotations the automatic aligner could not cut (listed in
  `work/todo_<l>_cNN.json`): `{"ch05:7": "official text cut verbatim", ...}` — one entry per todo key, key copied exactly.
- Helpers (read only; run them from the doctrine folder):
  - `python show_q.py <l> cNN [ch05]` — every quotation of the chunk (or of one chapter): the English and the official cut. Read the official
    quotations of a chapter before translating it, and reuse their wording and terms in your prose.
  - `python show_q.py <l> todo cNN` — only the quotations you must cut, with the full English and official verses.
  - `python show_q.py <l> term "Adjuster"` — glossary `../glossary/glossary_<l>.json` ([English, official term, definition]).
  - `python ../amq.py <l> 45:4.2` prints an official verse; `python ../amq.py <l> "?Ajustador"` finds verses containing a word.
- Check: `python build_doctrine_am.py <l> --chunk cNN --report 300` — must end with `errors 0` (review the warnings too).

## Unit shapes
| English value | What it is | What you return |
|---|---|---|
| `"string"` (`chNN:<i>`) | paragraph or section heading (`"1. One Center, Six Concentric Levels of Space"`) | one string, no `\n`, plain text (no HTML/markdown); headings keep their number `"1. …"` |
| `{"cap": "Table 5.1  …", "rows": [[header…], [row…], …]}` | table | same number of rows and cells; caption es `"Tabla 5.1  …"`, fr `"Tableau 5.1  …"`, pt `"Tabela 5.1  …"` (keep the two spaces) |
| `{"title": "Questions for Reflection", "items": ["1. …", …]}` | end-of-chapter box | same number of items, keep `1.`/`2.`/`3.`; title es "Preguntas para la reflexión", fr "Questions pour la réflexion", pt "Perguntas para reflexão" |
| `chNN:label` | `"Chapter 5"`, `"Preface"`, `"Afterword"` | es "Capítulo 5" / "Prefacio" / "Epílogo"; fr "Chapitre 5" / "Préface" / "Postface"; pt "Capítulo 5" / "Prefácio" / "Posfácio" |
| `chNN:title` / `chNN:sub` | chapter title split at the colon | two separate strings (the page prints the subtitle under the title) |
| `part:N` (c01) | part title, e.g. "God: The Starting Point of Every Doctrine" | keep the colon structure |
| `audio:NN` (c01) | titles of the 30 English audiobooks (the links open English audio) | translate the title |

## References (checked)
Every `P:S.p` reference inside a unit — in prose `(33:7.1)`, in table "Source" cells `12:1.10`, in questions — must stay exactly as written
(same numbers, colon and dot). The checker compares the set of references in each unit with the English (`references changed`).
Ranges and lists keep their form (`15:10.11~12`, `12:1.12, 12:1.16`). Cells that are only a reference, a number or "—" stay as they are.

## Quotations you cut (quotes_cNN.json) — never translate them yourself
- Quotations are separate units handled by the builder: 432 es / 352 fr / 437 pt were cut automatically from the official translation.
  You cut only the todo ones. The English cut is usually one or more whole English sentences (pieces joined by ` … `), sometimes a part of a sentence.
  The official verse splits/joins sentences differently, so the aligner gave up. Take the official words that correspond to the English,
  **character for character** (copy from the verse; the checker ignores only whitespace), and join pieces with ` … ` (space, U+2026, space) in verse order.
- If one official sentence covers more than the English (e.g. English ends at ";" but the official sentence continues), cut it at the
  corresponding place when that is clean (a clause boundary); otherwise take the whole official sentence. If the English is one sentence
  but the official has two, take both. Keep omissions where the English has them. Do not add extra material: the official cut should cover
  the same content as the English (the checker warns when the length ratio is off).
- Keep the official punctuation inside; drop only an opening/closing guillemet or quotation mark that would be cut in half.
- Do not put the quotation in quotation marks (the page shows it in a box).

## Prose: terms and conventions
- Always the official terms (glossary / `<l>.json`): es Padre Universal, Hijo Eterno, Espíritu Infinito, Ajustador del Pensamiento,
  Ser Supremo, Trinidad del Paraíso, YO SOY, morontial, mundos de estancia, Hijo Creador, Espíritu Materno del Universo, Micael (never Miguel),
  Gabriel, Ancianos de los Días, Espíritu de la Verdad, reino del cielo (official text: 179 vs 17); fr Père Universel, Fils Éternel, Esprit Infini, Ajusteur de Pensée,
  Être Suprême, Trinité du Paradis, JE SUIS, morontiel, mondes des maisons, Fils Créateur, Esprit-Mère de l’Univers, Micaël, Gabriel, Anciens des Jours,
  Esprit de Vérité, royaume des cieux; pt Pai Universal, Filho Eterno, Espírito Infinito, Ajustador do Pensamento, Ser Supremo, Trindade do Paraíso,
  EU SOU, moroncial, mundos das mansões, Filho Criador, Espírito Materno do Universo, Michael, Gabriel, Anciães dos Dias, Espírito da Verdade, Reino do céu.
  **These are reminders, not authority: confirm each with show_q (the official quotations of the same chapter) or amq "?word" — do not invent.**
- Book title in prose: es *El libro de Urantia*, fr *le Livre d’Urantia* (du Livre d’Urantia), pt *O Livro de Urântia* (plain text, no markup).
  The title of this book (Preface): es "Doctrinas fundamentales de El libro de Urantia", fr "Doctrines essentielles du Livre d’Urantia",
  pt "Doutrinas fundamentais de O Livro de Urântia".
- "Paper 57" → es "documento 57", fr "fascicule 57", pt "documento 57"; "Paper 57:3" / "section 3 of Paper 57" → documento 57, sección 3 /
  fascicule 57, section 3 / documento 57, seção 3; "the Foreword" → es "el Prólogo", fr "l’Introduction", pt "a Introdução".
  A paper title quoted in prose: use the official title (`python -c "import sys; sys.path.insert(0,'..'); import amq; print(amq.title('es', 105))"`).
- "Part One/Part Two" → es "la primera/segunda parte", fr "la première/deuxième partie", pt "a primeira/segunda parte"; "Part 2" in tables →
  "Parte 2" / "Partie 2" / "Parte 2". "Chapter 5" → Capítulo 5 / chapitre 5 / capítulo 5. "the revelators" → es los reveladores, fr les révélateurs,
  pt os reveladores. "the text" (= The Urantia Book) → el texto / le texte / o texto.
- Short phrases quoted inside commentary (“a silent or inactive member” (32:4.1)) are not checked, but use the official wording of the cited
  or nearby verse (find it with amq), in your quotation marks: es «…», fr « … », pt “…”.
- Bible references → book names in your language (es Juan 14:6, fr Jean 14:6, pt João 14:6). Christian creeds and church terms in the usual form
  of your language (Credo niceno / Symbole de Nicée / Credo niceno). "Christology" → cristología / christologie / cristologia.
- Pronouns for God: follow the official verses (es él lower case as the official text does; fr il; pt Ele/ele as the official text does).
- Preface ch00:4 says "every quotation is taken word for word from The Urantia Book": say instead that the quotations are reproduced
  word for word from the official Spanish/French/Portuguese translation published by Urantia Foundation (fr Fondation Urantia), each with its
  paper, section and paragraph number. ch00:9 / ch33:11 mention the English audiobooks, QR codes, ebook and printed book: translate faithfully
  (the audiobooks are in English; keep "urantiareaders.com"). Everything else: translate faithfully.
- Style: faithful, natural, standard written language; measured expository tone (not preaching); same content and order; add nothing, drop nothing.
  es neutral Spanish (formal "usted" if a "you" occurs). fr 1990 reformed spelling as the official text (maitre, ile, connaitre, paraitre,
  surement, aout); « » with a normal space inside, normal space before ; : ! ? (the builder converts it to a no-break space).
  pt Brazilian spelling as the official text (pre-2009 forms where the official text has them, e.g. "idéia", "vôo" — check with amq).
- No Korean anywhere; no English left (the checker flags English function words such as the/and/of/which and values left identical to English).
