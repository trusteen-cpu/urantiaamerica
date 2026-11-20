# qna menu ("A Thousand Questions and Answers"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\qna\`.

## Files
- `work_<l>/src_cNN.json` — **your source** (English units of chunk cNN; inside the `⟦Q⟧` markers the official
  translation is already filled in where it could be cut automatically). Do not edit.
- `<l>/cNN.json` — **your output**: a JSON object with exactly the same keys in the same order, translated values.
  Write it from a Python script: `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Put your own scripts only in `scratch/<l>_cNN/` (create it; nobody
  else uses that folder). Load your output file if it exists, add/replace units, dump again (save after every few units).
- Helpers (read only): `python show_q.py <l> cNN` lists the quotations of your chunk (English quote, English verse,
  official verse); `python show_q.py <l> term "Adjuster"` looks up the glossary `../glossary/glossary_<l>.json`
  ([English, official term, definition]); `python ../amq.py <l> 45:4.2` prints an official verse;
  `python ../amq.py <l> "?Ajustador"` finds verses containing a word (to confirm an official term).
- Check: `python build_qna_am.py <l> --chunk cNN --report 200` — must end with `errors 0`.

## Unit format
`"q027": {"question": "...", "answer": "..."}` — translate both. c01 also has `ui.*` strings (see below).
A long answer is easiest built from a Python list of paragraphs joined with `"\n\n"`.

## Structure the checker enforces
- same keys; `question`/`answer` non-empty;
- same number of paragraphs (`\n\n`) as the English; keep single `\n` line breaks too;
- every `N:M.K` reference of the English still present — keep brackets exactly: `[45:4.2, 45:4.5]`, `[78:6.1-78:6.5]`;
- same number of `**` bold markers; bullets and symbols (• ● ○ ━ ① → 💡 ※) stay as they are;
- numbered headings keep ASCII digit + period + space: `1. Introducción`, `2.1 …`;
- no Korean; no English left (the checker counts English function words such as "the/and/of/which").

## Urantia Book quotations — never translate them yourself
1. `⟦P 100:6.7⟧` — whole paragraph, filled by the builder. **Copy the token unchanged** (and the numbers before it).
2. `⟦Q 37:8.2⟧…⟦/Q⟧` — a verbatim quotation of (part of) that verse. Keep the marker with its citation.
   - If the source already has official-language text inside (pre-cut): keep it exactly.
   - If it still has English inside (`show_q.py` says TO CUT BY YOU): replace the English with the matching words cut
     **character for character** from the official verse (`show_q.py` prints it). If the English is a partial phrase,
     cut the corresponding partial phrase of the official sentence (it may be worded differently — take the official
     words that carry that meaning, contiguous). Where the English omits words (`...` / `…`) put ` … ` between pieces.
     Leave out the official text's own outer quotation marks/guillemets if they would be cut in half.
   - Put your language's quotation marks outside the marker: es «⟦Q k⟧…⟦/Q⟧» , fr « ⟦Q k⟧…⟦/Q⟧ » , pt “⟦Q k⟧…⟦/Q⟧”.
   - Make the surrounding sentence fit the official wording grammatically.
   The checker verifies every quotation with `amq.check` (only whitespace and ` … ` omissions are tolerated).
3. Unmarked quoted words ("Nephilim", "the spirit of worship", etc.) are terms or paraphrases: translate them with the
   official term (glossary / `amq.py "?word"`) and put them in your quotation marks. Not checked.

## Terms and conventions
- Always the official terms (glossary_<l>.json / `<l>.json`): es Padre Universal, Hijo Eterno, Espíritu Infinito,
  Ajustador del Pensamiento, Ser Supremo, morontial, mundos de estancia, Hijo Creador, Espíritu Madre, Micael (never
  Miguel); fr Père Universel, Fils Éternel, Esprit Infini, Ajusteur de Pensée, Être Suprême, morontiel, mondes des maisons,
  Fils Créateur, Micaël; pt Pai Universal, Filho Eterno, Espírito Infinito, Ajustador do Pensamento, Ser Supremo,
  moroncial, mundos das mansões, Filho Criador, Michael. Check the glossary when unsure — do not invent.
- Book title: es *El libro de Urantia*, fr *le Livre d’Urantia*, pt *O Livro de Urântia* (plain text). "the text" / "the
  book" meaning the Urantia Book → es "el libro", fr "le Livre", pt "o livro" (or the full title).
- "Paper 57" → es "documento 57", fr "fascicule 57", pt "documento 57"; `[Paper 45]` → `[Documento 45]` / `[Fascicule 45]` /
  `[Documento 45]`; "section 3" → es "sección 3", fr "section 3", pt "seção 3"; the Foreword → es "el Prólogo",
  fr "l’Introduction", pt "a Introdução". Paper titles if named: `../data/<l>_titles.json`.
- Dates: "8000 B.C." → es "8000 a. C.", fr "8000 av. J.-C.", pt "8000 a.C."; numbers with the language's usual
  separators where the English has them (e.g. es/pt 200.000, fr 200 000); "65%" stays (fr "65 %").
- Bible references in parentheses (e.g. "(John 3:16)") → book names in your language (es Juan, fr Jean, pt João).
- es: neutral Spanish, formal "usted" if a "you" occurs. fr: 1990 reformed spelling as the official text (maitre, ile,
  connaitre, aout, paraitre, surement), « » with a normal space inside, space before ; : ! ? (the builder does not change it).
  pt: Brazilian spelling as the official text.
- Plain explanatory prose; same content and order; add nothing, drop nothing.
- No `<`, `>`, backtick or `${` (unless the English already has them).

## UI strings (chunk c01 only; keep `{n}`, `{badge}`, `{question}`)
| key | es | fr | pt |
|---|---|---|---|
| ui.page_title | Mil preguntas y respuestas — El libro de Urantia | Mille questions et réponses — le Livre d’Urantia | Mil perguntas e respostas — O Livro de Urântia |
| ui.og_description | Preguntas y respuestas sobre El libro de Urantia | Questions et réponses sur le Livre d’Urantia | Perguntas e respostas sobre O Livro de Urântia |
| ui.h1 | Mil preguntas y respuestas | Mille questions et réponses | Mil perguntas e respostas |
| ui.sub | Preguntas y respuestas sobre El libro de Urantia — elija una pregunta a la izquierda | Questions et réponses sur le Livre d’Urantia — choisissez une question à gauche | Perguntas e respostas sobre O Livro de Urântia — escolha uma pergunta à esquerda |
| ui.search_placeholder | Buscar una pregunta (número o palabra) | Chercher une question (numéro ou mot) | Buscar uma pergunta (número ou palavra) |
| ui.loading | Cargando… | Chargement… | Carregando… |
| ui.back | ← Todas las preguntas | ← Toutes les questions | ← Todas as perguntas |
| ui.empty | Aún no hay preguntas. | Pas encore de questions. | Ainda não há perguntas. |
| ui.badge | P {n} | Q {n} | P {n} |
| ui.count | {n} preguntas | {n} questions | {n} perguntas |
| ui.found | {n} encontradas | {n} trouvées | {n} encontradas |
| ui.prev | ← Anterior {badge} | ← Précédente {badge} | ← Anterior {badge} |
| ui.next | Siguiente {badge} → | Suivante {badge} → | Próxima {badge} → |
| ui.load_error | No se pudieron cargar las preguntas. | Impossible de charger les questions. | Não foi possível carregar as perguntas. |
| ui.title_form | P {n}. {question} | Q {n}. {question} | P {n}. {question} |
