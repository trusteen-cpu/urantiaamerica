# cosmology menu ("A Commentary on A Study of the Master Universe"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology\`.
The English web edition you are translating (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\cosmology\`.
The book: Jay Han's calm, explanatory commentary on William S. Sadler, Jr.'s *A Study of the Master Universe*: Preface, Notes for the Reader,
colophon, 18 chapters and 27 appendix chapters, 67 figures (the figures stay English images; only their captions are translated).

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN (block quotations are not in it). Read only.
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys in the same order and every value translated.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts: load your output file if it exists, add units, dump it again, and save often.
- `<l>/quotes_cNN.json`: **your second output**, the block quotations the automatic aligner could not cut.
  They are listed in `work/todo_<l>_cNN.json` as `{"w03.045": {"cit", "en", "why"}}`. Write `{"w03.045": "official text cut verbatim", ...}`,
  one entry per todo key, with the key copied exactly. (All other block quotations are already filled automatically from `auto_<l>.json`; do not touch them.)
- `work/inline_<l>_cNN.json`: the short quotations inside prose (see below), with the full official verse for each, as a convenience.
- Helpers (read only):
  - `python ../amq.py <l> 106:4.2` prints an official verse. `python ../amq.py <l> "?absonit"` finds verses that contain a word (use it to confirm terms).
  - Glossary: `../glossary/glossary_<l>.json` is a list of [English, official term, definition]. Search it with Python.
- Check: `python build_cosmology_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (they flag English left behind).

## Unit format (values in work/src_cNN.json)
1. **String**: a paragraph, a `##`/`###` heading, a list item, a box title, a table caption, a figure caption, a chapter or appendix title
   (title only; the builder adds the "Chapter N" label), or the "Original:" line under a title (only the part after "Original:", which is
   Sadler's original section name; translate it, then the English title in parentheses is not needed).
   Keep light Markdown: `**bold**` and `*italic*`. Do not put `|` in strings (it breaks figures and tables).
2. **List of strings**: one table row, one string per cell. Keep the same number of cells. The first row of each table is the header row.

Inline citations in prose such as `[106:7.5]` or `(106:6.3; 106:7.4)` stay exactly as they are written (ASCII brackets, same numbers).
Page references to Sadler's study, such as "(orig. p. 38)" / "(orig. pp. 1–2)", become es "(orig., p. 38)" / "(orig., pp. 1–2)",
fr "(orig., p. 38)", pt "(orig., p. 38)" / "(orig., pp. 1–2)".

## Urantia Book quotations: never translate them yourself
**Block quotations you cut (quotes_cNN.json).** The English cut is whole English sentences (pieces joined by an ellipsis). The official verse
splits or joins sentences differently, so the aligner gave up (`why`). Take the official words that correspond to each English piece
**character for character** (copy them from `amq.py` output; the checker ignores only whitespace), and join pieces with ` … ` (space, U+2026, space)
in verse order. If the English piece is part of a sentence, cut the official sentence at the corresponding clause boundary; if that is not clean,
take the whole official sentence. If one English sentence is two official sentences, take both. Keep the omissions the English has. A range such as
`12:6.9–12` means paragraphs 12:6.9 to 12:6.12; the checker searches their joined text. Do not add quotation marks around the quotation.

**Inline quotations** (short phrases quoted in prose with a citation) are marked `"⟦Q 0:3.24⟧Father-Infinite⟦/Q⟧" [0:3.24]`.
Keep the markers and the citation inside the opening marker exactly. Replace only the text between the markers with the verbatim official words from
that verse (see `work/inline_<l>_cNN.json`), e.g. es `«⟦Q 0:3.24⟧…official words…⟦/Q⟧» [0:3.24]`. Change the surrounding quotation marks to
es « », fr « » (with spaces inside), pt “ ”. The checker verifies the text between the markers. Adjust the sentence grammar around it if needed.
Quoted phrases without a citation are not checked; still use the official wording when you can find it with `amq.py "?word"`.

## Terms (use these everywhere; all eight chunks must agree)
| English | es | fr | pt |
|---|---|---|---|
| master universe | universo maestro | maitre univers | universo-mestre |
| grand universe | gran universo | grand univers | grande universo |
| central universe | universo central | univers central | universo central |
| superuniverse | superuniverso | superunivers | superuniverso |
| outer space (levels) | (niveles del) espacio exterior | (niveaux de l’)espace extérieur | (níveis do) espaço exterior |
| absonite | absonito | absonite | absonito |
| eventuate / eventuation | eventuar / eventuación | s’extérioriser / extériorisation | emergir / emergência (check amq "?emerg" and "?derivad") |
| experiential / existential | experiencial / existencial | expérientiel / existentiel | experiencial / existencial |
| Supreme Being | Ser Supremo | Être Suprême | Ser Supremo |
| God the Supreme / Ultimate / Absolute | Dios el Supremo / el Último / el Absoluto | Dieu le Suprême / l’Ultime / l’Absolu | Deus, o Supremo / o Último / o Absoluto |
| God the Sevenfold | Dios el Séptuple | Dieu le Septuple | Deus, o Sétuplo |
| Deity Absolute | Absoluto de Deidad | Absolu de Déité | Absoluto da Deidade |
| Universal / Unqualified Absolute | Absoluto Universal / Absoluto No Cualificado | Absolu Universel / Absolu Non Qualifié | Absoluto Universal / Absoluto Inqualificável |
| Paradise Trinity | Trinidad del Paraíso | Trinité du Paradis | Trindade do Paraíso |
| Trinity of Trinities | Trinidad de Trinidades | Trinité des Trinités | Trindade das Trindades |
| Architects of the Master Universe | Arquitectos del Universo Maestro | Architectes du Maitre Univers | Arquitetos do Universo-Mestre |
| Isle of Paradise | Isla del Paraíso | Ile du Paradis | Ilha do Paraíso |
| the I AM | el YO SOY | le JE SUIS | o EU SOU |
| Supreme-Ultimate | Supremo-Último | Suprême-Ultime | Supremo-Último |
| Seven Master Spirits | Siete Espíritus Rectores | Sept Maitres Esprits | Sete Espíritos Mestres |
| Ancients of Days | Ancianos de los Días | Anciens des Jours | Anciães dos Dias |
| Corps of the Finality / finaliters | Cuerpo de la Finalidad / finalistas | Corps de la Finalité / finalitaires | Corpo de Finalidade / finalitores |
| pervaded / unpervaded space / midspace | espacio ocupado / desocupado / espacio intermedio | espace pénétré / non pénétré / espace intermédiaire | espaço preenchido / não-preenchido / espaço intermediário |
| force-charge | carga de fuerza | charge-force | carga-força |
| ultimaton | ultimatón | ultimaton | ultímaton |
| Andronover | Andronóver | Andronover | Andronover |
| Transcendentalers | Trascendentales | (check amq "?Transcendant") | (check amq "?Transcendent") |
Anything else: glossary first, then `amq.py "?word"`. Never invent a term the official translation already has.

Sadler's own terms (not in The Urantia Book): translate by meaning, give the English in parentheses at the first mention in each chapter only
if it helps, and use them consistently: Zero Age → es Edad Cero / fr Âge Zéro / pt Idade Zero; universe age(s) → edad(es) del universo /
âge(s) de l’univers / idade(s) do universo; nuclear / cytoplasmic universes → universos nucleares / citoplásmicos, univers nucléaires /
cytoplasmiques, universos nucleares / citoplasmáticos; Andronover Time Unit → Unidad de Tiempo de Andronóver / Unité de temps d’Andronover /
Unidade de Tempo de Andronover; Sadler's Cosmos Infinite (capitalized) → Cosmos Infinito / Cosmos Infini / Cosmos Infinito; thesis / antithesis /
synthesis → tesis / antítesis / síntesis, thèse / antithèse / synthèse, tese / antítese / síntese.
Box titles: "Sadler and the Text" → es Sadler y el texto · fr Sadler et le texte · pt Sadler e o texto; "Sadler’s inference" → es La inferencia de Sadler ·
fr L’inférence de Sadler · pt A inferência de Sadler. William S. Sadler, Jr. keeps his name. Sadler's book title stays in English, in italics:
*A Study of the Master Universe*.

## Book title, UI strings and front matter (chunk c01 only)
- `ui.title`: es "Comentario a *A Study of the Master Universe*" is not allowed (no Markdown in UI). Use plain text:
  es `Comentario a A Study of the Master Universe` · fr `Commentaire de A Study of the Master Universe` · pt `Comentário sobre A Study of the Master Universe`.
  Use the same title in the Preface and colophon (there in italics around the English part where the English uses italics).
- `ui.sub`: translate, e.g. es "Una lectura del estudio de William S. Sadler, Jr. sobre el universo maestro de El libro de Urantia".
- `ui.by`: "Jay Han". `ui.eb`: es "COSMOLOGÍA DE EL LIBRO DE URANTIA" · fr "COSMOLOGIE DU LIVRE D’URANTIA" · pt "COSMOLOGIA DE O LIVRO DE URÂNTIA".
- `ui.chapter_label`: es "Capítulo {n}" · fr "Chapitre {n}" · pt "Capítulo {n}". `ui.appendix_label`: es "Apéndice {roman}" · fr "Annexe {roman}" · pt "Apêndice {roman}".
- `ui.orig` "Original: {t}" → es "Original: {t}" · fr "Original : {t}" · pt "Original: {t}".
- `ui.part1` / `ui.part2` keep **two spaces** between the part number and its name (es "Primera parte  El texto principal").
- `ui.fig_label`, `ui.tab_label`, `ui.summ` ("IN THIS CHAPTER", capitals), `ui.points` ("Key Points"), `ui.prev`/`ui.next` keep the arrows.
- The colophon and Notes say quotations are given in the original English. Say instead that quotations from the book are reproduced word for word from
  the official Spanish/French/Portuguese translation published by Urantia Foundation (fr Fondation Urantia), each followed by its reference
  (es documento:sección.párrafo, fr fascicule:section.paragraphe, pt documento:seção.parágrafo), and that clicking a reference opens the text.
  This edition fact is the only allowed addition.

## Style
Faithful, natural, standard written language; calm explanatory tone; same content and order; add nothing, drop nothing.
Book title in prose: es *El libro de Urantia*, fr *le Livre d’Urantia*, pt *O Livro de Urântia* (as plain text, as the English writes it).
"Paper 57" → es "documento 57", fr "fascicule 57", pt "documento 57"; "the Foreword" → es "el Prólogo", fr "l’Introduction", pt "a Introdução".
es neutral Spanish. fr 1990 reformed spelling as the official text (maitre, ile, connaitre, paraitre); « » with a normal space inside and a normal
space before ; : ! ? (the builder turns it into a no-break space). pt Brazilian spelling as the official text (check doubtful words with amq).
Numbers in words stay words. No Korean anywhere; no English left except Sadler's book title, names, and English in parentheses.

## Sadler's terms fixed during the Spanish edition (fr / pt must use these forms in every chunk)
| English | es (done) | fr | pt |
|---|---|---|---|
| Primary … Quartan Space Level | Nivel Espacial Primario … Cuartano | niveau d’espace primaire / secondaire / tertiaire / quaternaire | Nível Espacial Primário / Secundário / Terciário / Quaternário |
| Master Architects | Arquitectos Maestros | Maitres Architectes | Arquitetos Mestres |
| Master Son / Master Michael(s) | Hijo Mayor / Micael(es) Mayor(es) | (fr: amq "?Fils" in 21:6) Micaël(s) Maitre(s) | Filho Mestre / Michael(s) Mestre(s) |
| God the Sevenfold | Dios el Séptuple | Dieu le Septuple | Deus, o Sétuplo |
| Majeston | Majeston | Majeston | Majeston |
| Finite / Absonite / Final Story (Sadler's three stories) | Historia Finita / Absonita / Final | Histoire finie / absonite / finale | História Finita / Absonita / Final |
| Final Age | Edad Final | Âge Final | Idade Final |
| Supreme / Ultimate / Absolute Adventure | Aventura Suprema / Última / Absoluta | Aventure Suprême / Ultime / Absolue | Aventura Suprema / Última / Absoluta |
| Barrier of Infinity / Impasse of the Absolutes | Barrera de la Infinidad / Impasse de los Absolutos | Barrière de l’Infini / Impasse des Absolus | Barreira da Infinitude / Impasse dos Absolutos |
| Limited-Absolute | Absoluto-Limitado | Absolu-Limité | Absoluto-Limitado |
| eternal / eternaler / eternalest | eterno / más eterno / el más eterno | éternel / plus éternel / le plus éternel | eterno / mais eterno / o mais eterno |
| post-supreme / post-ultimate | post-supremo / post-último | post-suprême / post-ultime | pós-supremo / pós-último |
| Andronover Time Unit (ATU) | Unidad de Tiempo de Andronóver (UTA) | Unité de temps d’Andronover (UTA) | Unidade de Tempo de Andronover (UTA) |
| Son-Spirit Creative Trio(s) / Associate Creator | Trío(s) Creativo(s) Hijo-Espíritu / Creador Asociado | Trio(s) Créatif(s) Fils-Esprit / Créateur Associé | Trio(s) Criativo(s) Filho-Espírito / Criador Associado |
| quiet zones / quiet times | zonas / tiempos de quietud | zones / temps de quiétude | zonas / tempos de quietude |
| Dual-Deity | Deidad Dual | Déité Duelle | Deidade Dual |
| Processional of Initiative | Procesión de la Iniciativa | Procession de l’Initiative | Procissão da Iniciativa |
| Afterword / Epilogue / Sadler's own Foreword | Posfacio / Epílogo / prefacio (the UB Foreword stays el Prólogo) | Postface / Épilogue / avant-propos (UB Foreword = l’Introduction) | Posfácio / Epílogo / prefácio (UB Foreword = a Introdução) |
| Undivided Deity, Inc. (mock company) | Deidad Indivisa, Sociedad Anónima | Déité Indivise, Société Anonyme | Deidade Indivisa, Sociedade Anônima |
Large numbers follow the language's own scale (trillion = es/fr/pt billón / billion / trilhão — check: pt Brazilian "trilhão" = 10^12; fr "billion" = 10^12) and decimal comma.
If the English note is about English spelling (e.g. the hyphen in "cosmos-infinite"), keep the English form in parentheses so the remark still makes sense.
