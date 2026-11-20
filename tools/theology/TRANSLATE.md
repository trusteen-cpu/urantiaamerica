# theology menu ("Theology of The Urantia Book"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology\`.
The English web edition you are translating: `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\theology\` (read only).
A calm theological handbook: 37 chapters in 8 parts; each chapter = title, subtitle, summary, 4–5 sections; each section has
numbered units = key proposition (`.k`) → commentary paragraph (`.p`) → 1–2 Urantia Book quotations; then reflection questions.

## Files
- `work/src_cNN.json` — **your source**: the English prose units of chunk cNN (quotations and UI strings are not in it). Read only.
- `<l>/cNN.json` — **your output**: a JSON object with exactly the same keys (same order), every value translated.
  Write it from a Python script: `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Put your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Load your output file if it exists, add/replace units, dump again (save after every chapter or so).
- `<l>/quotes_cNN.json` — **your second output**: the quotations the automatic aligner could not cut (listed in
  `work/todo_<l>_cNN.json`): `{"ch01.s2.u1.q2#0": "official text cut verbatim", ...}` — one entry per todo key, key copied exactly.
- Helpers (read only):
  - `python show_q.py <l> cNN [ch03.s2]` — every quotation of the chunk: English cut and the official cut (auto) — read the official
    quotations of a unit before translating its `.k`/`.p`, and reuse their wording/terms.
  - `python show_q.py <l> todo cNN` — only the quotations you must cut, with full English and official verses.
  - `python show_q.py <l> term "Adjuster"` — glossary `../glossary/glossary_<l>.json` ([English, official term, definition]).
  - `python ../amq.py <l> 45:4.2` prints an official verse; `python ../amq.py <l> "?Ajustador"` finds verses containing a word.
- Check: `python build_theology_am.py <l> --chunk cNN --report 300` — must end with `errors 0` (review warnings too).

## Quotations you cut (quotes_cNN.json) — never translate them yourself
- The English cut always consists of whole English sentences (pieces joined by ` … `). The official verse splits/joins sentences
  differently, so the aligner gave up. Take the official words that correspond to each English piece, **character for character**
  (copy from the verse; the checker ignores only whitespace), and join pieces with ` … ` (space, U+2026, space) in verse order.
- If one official sentence covers more than the English piece (e.g. English ends at ";" but the official sentence continues),
  cut it at the corresponding place when that is clean (a clause boundary); otherwise take the whole official sentence.
  If the English piece is one sentence but the official has it as two, take both. Keep omissions where the English has them.
- Keep the official punctuation inside; drop only an opening/closing guillemet or quotation mark that would be cut in half.
- Do not put the quotation in quotation marks (the page shows it in a box).

## Prose: terms and conventions
- Always the official terms (glossary / `<l>.json`): es Padre Universal, Hijo Eterno, Espíritu Infinito, Ajustador del Pensamiento,
  Ser Supremo, Trinidad del Paraíso, morontial, mundos de estancia, Hijo Creador, Espíritu Materno, Micael (never Miguel),
  Espíritu de la Verdad, reino del cielo; fr Père Universel, Fils Éternel, Esprit Infini, Ajusteur de Pensée, Être Suprême,
  Trinité du Paradis, morontiel, mondes des maisons, Fils Créateur, Esprit-Mère, Micaël, Esprit de Vérité, royaume des cieux;
  pt Pai Universal, Filho Eterno, Espírito Infinito, Ajustador do Pensamento, Ser Supremo, Trindade do Paraíso, moroncial,
  mundos das mansões, Filho Criador, Espírito Materno, Michael, Espírito da Verdade, Reino do céu. **Confirm with show_q (the quoted official verses
  of the same unit) or amq "?word" — do not invent.**
- Book title in prose: es *El libro de Urantia*, fr *le Livre d’Urantia*, pt *O Livro de Urântia* (plain text, no markup).
  "Urantia Book theology" → es "la teología de El libro de Urantia", fr "la théologie du Livre d’Urantia", pt "a teologia de O Livro de Urântia".
- "Paper 57" → es "documento 57", fr "fascicule 57", pt "documento 57"; "the Foreword" → es "el Prólogo", fr "l’Introduction", pt "a Introdução".
- Short phrases quoted inside commentary ("Be you perfect…") are not checked, but use the official wording when you can identify it
  (find it with amq "?word"), in your quotation marks: es «…», fr « … », pt “…”.
- Bible references → book names in your language. Numbers in words stay words.
- Pronouns for God: es Él/él as the official text does (lower case "él" — follow the official verses); fr il; pt Ele/ele (follow the official verses).
- Part names (used in the text when a part is mentioned; c01 translates them): es 1 Dios · 2 El universo · 3 Espíritus e Hijos ·
  4 El hombre · 5 Pecado y salvación · 6 Jesús y el reino · 7 La vida religiosa · 8 La ascensión eterna;
  fr Dieu · L’univers · Esprits et Fils · L’homme · Péché et salut · Jésus et le royaume · La vie religieuse · L’ascension éternelle;
  pt Deus · O universo · Espíritos e Filhos · O homem · Pecado e salvação · Jesus e o reino · A vida religiosa · A ascensão eterna.
- Style: faithful, natural, standard written language; calm expository tone; same content and order; add nothing, drop nothing.
  es neutral Spanish (formal "usted" if a "you" occurs). fr 1990 reformed spelling as the official text (maitre, ile, connaitre,
  paraitre, surement, aout); « » with a normal space inside, normal space before ; : ! ? (the builder converts it to a no-break space).
  pt Brazilian spelling as the official text.
- Reflection questions (`.qsN`): questions in your language (es ¿…?).
- No Korean anywhere; no English left (the checker flags English function words such as the/and/of/which).

## Chunk c01 only: front matter
- `front.title`: es "Teología de El libro de Urantia" · fr "Théologie du Livre d’Urantia" · pt "Teologia de O Livro de Urântia".
- `front.author`: "Jay Han". `front.sub`: translate. `part.1`…`part.8`: the names above.
- `front.preface3` describes the English edition ("quotations ... reproduced word for word from the original English text"): say
  instead that in this edition the quotations are reproduced word for word from the official Spanish/French/Portuguese translation of the book
  published by Urantia Foundation (fr "Fondation Urantia"), each followed by its paper:section.paragraph reference
  (es documento:sección.párrafo, fr fascicule:section.paragraphe, pt documento:seção.parágrafo). Everything else: translate faithfully.
- "more than two thousand pages" stays.
