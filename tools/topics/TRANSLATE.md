# Topical Studies (menu id `topics`): translation brief (es / fr / pt)

Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\topics\` (below: `topics/`).
Read `../SPEC_AM.md` too; everything there applies.

## What the menu is
100 topics (Universal Father … Quest for Perfection). Each topic = name, overview (`sum`), 3–7 sections with a short
heading, and items under each heading. An item is either an editor's **summary sentence** (translate it) or a
**quotation** from The Urantia Book (never translate; cut verbatim from the official translation; handled separately).

## Files
- `src/c01.json` … `src/c10.json` — English prose units, 10 topics per chunk (c01 = topics 1–10, …). Read only.
  Keys: `tNNN.t` (name) · `tNNN.sum` (overview) · `tNNN.sK.h` (section heading) · `tNNN.sK.iJ` (summary item).
  Quotation items are NOT in these files (they live in `src/quotes.json`).
- `names.py` — the 100 topic names in es/fr/pt, fixed. **Do not translate `tNNN.t`; you may omit those keys.**
  When prose mentions another topic by name, use the same term.
- Prose translators write `<l>/cNN.json` (`es/c01.json`, `fr/c07.json`, …): same keys as `src/cNN.json`
  (all except `tNNN.t`), string values in the target language. Nothing added, nothing missing.
  Write it with Python `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)` from a
  script file made with the Write tool, or with the Write tool directly. Never put non-ASCII in a shell heredoc.
- Quotations: `align_quotes.py` already cut 70% automatically (`auto_<l>.json`). The rest are in
  `work/todo_<l>.json` {key: {cit, en_quote, en_verse, verse}}. Quotation workers write `<l>/quotes_<part>.json`
  {key: "verbatim official text"} (see "Quotations" below).
- `build_topics_am.py` merges everything, checks, and writes `site/<l>/topics/`. `python build_topics_am.py es --draft`
  previews with English where missing; without `--draft` it refuses to write if any check fails.

## Terminology (official Urantia Foundation translations)
- Look terms up in the official text: `python ../amq.py <l> 1:0.1` (show a verse), `python ../amq.py <l> "?Ajustador"`
  (verses containing a word). Best method: find the English verse cited in the item (`E:\OneDrive\유란시아 작업\theology-book\en.json`),
  read the same verse number in `../data/<l>.json`, and reuse its wording. Glossary of official terms:
  `../glossary/glossary_<l>.json` = list of [English, official term, definition].
- Fixed: es Padre Universal, Hijo Eterno, Espíritu Infinito, Trinidad del Paraíso, Ser Supremo, Dios el Séptuple, Dios el Último,
  Ajustador del Pensamiento, morontial / morontia, Hijo Creador, **Micael** de Nebadon, Espíritu Materno del Universo Local,
  Espíritus Rectores, Ancianos de los Días, los Melquisedek (plural invariable), Hijos Avonales, Hijos Instructores Trinitarios,
  seres intermedios, Portadores de Vida, Hijos Materiales, finalistas, Cuerpo de la Finalidad, mundos de estancia,
  espíritus ayudantes de la mente, Espíritu de la Verdad, reino del cielo, hermandad de los hombres, filiación con Dios,
  autootorgamiento, luz y vida, Maquiventa Melquisedek, Lucifer, Caligastia, Adán y Eva, supervivencia, mente cósmica,
  huestes angélicas, Jerusem, Satania, Edentia, Salvington, Uversa, Orvonton, Urantia.
- Fixed: fr Père Universel, Fils Éternel, Esprit Infini, Trinité du Paradis, Être Suprême, Dieu le Septuple, Dieu l’Ultime,
  Ajusteur de Pensée, morontiel / morontia, Fils Créateur, **Micaël** de Nébadon, Esprit-Mère de l’univers local,
  Maitres Esprits, Anciens des Jours, Melchizédeks, Fils Avonals, Fils Instructeurs de la Trinité, médians, Porteurs de Vie,
  Fils Matériels, finalitaires, Corps de la Finalité, mondes des maisons, esprits-mentaux adjuvats, Esprit de Vérité,
  royaume des cieux, fraternité des hommes, filiation avec Dieu, effusion, lumière et vie, Machiventa Melchizédek,
  gardiens séraphiques, survie, mental (the mind = « le mental »), mental cosmique, armées angéliques, Jérusem, Satania,
  Édentia, Salvington, Uversa, Orvonton. **1990 reformed spelling** as in the official text: maitre, ile, connaitre, paraitre, aout.
- Fixed: pt Pai Universal, Filho Eterno, Espírito Infinito, Trindade do Paraíso, Ser Supremo, Deus, o Sétuplo, Deus, o Último,
  Ajustador do Pensamento, moroncial / morôncia, Filho Criador, **Michael** de Nébadon, Espírito Materno do Universo Local,
  Espíritos Mestres, Anciães dos Dias, Melquisedeques, Filhos Avonais, Filhos Instrutores da Trindade, criaturas intermediárias,
  Portadores da Vida, Filhos Materiais, finalitores, Corpo de Finalidade, mundos das mansões, espíritos ajudantes da mente,
  Espírito da Verdade, Reino do céu, irmandade dos homens, filiação a Deus, auto-outorga, luz e vida, Maquiventa Melquisedeque,
  Lúcifer, Caligástia, Adão e Eva, sobrevivência, mente cósmica, hostes angélicas, Jerusém, Satânia, Edêntia, Sálvington,
  Uversa, Orvônton, Urântia. Brazilian spelling.
- Jesus' names and Bible people: use the official text's forms (es Juan el Bautista, Simón Pedro; fr Jean le Baptiste, Simon Pierre;
  pt João Batista, Simão Pedro — check with amq).
- Book title: es *El libro de Urantia*, fr *le Livre d’Urantia*, pt *O Livro de Urântia*.
- God pronoun: lower case as in the official text (él / il / ele).

## Style
- Plain expository written language, the tone of a study handbook: faithful to the English, concise, factual, no sermon,
  no additions or omissions. Summary items stay one sentence each, ending with a period. Overviews (`sum`) keep their
  sentence count. Headings: short noun phrases, no final period, sentence case (capital only on the first word and on
  official proper terms).
- Neutral Spanish (readable in Latin America), « » quotation marks; French: « » with a space inside and a space before ; : ! ?
  (normal space is fine); Portuguese (Brazil): “ ”.
- English words in double quotes inside a summary (e.g. "Father") are usually the book's words: use the official text's
  wording for them (check the cited verse).
- No Korean, no English left (except proper names that the official text leaves in English).
- Numbers in the language's convention (es/pt 1.000; fr 1 000), as the official text writes them.

## Quotations (quotation workers only)
- For each key in your part of `work/todo_<l>.json`: compare `en_quote` with `en_verse`, find the corresponding span in
  `verse` (the official translation of the same paragraph), and copy it **character for character** (same punctuation,
  quotation marks, dashes, capitalization). Same extent as the English: whole sentence(s) for whole sentence(s),
  a clause for a clause. If the English cut starts mid-sentence (lower case), start the translation at the matching
  point; if it ends mid-sentence (no final period), stop at the matching point without adding a period.
- If the corresponding text is not contiguous in the translation (word order differs), give the smallest contiguous span
  that covers the meaning — or join verbatim pieces in order with ` … `. Never write words that are not in `verse`.
- Check: `python -c "import sys; sys.path.insert(0, r'..'); import amq; print(amq.check('es', '1:2.1', 'quote'))"` must be True.
  Easiest: write a small Python script that loads your output and asserts `amq.check(l, cit, q)` for every key.
