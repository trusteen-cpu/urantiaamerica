# books ("The Life and Teachings of Jesus" · "The Twelve Apostles of Jesus"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\books\`.
The English web editions (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\jesus-book\`
and `...\site\en\apostles-book\`.

Two books by Jay Han, both **narrative retellings of Part IV of The Urantia Book** (Papers 120–196):
- **jesus** = *The Life and Teachings of Jesus* (prologue, 53 chapters, epilogue; 8 parts; ~143,000 words, 20 chunks). It follows Part IV
  closely and quotes the words of Jesus (and of Gabriel, Mary, the apostles …) **verbatim** wherever it can.
- **apostles** = *The Twelve Apostles of Jesus* (26 chapters in 5 parts + epilogue; ~163,000 words, 25 chunks). A novel: the four years beside
  Jesus seen through the apostles' eyes. The words of Jesus are retold, not quoted. Each chapter ends with "Sources for This Chapter" notes
  (paper references and what was added as fiction): translate them like prose, keep every reference number.

The text you translate is the author's. **Do not add sentences, explanations or facts that are not in the English, and do not drop any.**
Narrative style: literary but plain standard written language, the tone of the English (no preaching, no embellishment).

## Files
- `work/<book>/src_cNN.json`: **your source**, the English units of chunk cNN of that book (quotation blocks are not in it). Read only.
- `<l>/<book>/cNN.json`: **your output**, a JSON object with exactly the same keys in the same order and every value translated
  (`<l>` = es | fr | pt; e.g. `es/jesus/c03.json`). Write it from a Python script with
  `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`. Never put non-ASCII text in a shell heredoc.
  Keep your own scripts only in `scratch/<l>_<book>_cNN/` (create it; nobody else uses it). Work in parts: load your output file if it
  exists, add units, dump it again, and save often.
- `work/<book>/todo_<l>_cNN.json`: Urantia Book **block quotations** the tool could not cut automatically (see below) → you write
  `<l>/<book>/quotes_cNN.json`. Most chunks have none.
- `work/<book>/inline_<l>_cNN.json`: for every ⟦Q⟧-marked quotation inside a unit: `{"cit", "en", "verses", "auto"?}` (see below).
- Helpers (read only): `python ../amq.py <l> 162:7.2` prints an official verse; `python ../amq.py <l> "?Capernaum"` finds verses that contain a word.
  Glossary `../glossary/glossary_<l>.json` ([English, official term, definition]).
- Check: `python build_books_am.py <l> --book <book> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left
  behind, “ ” in French, post-2009 Portuguese spelling).

## Chunks
Whole chapters, about 6,000–8,000 English words each (`python extract_src.py` prints the list). c01 of each book also holds the screen
strings (`ui.*`) and the front matter (`intro.*`). The order of work is in `../QUEUE.txt` (`books jesus es c01` …).

| book | chunks | c01 | then |
|---|---|---|---|
| jesus | c01–c20 | ui, intro (about, eight parts, preface), prologue, ch. 1–2 | about three chapters per chunk, ch. 54 = epilogue in c20 |
| apostles | c01–c25 | ui, intro (about, who this book is for, preface), ch. 1 | one chapter per chunk (c23 = ch. 23–24), ch. 26 = epilogue |

## Unit format
Every value is a string.
- `ui.*` screen strings, `intro.*` front matter, `partN` part names ("Part One: The Child of Nazareth"), `chNN.title`,
  `chNN.bNNN` the blocks of chapter NN in order (headings, paragraphs, notes), `chNN.src` (only when the English source line is not just
  "Paper 122, sections 0–6": that line is written by the builder in your language — es Documento/secciones, fr Fascicule/sections,
  pt Documento/seções).
- Chapter labels ("Chapter 12", "Prologue", "Epilogue") and the table of contents are built automatically from `ui.chapter`, `ui.prologue`,
  `ui.epilogue` and your chapter titles / headings.
- `*…*` is italic (book titles, emphasis): keep the pairs (the checker counts the asterisks). `{n}`, `{title}` are placeholders: keep them.
- Keep the author's name **Jay Han** and the paragraph references "(196:1.3)", "(137:0.1, 137:1.1–1.4)" unchanged.
- Dialogue: es and fr use « » (fr with a normal space inside and before ; : ! ? — the builder turns it into a no-break space); pt “ ”.
  Inner quotations: es “ ”, fr “ ” or ‹ › as the official text does, pt ‘ ’.

## Urantia Book quotations: never translate them yourself
**Block quotations** (`q` blocks: the angel's words, Zacharias' song, Michael's charge …; jesus only; 83 + one line of the preface) are not in
your source: the builder takes them from the official translation (`tools/data/<l>.json`). 81 (es, pt) / 76 (fr) are cut automatically
(`auto_<l>.json`). The rest are in `work/<book>/todo_<l>_cNN.json` as
`{"ch23.b020": {"cits", "en", "verses", "why"}}`: `en` is the English quotation (pieces joined with " … "), `verses` the official paragraph(s).
Write `<l>/<book>/quotes_cNN.json` = `{"ch23.b020": "official words … official words", ...}`: the official words that correspond to the
English, **copied character for character** from the verse(s), pieces joined with " … " exactly where the English has "…", in verse order,
**without** surrounding « » / “ ” (the builder adds them). The checker ignores only whitespace. If `why` says the English was not found
verbatim, the verses are best guesses: look for the right verse with `amq.py` and tell the coordinator the citation if it is not listed (the
checker only accepts the listed verses).

**Inline quotations** (jesus: about 1,090 quoted speeches in the prose that are verbatim Urantia Book words; apostles: 4) are marked in the
English unit: `Jesus said, “⟦Q 141:4.2⟧Who is this God of the kingdom?⟦/Q⟧” Andrew …`. Keep the markers and the citation inside the opening
marker exactly (it can be two verses: `⟦Q 144:8.2,144:8.3⟧`). Replace only the text between the markers with the corresponding official words
of the verse(s), **character for character**. `work/<book>/inline_<l>_cNN.json` lists them per unit in order: `verses` = the official
paragraph(s); `auto` (about 80 %) = the official words already cut for you — check that it matches the English and copy it. Without `auto`,
cut the official sentence at the corresponding words yourself; you may include a few more official words if the clause boundary falls
differently, but nothing that is not in the verse; join omissions with " … " as the English does. Put your language's quotation marks
**outside** the markers (`«⟦Q 141:4.2⟧¿Quién es este Dios del reino?⟦/Q⟧»`) and adjust the narration around it so it reads naturally.
The checker verifies every marked text; a unit fails if a marker is lost, added or changes citation.
Unmarked short quotations (fewer than six words, or paraphrased) are translated normally; when the words obviously come from the book, use
the official wording if `amq.py "?word"` finds it.

## Terms (official translation, Part IV; same as `../jesus/TRANSLATE.md`)
| English | es | fr | pt |
|---|---|---|---|
| The Urantia Book (in prose) | *El libro de Urantia* | *le Livre d’Urantia* | *O Livro de Urântia* |
| Paper 139 / section 3 | documento 139 / sección 3 | fascicule 139 / section 3 | documento 139 / seção 3 |
| the Master | el Maestro | le Maitre | o Mestre |
| kingdom of heaven | reino del cielo | royaume des cieux | Reino do céu |
| gospel of the kingdom | evangelio del reino | évangile du royaume | evangelho do Reino |
| Father in heaven | Padre en el cielo / Padre celestial (check amq) | Père qui est aux cieux / Père céleste | Pai que está no céu / Pai celeste |
| Son of Man / Son of God | Hijo del Hombre / Hijo de Dios | Fils de l’Homme / Fils de Dieu | Filho do Homem / Filho de Deus |
| Spirit of Truth | Espíritu de la Verdad | Esprit de Vérité | Espírito da Verdade |
| Thought Adjuster | Ajustador del Pensamiento | Ajusteur de Pensée | Ajustador do Pensamento |
| Michael (of Nebadon) / Christ Michael | Micael (de Nebadon) / Cristo Micael | Micaël (de Nébadon) / Christ Micaël | Michael (de Nébadon) / Cristo Michael |
| Immanuel / Gabriel / Salvington | Emanuel / Gabriel / Salvington | Emmanuel / Gabriel / Salvington | Emanuel / Gabriel / Salvington (check amq) |
| bestowal | autootorgamiento | effusion | auto-outorga |
| Creator Son / Universal Father | Hijo Creador / Padre Universal | Fils Créateur / Père Universel | Filho Criador / Pai Universal |
| Orvonton / Nebadon / Urantia | Orvonton / Nebadon / Urantia | Orvonton / Nébadon / Urantia | Orvônton / Nébadon / Urântia |
| morontia appearance | aparición morontial | apparition morontielle | aparição moroncial |
| John the Baptist | Juan el Bautista | Jean le Baptiste | João Batista |
| apostles / the seventy / women's corps | apóstoles / los setenta / cuerpo de mujeres | apôtres / les soixante-dix / corps évangélique des femmes (check amq 150:1) | apóstolos / os setenta / corpo de mulheres |
| Passover / Pentecost / Sanhedrin / Pharisees | Pascua / Pentecostés / sanedrín / fariseos | Pâque / Pentecôte / sanhédrin / pharisiens | Páscoa / Pentecostes / sinédrio / fariseus |
| Capernaum / Bethsaida / Kheresa / Magadan / Gethsemane | Capernaum / Betsaida / Queresa / Magadán / Getsemaní | Capharnaüm / Bethsaïde / Khérésa / Magadan / Gethsémani | Cafarnaum / Betsaida / Queresa / Magadam / Getsêmani |
| Simon Peter, Andrew, James and John Zebedee, Philip, Nathaniel, Matthew Levi, Thomas, James and Judas Alpheus, Simon Zelotes, Judas Iscariot | Simón Pedro, Andrés, Santiago y Juan Zebedeo, Felipe, Natanael, Mateo Leví, Tomás, Jacobo y Judas Alfeo, Simón el Zelote, Judas Iscariote | Simon Pierre, André, Jacques et Jean Zébédée, Philippe, Nathanael, Matthieu Lévi, Thomas, Jacques et Judas Alphée, Simon Zélotès, Judas Iscariot | Simão Pedro, André, Tiago e João Zebedeu, Filipe, Natanael, Mateus Levi, Tomé, Tiago e Judas Alfeus, Simão zelote, Judas Iscariotes |
| Joseph, Mary, James, Jude, Ruth, Miriam, Martha | José, María, Santiago, Judá, Rut, Miriam, Marta (check amq) | Joseph, Marie, Jacques, Jude, Ruth, Miriam, Marthe | José, Maria, Tiago, Judá, Rute, Míriam, Marta (check amq) |
| David Zebedee / John Mark / Abner / Lazarus / Nicodemus | David Zebedeo / Juan Marcos / Abner / Lázaro / Nicodemo | David Zébédée / Jean Marc / Abner / Lazare / Nicodème | Davi Zebedeu / João Marcos / Abner / Lázaro / Nicodemos |
| Ganid / Gonod / Rebecca / Zacharias / Elizabeth | Ganid / Gonod / Rebeca / Zacarías / Elizabeth | Ganid / Gonod / Rébecca / Zacharie / Élisabeth | Ganid / Gonod / Rebeca / Zacarias / Isabel |
Anything else: glossary first, then `amq.py "?word"`. Place names and persons: always the official spelling (find them in the verse the
chapter's source line or the "Sources" note cites). pt: the official text writes **Alfeus** (not Alfeu).

## Dates and numbers
Era: es "7 a. de J.C." / "26 d. de J.C." (as the official text, never "a. C."); fr "7 av. J.-C." / "en 26" or "26 apr. J.-C." where needed;
pt "7 a.C." / "26 d.C.". "A.D. 13, the Daughter of Ezra" → es "13 d. de J.C., la hija de Ezra". Month names in your language; dates in its
usual order ("Saturday, February 23, A.D. 26" → es "el sábado 23 de febrero del año 26 d. de J.C."). Use the official figures for
distances where the official text of that verse gives them (fr uses metric as the official text).

## UI strings and front matter (c01 of each book)
- `ui.title` / `intro.title`: jesus → es "La vida y las enseñanzas de Jesús" · fr "La vie et les enseignements de Jésus" · pt "A vida e os
  ensinamentos de Jesus"; apostles → es "Los doce apóstoles de Jesús" · fr "Les douze apôtres de Jésus" · pt "Os doze apóstolos de Jesus"
  (the same names as `ui.item_life` / `ui.item_apostles` of the Jesus Study hub, without "(in English)").
- `ui.hub` = the menu name (back button "← …"): es "Estudio sobre Jesús" · fr "Étude sur Jésus" · pt "Estudo sobre Jesus".
- `ui.contents` keeps ☰. `ui.ub` = the book title as cited before a source line: es "El libro de Urantia" · fr "Le Livre d’Urantia" ·
  pt "O Livro de Urântia". `ui.chapter` "Chapter {n}" → es "Capítulo {n}" · fr "Chapitre {n}" · pt "Capítulo {n}". `ui.illustration`
  "Illustration: {title}" (image alt text). `ui.toc_about` is a very short label (column of 76 px): es "Acerca" · fr "À propos" · pt "Sobre".
- `intro.meta*` describe the **English** print edition ("English edition · 404 pages"): translate literally (es "Edición inglesa · 404 páginas").
- In the preface the line "“Of all human knowledge …” (196:1.3)" is a quotation unit (automatic); the apostles preface line "“What was poured
  into those ordinary vessels was never ordinary.”" is the author's own sentence: translate it, keeping the quotation marks of your language.

## Style
Faithful, natural, standard written language; same content and order; add nothing, drop nothing. es neutral Spanish. fr 1990 reformed
spelling as the official text (maitre, connaitre, paraitre, aout). pt Brazilian spelling **as the official text** (old orthography: idéia,
conseqüência, freqüente, assembléia, heróico): run `python ..\pt_old_spelling.py pt\<book>\cNN.json` before finishing (it never touches ⟦Q⟧
text). No Korean anywhere; no English left except names and English in parentheses.

## Check and build (coordinator)
    python extract_src.py                                   # only if the Far East English books change (rewrites src/, work/, auto_<l>.json; never <l>/)
    python build_books_am.py es --book jesus --chunk c03    # check one chunk (writes nothing)
    python build_books_am.py es --draft                     # preview both books in _draft_es/<book>/ with English for missing units
    python build_books_am.py es                             # check everything; if clean, writes site/es/jesus-book/, site/es/apostles-book/,
                                                            #   and copies the illustrations once to site/books-img/<book>/ (shared)
    python ..\jesus\build_jesus_am.py es                    # then rebuild the Jesus Study hub: it links to /es/jesus-book/ and
                                                            #   /es/apostles-book/ once those folders exist (else the Far East English books)
Each book page has the site home button (`/home-button.js`, → /<l>/) and a "← Estudio sobre Jesús" button (→ /<l>/jesus/).
`--out <dir>` writes a test build to `<dir>/<l>/<book>/` and `<dir>/books-img/` instead of `site/`.

- es spelling decision (coordinator): write "sólo" (adverb) with the accent as the official text does; "solo" only as adjective.

- apostles es names (from c01–c03, follow them): Andrés, Simón Pedro, Santiago y Juan Zebedeo, Felipe, Natanael, Mateo Leví, Tomás Dídimo, Jacobo y Judas Alfeo (gemelos), Simón el Zelote, Judas Iscariote; Judá/José (hermanos de Jesús), Salomé, Esdras, Noemí, Queriot; "Libertador", "el Maestro", "astillero"; Sources heading "Fuentes de este capítulo"; ch.4 title «El día de la ordenación»; parts: Primera parte: El llamamiento · Segunda parte: Primavera galilea · Tercera parte: Tierras extranjeras y el monte · Cuarta parte: Hacia Jerusalén · Quinta parte: Resurrección y Pentecostés.

- fr (coordinator 11-25): 1990 spelling as the official text: keep circumflex only in masc. singular "sûr"/"mûr"; plurals/feminines without it ("surs", "mures", "sure"). "cent-trentième" hyphenated.

- es apostles (coordinator 11-25): "aposento superior" (official), not "aposento alto".
