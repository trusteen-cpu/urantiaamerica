# -*- coding: utf-8 -*-
# 「유란시아서 요약본」(The Urantia Book, Abridged) 스페인어·프랑스어·포르투갈어판 → site/<l>/abridged/
#   극동판 tools/zh/abridged/build_abridged_zh.py 를 옮긴 것. 영어판 site/en/abridged/ 의 index.html·meta.js·c*.js 를
#   읽기만 하고(고치지 않음), 블록 구조(종류·순서·'own' 표시)는 그대로 두고 글자만 번역으로 바꾼다.
#   원고: src/cNN.json (영어 단위, extract_src.py)
#        + <l>/cNN.json (번역: 인용 상자 .q 를 뺀 모든 단위, 같은 키)
#        + 인용 상자 .q: auto_<l>.json (prep.py 자동) 또는 <l>/quotes_cNN.json (손으로 자른 것, 이쪽이 우선)
#   검사: 키 누락·남는 키·구조·빈 값·한글·⟦Q⟧ 표시·자리표시자·인용(tools/data/<l>.json 원문 그대로, 공백만 무시)·영어 잔재(경고)
#        — 하나라도 어긋나면 쪽을 만들지 않는다.
#   python build_abridged_am.py es [fr pt]          검사 + 통과 시 site/<l>/abridged/ 빌드
#   python build_abridged_am.py es --chunk c03      그 묶음만 검사 (쓰지 않음)
#   python build_abridged_am.py es --draft          빠진 단위는 영어로 채워 tools/abridged/_draft_<l>/ 에 미리보기
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
EN_DIR = os.path.join(FE, "site", "en", "abridged")
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]

CHUNKS = [c["id"] for c in json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))]
EN, CH = {}, {}
for c in CHUNKS:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    EN.update(d); CH.update({k: c for k in d})
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their|who|what)\b")
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", re.S)
ANYMARK = re.compile(r"⟦/?Q[^⟧]*⟧")
nows = lambda s: re.sub(r"\s+", "", s.replace("\u00a0", " "))
strip_marks = lambda s: ANYMARK.sub("", s)
QUOTES = {"es": ("«", "»"), "fr": ("«\u00a0", "\u00a0»"), "pt": ("“", "”")}


def strings(v):
    return [x for r in v for x in r] if isinstance(v, list) else [v]


def fr_nb(s):
    """French no-break spaces, applied only outside ⟦Q⟧…⟦/Q⟧ (never inside quotations)."""
    def f(t):
        t = re.sub(r" ([;:!?»])", "\u00a0\\1", t)
        return t.replace("« ", "«\u00a0")
    out, pos = [], 0
    for m in MARK.finditer(s):
        out.append(f(s[pos:m.start()])); out.append(m.group(0)); pos = m.end()
    out.append(f(s[pos:]))
    return "".join(out)


def box_parts(v):
    """English .q unit → (pre, cits, inner, post)."""
    m = MARK.search(v)
    return v[:m.start()], m.group(1), m.group(2), v[m.end():]


def load(l):
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    T = {}
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    for c in CHUNKS:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        elif not CHUNK and not DRAFT: print(f"  [missing file] {l}/{c}.json")
        hand = {}
        p = os.path.join(H, l, f"quotes_{c}.json")
        if os.path.exists(p): hand = json.load(open(p, encoding="utf-8"))
        for k in hand:
            if CH.get(k) != c or not k.endswith(".q"): print(f"  ERR quotes_{c}.json has a key that is not a quotation box of {c}: {k}")
        for k in (x for x in EN if CH[x] == c and x.endswith(".q")):
            q = hand.get(k, auto.get(k))
            if q is not None: T[k] = q
    return BOOK, T


def quote_cit(BOOK, text, cits):
    """the first candidate verse that contains every piece of text verbatim (whitespace ignored), else None."""
    pieces = [nows(p).strip("“”\"'‘’«»") for p in re.split(r"…|\.\.\.", text)]
    pieces = [p for p in pieces if p]
    if not pieces: return None
    for c in cits.split("|"):
        if c in BOOK:
            hay = nows(BOOK[c])
            if all(p in hay for p in pieces): return c
    return None


def check(l, BOOK, T, LINK):
    errs, warns, badq, nq = [], [], [], 0
    for k, ev in EN.items():
        if CHUNK and CH[k] != CHUNK: continue
        if k not in T: errs.append(f"missing: {k}"); continue
        tv = T[k]
        if k.endswith(".q"):
            nq += 1
            if not isinstance(tv, str) or not tv.strip(): errs.append(f"quotation box empty or not a string: {k}"); continue
            if HANGUL.search(tv): errs.append(f"hangul: {k}")
            if "⟦" in tv: errs.append(f"quotation box must hold only the official text (no markers): {k}")
            _, cits, inner, _ = box_parts(ev)
            c = quote_cit(BOOK, tv, cits)
            if c: LINK[k] = c
            else: badq.append(f"{k} [{cits}] {tv[:60]}")
            continue
        if isinstance(ev, list):
            if not (isinstance(tv, list) and len(tv) == len(ev) and all(isinstance(r, list) and len(r) == len(r0) for r, r0 in zip(tv, ev))):
                errs.append(f"table shape differs: {k}"); continue
        elif not isinstance(tv, str): errs.append(f"not a string: {k}"); continue
        for es_, ts in zip(strings(ev), strings(tv)):
            if not isinstance(ts, str): errs.append(f"not a string: {k}"); break
            if es_.strip() and not ts.strip(): errs.append(f"empty: {k}"); break
            if HANGUL.search(ts): errs.append(f"hangul: {k}")
            if [m.group(1) for m in MARK.finditer(es_)] != [m.group(1) for m in MARK.finditer(ts)]:
                errs.append(f"inline quotation markers changed: {k}")
            if len(ANYMARK.findall(ts)) != 2 * len(MARK.findall(ts)):
                errs.append(f"broken marker: {k}")
            for m in MARK.finditer(ts):
                nq += 1
                if not quote_cit(BOOK, m.group(2), m.group(1)): badq.append(f"{k} inline [{m.group(1)}] {m.group(2)[:50]}")
            if k.startswith("ui."):
                for ph in re.findall(r"\{\w+\}|<br>", es_):
                    if ph not in ts: errs.append(f"placeholder {ph} lost: {k}")
            plain = re.sub(r"“[^”]*”|«[^»]*»|\"[^\"]*\"|⟦Q[^⟧]*⟧.*?⟦/Q⟧|\([^)]*\)", "", ts)
            hits = ENGW.findall(plain)
            if es_.strip() and nows(ts) == nows(es_) and len(es_.split()) > 2: warns.append(f"untranslated? {k}")
            elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
    for k in T:
        if k not in EN: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    sel = [k for k in EN if not CHUNK or CH[k] == CHUNK]
    print(f"[{l}{scope}] translated: {sum(1 for k in sel if k in T)}/{len(sel)} · quotations checked: {nq} · bad: {len(badq)} · "
          f"errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


def js_obj(path):
    s = open(path, encoding="utf-8").read()
    return json.loads(s[s.index("{"):s.rindex("}") + 1])


VOICE = {
    "es": ("helena|laura|sabina|elvira|dalia|paloma|elena|monica|paulina|lucia|ximena|female",
           "pablo|alvaro|jorge|raul|diego|gerardo|jorge|tomas|male", "es", "es-MX", "/(MX|US|419|AR|CO)/i"),
    "fr": ("denise|julie|hortense|amelie|eloise|vivienne|brigitte|audrey|aurelie|sylvie|female",
           "henri|paul|claude|remy|antoine|jerome|alain|male", "fr", "fr-FR", "/FR/i"),
    "pt": ("francisca|maria|thalita|leila|leticia|yara|luciana|raquel|female",
           "antonio|donato|fabio|humberto|julio|nicolau|male", "pt-BR", "pt-BR", "/BR/i"),
}


def build(l, T, LINK):
    def V(k):
        v = T.get(k, EN[k]) if DRAFT else T[k]
        if l == "fr" and not k.endswith(".q") and not k.startswith("ui."):
            v = [[fr_nb(x) for x in r] for r in v] if isinstance(v, list) else fr_nb(v)
        return v
    UI = {k[3:]: strip_marks(V(k)) for k in EN if k.startswith("ui.")}
    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "abridged")
    os.makedirs(out, exist_ok=True)
    M = js_obj(os.path.join(EN_DIR, "meta.js"))
    o, cl = QUOTES[l]
    toc, nblocks = [], 0
    for t in M["toc"]:
        no = t["no"]
        d = js_obj(os.path.join(EN_DIR, t["file"]))
        blocks = []
        for i, b in enumerate(d["blocks"]):
            base = f"{no}.b{i}"
            if b[0] == "h": blocks.append(["h", strip_marks(V(base + ".h"))])
            elif b[0] == "p": blocks.append(["p", strip_marks(V(base + ".p"))])
            elif b[0] == "t": blocks.append(["t", [[strip_marks(x) for x in r] for r in V(base + ".t")]])
            elif len(b) > 2: blocks.append(["q", strip_marks(V(base + ".box"))] + b[2:])
            elif base + ".q" in EN:
                pre, cits, inner, post = box_parts(EN[base + ".q"])
                if base + ".q" in T:
                    txt = T[base + ".q"].strip()
                    if pre.strip() or post.strip(): txt = o + txt + cl
                    blocks.append(["q", txt, {"c": LINK.get(base + ".q", "")}])
                else:                                   # draft only: English
                    blocks.append(["q", strip_marks(EN[base + ".q"]), {"c": cits.split("|")[0]}])
            else: blocks.append(["q", strip_marks(V(base + ".ask"))])
        if len(blocks) != len(d["blocks"]): raise SystemExit(f"block count differs in paper {no}")
        title = strip_marks(V(f"{no}.title"))
        with open(os.path.join(out, t["file"]), "w", encoding="utf-8") as f:
            f.write("UB_CHAP(%d,%s);" % (no, json.dumps({"no": no, "title": title, "blocks": blocks}, ensure_ascii=False)))
        label = UI["label_paper"].replace("{n}", str(no)) if no else UI["label_foreword"]
        toc.append({"no": no, "title": title, "part": t["part"], "file": t["file"],
                    "subs": [b[1] for b in blocks if b[0] == "h"], "n": len(blocks), "label": label})
        nblocks += len(blocks)
    meta = {"title": UI["title"], "sub": UI["sub"], "orig": "", "author": "Jay Han", "translator": "",
            "publisher": "", "year": M.get("year", ""), "by": UI["by"], "copy": UI["copy"], "toc": toc}
    with open(os.path.join(out, "meta.js"), "w", encoding="utf-8") as f:
        f.write("UB_META(%s);" % json.dumps(meta, ensure_ascii=False))

    t = open(os.path.join(EN_DIR, "index.html"), encoding="utf-8").read()
    js = lambda s: s.replace("\\", "\\\\").replace("'", "\\'")
    attr = lambda s: s.replace("&", "&amp;").replace('"', "&quot;")
    fem, mal, tl, ulang, pref = VOICE[l]
    R = [
     ('<html lang="en">', f'<html lang="{l}">'),
     ("<title>The Urantia Book, Abridged</title>", "<title>%s</title>" % attr(UI["title"])),
     ("word-break:keep-all", "word-break:normal;overflow-wrap:break-word;hyphens:auto"),
     ('<button class="btn" id="burger">☰ Contents</button>', '<button class="btn" id="burger">%s</button>' % UI["contents"]),
     ('title="How far to read"', 'title="%s"' % attr(UI["scope_title"])),
     ('<option value="ch">This paper</option><option value="all">Keep going</option>',
      '<option value="ch">%s</option><option value="all">%s</option>' % (UI["scope_ch"], UI["scope_all"])),
     ('<button class="btn g" id="play">▶ Listen</button>', '<button class="btn g" id="play">%s</button>' % UI["listen"]),
     ('<button class="btn" id="stopb">■ Stop</button>', '<button class="btn" id="stopb">%s</button>' % UI["stop"]),
     ('<select id="voice" title="Voice">', '<select id="voice" title="%s">' % attr(UI["voice_title"])),
     ('id="spd" title="Speed"', 'id="spd" title="%s"' % attr(UI["speed_title"])),
     ('placeholder="Find a paper or heading"', 'placeholder="%s"' % attr(UI["search_ph"])),
     ('<p style="color:var(--dim)">Loading…</p>', '<p style="color:var(--dim)">%s</p>' % UI["loading"]),
     ('content:"This book cannot be printed. Please read it on screen."', 'content:"%s"' % UI["no_print"].replace('"', "'")),
     ("flash('You may quote, but not copy more than '+LIMIT+' characters at once.')",
      "flash('%s')" % js(UI["copy_limit"]).replace("{n}", "'+LIMIT+'")),
     ("flash('This book cannot be copied, saved, or printed as a whole.')", "flash('%s')" % js(UI["no_bulk"])),
     ("var FEM=/aria|jenny|zira|samantha|female|susan|hazel|libby|sonia/i, MAL=/guy|david|mark|daniel|male|ryan|george|christopher|eric/i;",
      f"var FEM=/{fem}/i, MAL=/{mal}/i;"),
     ("VOICES=(SPK.getVoices()||[]).filter(function(v){return /^en/i.test(v.lang)});\n  VOICES.sort(function(a,b){return vscore(b)-vscore(a)});",
      "VOICES=(SPK.getVoices()||[]).filter(function(v){return /^%s/i.test(v.lang)});\n"
      "  VOICES.sort(function(a,b){return (vscore(b)+(%s.test(b.lang)?1:0))-(vscore(a)+(%s.test(a.lang)?1:0))});" % (l, pref, pref)),
     ("o.textContent='Standard voice (same in every browser)'", "o.textContent='%s'" % js(UI["std_voice"])),
     ("&tl=en&", f"&tl={tl}&"),
     ("u.lang='en-US'", f"u.lang='{ulang}'"),
     ("$('#play').textContent='▶ Listen'", "$('#play').textContent='%s'" % js(UI["listen"])),
     ("$('#play').textContent='⏸ Pause'", "$('#play').textContent='%s'" % js(UI["pause"])),
     ("(t.mark||(t.no?t.no:'Fwd'))", "(t.mark||(t.no?t.no:'%s'))" % js(UI["toc_mark_foreword"])),
     ("'<div style=\"color:var(--dim);font-size:12.5px;padding:6px\">Nothing found.</div>'",
      "'<div style=\"color:var(--dim);font-size:12.5px;padding:6px\">%s</div>'" % js(UI["nothing"])),
     ("(t.label||(t.no?'Paper '+t.no:'Foreword'))",
      "(t.label||(t.no?'%s':'%s'))" % (js(UI["label_paper"]).replace("{n}", "'+t.no+'"), js(UI["label_foreword"]))),
     ("else if(b[0]==='q'){h+='<div class=\"bx\" id=\"p'+i+'\">'+esc(b[1])+'</div>'}",
      "else if(b[0]==='q'){h+='<div class=\"bx\" id=\"p'+i+'\">'+esc(b[1])+(b[2]&&b[2].c?'<a class=\"cit\" href=\"/%s/book/#'+b[2].c+'\" title=\"%s\">'+b[2].c+'</a>':'')+'</div>'}"
      % (l, js(attr(UI["cite_title"])))),
     ('<button id="prev">← Previous</button><button id="next">Next →</button>',
      '<button id="prev">%s</button><button id="next">%s</button>' % (js(UI["prev"]), js(UI["next"]))),
     ('title="Listen to this paragraph"', 'title="%s"' % js(attr(UI["para_listen"]))),
     ("'<div class=\"note\">The text could not be loaded. Please check your connection and reload this page.</div>'",
      "'<div class=\"note\">%s</div>'" % js(UI["load_fail"])),
     ("location.href='/?lang=en'", f"location.href='/{l}/'"),
     ("+'<br>by '+esc(M.author)", "+'<br>'+esc(M.by||M.author)"),
     ("$('#bby').textContent=d.by||('by '+d.author);", "$('#bby').textContent=d.by||d.author;"),
     ("</style></head>", ".bx .cit{margin-left:8px;font-size:12px;color:#1F6D73;text-decoration:none;white-space:nowrap;opacity:.8}"
      ".bx .cit:hover{text-decoration:underline}[data-dark='1'] .bx .cit{color:#e9d99a}</style></head>"),
    ]
    for a, b in R:
        if a not in t: raise SystemExit("not found in the English index.html: " + a[:80])
        t = t.replace(a, b, 1 if a == "</style></head>" else -1)
    if DRAFT:
        t = t.replace("<body>\n", '<body>\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>\n', 1)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(t)

    left = []
    for f in os.listdir(out):
        s = open(os.path.join(out, f), encoding="utf-8").read()
        if HANGUL.search(s) or "⟦" in s: left.append(f)
    for w in ("☰ Contents", "▶ Listen", "⏸ Pause", "← Previous", "Loading…", "'Paper '", "Nothing found", "lang=en", "tl=en&", "en-US"):
        if w in t and w.split(" ")[-1] not in str(UI.get("pause", "")): left.append("index.html:" + w)
    if left and not DRAFT: raise SystemExit("CHECK FAILED: Hangul / markers / English screen text left in output: %s" % left[:10])
    if left: print("  (draft) left in output:", left[:10])
    print(f"[{l}{' DRAFT' if DRAFT else ''}] {len(toc)} papers · {nblocks} blocks · {len(LINK)} quotation boxes linked → {out}")


fail_any = False
for l in LANGS:
    BOOK, T = load(l)
    LINK = {}
    failed = check(l, BOOK, T, LINK)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/abridged/ not written (use --draft for a preview)"); continue
    build(l, T, LINK)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
