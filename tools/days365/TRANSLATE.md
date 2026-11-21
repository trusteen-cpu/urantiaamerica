# days365 menu ("365 Days with The Urantia Book"): translation brief (es / fr / pt)

Read `../SPEC_AM.md` first; everything there applies. Folder: `E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\days365\`.
The English web edition (read only, to see how a page looks): `E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\365days\`.
The menu: one page per day of the year (d001 = January 1 … d365 = December 31). Each page shows the date, the source line,
**the day's Urantia Book passage** (blockquote), a title, a meditation of several paragraphs, and a one-sentence practice ("Today").
Warm, plain devotional prose by Jay Han; about 215,000 English words in 15 chunks.

**You do not translate the daily passage or the source line.** The builder takes the passage verbatim from `../data/<l>.json`
(verses `_ref`) and the source line from the official titles (`../data/<l>_titles.json`). Dates and month names are made by the builder.

## Files
- `work/src_cNN.json`: **your source**, the English units of chunk cNN. Read only. (Same as `src/cNN.json`.)
- `<l>/cNN.json`: **your output**, a JSON object with exactly the same keys, in the same order, every text value translated.
  Write it from a Python script with `json.dump(D, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)`.
  Never put non-ASCII text in a shell heredoc. Keep your own scripts only in `scratch/<l>_cNN/` (create it; nobody else uses it).
  Work in parts: load your output file if it exists, add units, dump it again, and save often.
- `work/ref_<l>_cNN.json`: the day's passage for every day of the chunk, English and official text
  `{"d001": {"ref", "en": [...], "<l>": [...]}}`. When the meditation explains or paraphrases the passage, reuse the official wording.
- `work/inline_<l>_cNN.json`: every inline quotation of the chunk, `{"d001": [{"at", "cit", "en", "auto", "verse"}]}`.
  `at` = `day.field.n` (e.g. `d027.msg[0].1` = first marker in paragraph 0). `auto` = the official text already cut for you
  (whole verse or whole sentences; also in `../days365/auto_<l>.json`), or null. `verse` = the full official verse.
- `work/todo_<l>_cNN.json`: the inline quotations with no `auto`: you must cut these by hand from `verse`.
- Helpers (read only): `python ../amq.py <l> 106:4.2` prints an official verse; `python ../amq.py <l> "?word"` finds verses with a word.
  Glossary: `../glossary/glossary_<l>.json` (list of [English, official term, definition]).
- Check: `python build_days365_am.py <l> --chunk cNN`. It must end with `errors 0`. Read the warnings too (English left behind).

| chunk | days | inline quotations | es auto / hand | fr auto / hand | pt auto / hand |
|---|---|---|---|---|---|
| c01 (+ UI strings) | d001–d025 | 13 | 4 / 9 | 2 / 11 | 3 / 10 |
| c02 | d026–d049 | 68 | 29 / 39 | 28 / 40 | 31 / 37 |
| c03 | d050–d073 | 56 | 24 / 32 | 10 / 46 | 19 / 37 |
| c04 | d074–d098 | 7 | 3 / 4 | 0 / 7 | 1 / 6 |
| c05 | d099–d122 | 0 | – | – | – |
| c06 | d123–d147 | 11 | 3 / 8 | 2 / 9 | 3 / 8 |
| c07 | d148–d172 | 2 | 1 / 1 | 1 / 1 | 1 / 1 |
| c08 | d173–d197 | 11 | 5 / 6 | 1 / 10 | 6 / 5 |
| c09 | d198–d222 | 7 | 2 / 5 | 1 / 6 | 4 / 3 |
| c10 | d223–d246 | 5 | 0 / 5 | 0 / 5 | 1 / 4 |
| c11 | d247–d269 | 17 | 3 / 14 | 1 / 16 | 3 / 14 |
| c12 | d270–d293 | 67 | 16 / 51 | 9 / 58 | 19 / 48 |
| c13 | d294–d318 | 151 | 34 / 117 | 22 / 129 | 33 / 118 |
| c14 | d319–d342 | 109 | 47 / 62 | 26 / 83 | 52 / 57 |
| c15 | d343–d365 | 119 | 36 / 83 | 41 / 78 | 45 / 74 |

## Unit format
```json
"d001": {
 "_ref": "0:5.10",
 "t": "Where the Soul Is Born",
 "msg": ["… a mortal creature chooses to “⟦Q 0:5.10⟧do the will of the Father in heaven,⟦/Q⟧” the indwelling spirit …", "paragraph 2", "..."],
 "pr": "This evening, write down one moment today when you chose to do the will of the Father in heaven."
}
```
- `_ref`: copy **unchanged** (the checker compares it).
- `t`: day title (short, no final period, like a heading).
- `msg`: list of meditation paragraphs. **Same number of items, same order.** Do not merge or split paragraphs. Plain text, no Markdown.
- `pr`: the one-sentence practice (imperative, one sentence, final period).

## Urantia Book quotations inside the meditations: never translate them yourself
Wherever the English quotes the book verbatim, the text is wrapped: `“⟦Q 0:5.10⟧do the will of the Father in heaven,⟦/Q⟧”`.
- `⟦Q cit⟧` … `⟦/Q⟧` (U+27E6 / U+27E7). Keep the markers and the cit exactly; same number of markers, same order, same cits.
- Replace **only the text between the markers** with the corresponding words of the official verse `cit`, **character for character**
  (the checker ignores only whitespace and quotation marks at the ends). If `auto` is given, use it (you may drop a leading « or a trailing
  comma/period to fit your sentence). Otherwise cut it from `verse`: if the English quotes half a sentence, take the same half; if you must
  omit words inside, use ` … ` (space, U+2026, space) — every piece must still be verbatim in that verse, in verse order.
  Example es: `«⟦Q 0:5.10⟧hacer la voluntad del Padre en el cielo⟦/Q⟧»`.
- Quotation marks around the marked text: es « », fr « » (normal space inside; the builder makes it a no-break space), pt “ ”.
  Put them **outside** the markers.
- Build your sentence around the quotation; never reword the quotation to fit the sentence.
- Do not add new markers. Quoted phrases **without** markers (about 30: the author's sample prayers such as “Father, be with me.”, slogans,
  near-quotes of Jesus) are not verbatim book text: translate them normally. When they echo a saying of Jesus that the book contains
  (e.g. d343 “My peace I leave with you…”, d344 “Not my will…”), use the official wording (find it with `amq.py "?word"`).

## Terms (use these everywhere; all fifteen chunks must agree)
| English | es | fr | pt |
|---|---|---|---|
| The Urantia Book (in prose) | El libro de Urantia | le Livre d’Urantia | O Livro de Urântia |
| the Foreword | el Prólogo | l’Introduction | a Introdução |
| Paper 12 / Paper 12, section 3 | documento 12 / documento 12, sección 3 | fascicule 12 / fascicule 12, section 3 | documento 12 / documento 12, seção 3 |
| Universal Father | Padre Universal | Père Universel | Pai Universal |
| Father in heaven | Padre en el cielo | Père qui est aux cieux / Père céleste | Pai no céu / Pai celeste |
| Thought Adjuster / Adjuster | Ajustador del Pensamiento / Ajustador | Ajusteur de Pensée / Ajusteur | Ajustador do Pensamento / Ajustador |
| Mystery Monitor | Monitor Misterioso | Moniteur de Mystère | Monitor Misterioso |
| soul | alma | âme | alma |
| morontia (adj.) | morontial | morontiel(le) | moroncial |
| mansion worlds | mundos de estancia | mondes des maisons | mundos das mansões |
| survival | supervivencia | survie | sobrevivência |
| Paradise ascension | ascensión al Paraíso | ascension au Paradis | ascensão ao Paraíso |
| ascender | ascendente | ascendeur | ascendente |
| Spirit of Truth | Espíritu de la Verdad | Esprit de Vérité | Espírito da Verdade |
| Creator Son / Michael | Hijo Creador / Micael | Fils Créateur / Micaël | Filho Criador / Michael |
| Eternal Son / Infinite Spirit | Hijo Eterno / Espíritu Infinito | Fils Éternel / Esprit Infini | Filho Eterno / Espírito Infinito |
| Mother Spirit / Holy Spirit | Espíritu Materno / Espíritu Santo | Esprit-Mère / Saint-Esprit | Espírito Materno / Espírito Santo |
| Supreme Being | Ser Supremo | Être Suprême | Ser Supremo |
| kingdom of heaven | reino del cielo | royaume des cieux | Reino do céu |
| fatherhood of God / brotherhood of man | paternidad de Dios / hermandad de los hombres | paternité de Dieu / fraternité des hommes | paternidade de Deus / irmandade dos homens |
| sonship / Spirit-born | filiación / nacido del espíritu | filiation / né d’esprit | filiação / nascido do espírito |
| God-consciousness | conciencia de Dios | conscience de Dieu | consciência de Deus |
| fruits of the spirit | frutos del espíritu | fruits de l’esprit | frutos do espírito |
| worship / faith | adoración / fe | adoration / foi | adoração / fé |
| mind / personality | mente / personalidad | mental / personnalité | mente / personalidade |
| guardian seraphim / seraphim | guardianes seráficos / serafines | gardiens séraphiques / séraphins | guardiães seráficos / serafins |
| Lucifer rebellion | rebelión de Lucifer | rébellion de Lucifer | rebelião de Lúcifer |
| Corps of the Finality / finaliter | Cuerpo de la Finalidad / finalista | Corps de la Finalité / finalitaire | Corpo de Finalidade / finalitor |
| agondonter | agondonter | agondontaire | agondonteiro |
| Melchizedek / Nebadon / Salvington / Urantia | Melquisedek / Nebadon / Salvington / Urantia | Melchizédek / Nébadon / Salvington / Urantia | Melquisedeque / Nébadon / Sálvington / Urântia |
Anything else: glossary first, then `amq.py "?word"`. Never invent a term the official translation already has. When a meditation
discusses the day's passage, reuse the exact words the official passage (`work/ref_<l>_cNN.json`) uses for the same idea.
Pronoun for God / the Adjuster: masculine (es Él, fr Il, pt Ele, capitalized as the official text does).

## UI strings (chunk c01, keys `ui.*`)
Flat strings; translate all of them. Keep `{n}` where it is.
- `ui.page_title`: es `365 días con El libro de Urantia` · fr `365 jours avec le Livre d’Urantia` · pt `365 dias com O Livro de Urântia`. Use the same title everywhere.
- `ui.subtitle`, `ui.og_description`, `ui.meta_description`: translate.
- `ui.prev` / `ui.next`: keep the arrows (es `‹ Anterior` / `Siguiente ›`, fr `‹ Précédent` / `Suivant ›`, pt `‹ Anterior` / `Próximo ›`).
- `ui.today_button` (button that jumps to today) and `ui.practice_label` (label on the practice bar, shown in capitals): es `Hoy` · fr `Aujourd’hui` · pt `Hoje`.
- `ui.day_label`: must contain `{n}` (replaced by 001…365): es `DÍA {n}` · fr `JOUR {n}` · pt `DIA {n}`.
- `ui.paper_label`: source line before the official paper title: es `Documento {n}` · fr `Fascicule {n}` · pt `Documento {n}`.
- `ui.cite_prefix`: es `— El libro de Urantia` · fr `— Le Livre d’Urantia` · pt `— O Livro de Urântia` (the builder adds a space and the reference).
- `ui.open_in_book`: tooltip of the reference link ("Open in The Urantia Book").
- `ui.about_html`: may contain `<i>…</i>` around the book title. It already says the quotations are reproduced word for word from the official
  translation published by Urantia Foundation (fr Fondation Urantia); keep that meaning.
- `ui.aria_*`, `ui.loading`, `ui.toc_summary` ("All 365 days"), `ui.load_error`: translate.
- Not translated (made by the builder): month names, dates (es "1 de enero", fr "1er janvier", pt "1º de janeiro"), the separator before a title.

## Style
Devotional, warm, clear, standard written language; no preaching beyond the English; same content and order; add nothing, drop nothing.
Book title in prose as in the term table (plain text). es neutral Spanish (tú/usted: follow the English "you" with **tú** for the reader,
consistently). fr 1990 reformed spelling as the official text (connaitre, paraitre, maitre, ile, aout); « » with a normal space inside and a
normal space before ; : ! ? (the builder turns them into no-break spaces, never inside quotations). pt Brazilian spelling **as the official
text** (old orthography: idéia, conseqüência, freqüente, assembléia, heróico; check doubtful words with amq), "você" for the reader.
Numbers: as the English (words stay words). No Korean anywhere; no English left except names and English in parentheses.
