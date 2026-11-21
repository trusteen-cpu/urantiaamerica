# -*- coding: utf-8 -*-
# 「주 우주 연구」 해설 (A Commentary on A Study of the Master Universe) 스페인어·프랑스어·포르투갈어판 → site/<l>/cosmology/
#   극동판 tools/zh/cosmology/build_cosmology_zh.py 를 옮긴 것. 틀(CSS·head·render)은 극동판 tools/build_cosmology.py 에서 빌려 쓴다(고치지 않음).
#   원고: src/skeleton.json (줄 구조) + src/cNN.json (영어 단위)
#        + <l>/cNN.json (번역: 블록 인용을 뺀 모든 단위, 같은 키)
#        + 블록 인용: auto_<l>.json (자동) 또는 <l>/quotes_cNN.json (손으로 자른 것, 이쪽이 우선)
#   검사: 키 누락·구조·한글·영어 잔재·인용(tools/data/<l>.json 원문 그대로) — 하나라도 어긋나면 쪽을 만들지 않는다.
#   python build_cosmology_am.py es [fr pt]           검사 + 통과 시 빌드
#   python build_cosmology_am.py es --chunk c03       그 묶음만 검사 (쓰지 않음)
#   python build_cosmology_am.py es --draft           빠진 단위는 영어로 채워 _draft_<l>/ 에 미리보기
import json, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]

_src = open(os.path.join(FE, "tools", "build_cosmology.py"), encoding="utf-8").read()
ns = {"__file__": os.path.join(FE, "tools", "build_cosmology.py"), "__name__": "build_cosmology_borrowed"}
exec(_src.split('for lang in ("ko", "en"):')[0], ns)
esc, inline = ns["esc"], ns["inline"]
ns["CSS"] = ns["CSS"].replace("word-break:keep-all", "word-break:normal;overflow-wrap:break-word;hyphens:auto")

SK = json.load(open(os.path.join(H, "src", "skeleton.json"), encoding="utf-8"))
EN, CH = {}, {}
for c in SK["chunks"]:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    EN.update(d); CH.update({k: c for k in d})
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
nows = lambda s: re.sub(r"\s+", "", s)
strip_marks = lambda s: re.sub(r"⟦/?Q[^⟧]*⟧", "", s)
EN_BOOK = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
KEYS = list(EN_BOOK); IDX = {k: i for i, k in enumerate(KEYS)}
FONT = "Georgia,'Times New Roman',serif"; SANS = "'Segoe UI',system-ui,sans-serif"


def cit_keys(cit):
    out = []
    for tok in re.split(r"\s*[,;]\s*", cit.strip()):
        m = re.fullmatch(r"(\d+):(\d+)\.(\d+)(?:[–\-](\d+)(?::(\d+)\.(\d+))?)?", tok)
        if not m: return None
        a = f"{m.group(1)}:{m.group(2)}.{m.group(3)}"
        b = f"{m.group(4)}:{m.group(5)}.{m.group(6)}" if m.group(5) else (f"{m.group(1)}:{m.group(2)}.{m.group(4)}" if m.group(4) else a)
        if a not in IDX or b not in IDX: return None
        out += KEYS[IDX[a]:IDX[b] + 1]
    return out


def fr_nb(s):
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def load(l):
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    T = {}
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    for c in SK["chunks"]:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        elif not CHUNK: print(f"  [missing file] {l}/{c}.json")
        hand = {}
        p = os.path.join(H, l, f"quotes_{c}.json")
        if os.path.exists(p): hand = json.load(open(p, encoding="utf-8"))
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        for k, v in S.items():
            if isinstance(v, dict):
                q = hand.get(k, auto.get(k))
                if q is not None: T[k] = {"q": q, "cit": v["cit"]}
    return BOOK, T


def check(l, BOOK, T):
    def quote_ok(text, cit):
        ks = cit_keys(cit)
        if not ks or any(k not in BOOK for k in ks): return False, "citation not in book"
        hay = nows("".join(BOOK[k] for k in ks))
        for piece in re.split(r"…|\.\.\.", text):
            piece = nows(piece).strip("“”\"'‘’«»")
            if piece and piece not in hay: return False, piece[:50]
        return True, ""
    errs, warns, badq, nq = [], [], [], 0
    for k, ev in EN.items():
        if CHUNK and CH[k] != CHUNK: continue
        if k not in T: errs.append(f"missing: {k}"); continue
        tv = T[k]
        if type(tv) is not type(ev): errs.append(f"type differs: {k}"); continue
        if isinstance(ev, dict):
            nq += 1
            ok, why = quote_ok(tv["q"], tv["cit"])
            if not ok: badq.append(f"{k} [{tv['cit']}] {why}")
            if HANGUL.search(tv["q"]): errs.append(f"hangul: {k}")
            continue
        if isinstance(ev, list) and len(tv) != len(ev): errs.append(f"table cells {len(tv)}≠{len(ev)}: {k}"); continue
        for es_, ts in zip(ev if isinstance(ev, list) else [ev], tv if isinstance(tv, list) else [tv]):
            if not isinstance(ts, str): errs.append(f"not a string: {k}"); break
            if HANGUL.search(ts): errs.append(f"hangul: {k}")
            if [m.group(1) for m in MARK.finditer(es_)] != [m.group(1) for m in MARK.finditer(ts)]:
                errs.append(f"inline quotation markers changed: {k}")
            if ts.count("⟦") != ts.count("⟧") or len(MARK.findall(ts)) * 2 != ts.count("⟦"):
                errs.append(f"broken marker: {k}")
            for m in MARK.finditer(ts):
                nq += 1
                ok, why = quote_ok(m.group(2), m.group(1))
                if not ok: badq.append(f"{k} inline [{m.group(1)}] {why}")
            if k.startswith("ui."):
                ph = set(re.findall(r"\{\w+\}", es_))
                if ph and not ph & set(re.findall(r"\{\w+\}", ts)): errs.append(f"placeholder lost: {k}")
            elif "|" in ts and "|" not in es_: errs.append(f"'|' not allowed: {k}")
            plain = re.sub(r"\*[^*]+\*|“[^”]*”|\"[^\"]*\"|⟦Q[^⟧]*⟧.*?⟦/Q⟧|\([^)]*\)", "", ts)
            hits = ENGW.findall(plain)
            if es_.strip() and nows(ts) == nows(es_) and len(es_.split()) > 3: warns.append(f"untranslated? {k}")
            elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
    for k in T:
        if k not in EN: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    print(f"[{l}{scope}] translated: {sum(1 for k in EN if k in T and (not CHUNK or CH[k] == CHUNK))}/"
          f"{sum(1 for k in EN if not CHUNK or CH[k] == CHUNK)} · quotations checked: {nq} · bad: {len(badq)} · errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


def roman_to_int(r):
    v = dict(I=1, V=5, X=10, L=50); s = 0
    for i, ch in enumerate(r): s += -v[ch] if i + 1 < len(r) and v[r[i + 1]] > v[ch] else v[ch]
    return s


def build(l, T):
    V = (lambda k: T.get(k, EN[k])) if DRAFT else (lambda k: T[k])
    if l == "fr":
        V0 = V
        def V(k):
            v = V0(k)
            if isinstance(v, dict): return v
            if isinstance(v, list): return [fr_nb(x) for x in v]
            return fr_nb(v)
    UI = {k[3:]: strip_marks(V(k)) for k in EN if k.startswith("ui.")}

    def lines_of(name):
        out = []
        for e in SK["files"][name]:
            if isinstance(e, str): out.append(e); continue
            t, v = e["t"], V(e["k"])
            if t == "head": out.append(e)
            elif t == "orig": out.append({"t": "orig", "v": strip_marks(v)})
            elif t == "text": out.append(e["p"] + strip_marks(v))
            elif t == "quote": out.append(f'> {strip_marks(v["q"]).strip()} {e["o"]}{v["cit"]}{e["c"]}')
            elif t == "fig": out.append(f'[[Figure | {e["path"]} | {strip_marks(v)}]]')
            elif t == "row": out.append("| " + " | ".join(strip_marks(c) for c in v) + " |")
        return out

    chs = []
    for name in sorted(n for n in SK["files"] if re.fullmatch(r"w\d\d", n)):
        cur = chs[-1] if chs else None
        for ln in lines_of(name):
            if isinstance(ln, dict) and ln.get("t") == "head":
                app = ln["kind"] == "app"
                n = roman_to_int(ln["num"]) if app else int(ln["num"])
                label = (UI["appendix_label"] if app else UI["chapter_label"]).format(n=n, roman=ln["num"], cn=n)
                cur = {"label": label, "name": strip_marks(V(ln["k"])), "app": app, "num": ln["num"], "orig": "", "lines": []}
                chs.append(cur)
            elif isinstance(ln, dict): cur["orig"] = ln["v"]
            else: cur["lines"].append(ln)

    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "cosmology")
    os.makedirs(os.path.join(out, "fig"), exist_ok=True)
    L = dict(out=out, html=l, font=FONT, sans=SANS, fonts="family=Source+Serif+4:wght@400;700",
             cite=lambda r: f"/{l}/book/#" + r, **UI)
    head, render = ns["head"], ns["render"]
    allfigs = []
    na = sum(1 for x in chs if not x["app"])
    for k, c in enumerate(chs):
        c["file"] = ("a%02d.html" % (k - na + 1)) if c["app"] else ("ch%02d.html" % (k + 1))
    pages = []
    for k, c in enumerate(chs):
        body, _ = render(c["lines"], L, allfigs, c["num"], f"{l} {c['label']}")
        pv, nx = (chs[k - 1] if k else None), (chs[k + 1] if k + 1 < len(chs) else None)
        orig = UI["orig"].format(t=c["orig"]) if c["orig"] else ""
        page = (head(L, f'{c["label"]}  {c["name"]} — {L["title"]}')
                + f'<header class="top" style="padding:22px 16px 18px"><div class="eb">{esc(L["eb"])}</div>'
                  f'<p style="margin-top:6px"><a href="./" style="text-decoration:none;border-bottom:1px solid rgba(255,255,255,.5)">{esc(L["title"])}</a></p></header>\n'
                + '<div class="wrap">\n'
                + f'<div class="eyebrow">{esc((L["part2"] if c["app"] else L["part1"]).split("  ")[0])}  ·  {esc(c["label"])}</div>'
                + f'<h1 class="ct">{inline(c["name"])}</h1>'
                + (f'<p class="orig">{inline(orig)}</p>' if orig else "")
                + f'<div class="body">{body}</div>'
                + '<nav class="pager">'
                + (f'<a href="{pv["file"]}">{esc(L["prev"])} {esc(pv["label"])}</a>' if pv else "<span></span>")
                + f'<a href="./">{esc(L["contents"])}</a>'
                + (f'<a href="{nx["file"]}">{esc(nx["label"])} {esc(L["next"])}</a>' if nx else "<span></span>")
                + "</nav>\n</div>\n</body>\n</html>\n")
        pages.append((c["file"], page))
    toc, cur = [], None
    for c in chs:
        if c["app"] != cur:
            if cur is not None: toc.append("</div>")
            cur = c["app"]; toc.append(f'<div class="part">{esc(L["part2"] if cur else L["part1"])}</div><div class="chs">')
        toc.append(f'<a href="{c["file"]}"><b>{esc(c["num"])}</b><span>{inline(c["name"])}<small>{inline(c["orig"])}</small></span></a>')
    toc.append("</div>")
    blk = lambda n: render("\n".join(lines_of(n)).split("\n"), L, [], 0, "front")[0]
    idx = (head(L, L["title"])
           + f'<header class="top"><div class="eb">{esc(L["eb"])}</div><h1>{esc(L["title"])}</h1><p>{esc(L["sub"])}</p><div class="by">{esc(L["by"])}</div></header>\n'
           + '<div class="wrap">\n'
           + f'<h2 class="toc">{esc(L["pref"])}</h2><div class="front body">{blk("preface")}</div>'
           + f'<h2 class="toc">{esc(L["notes"])}</h2><div class="front body">{blk("notes")}</div>'
           + f'<h2 class="toc">{esc(L["toc"])}</h2>' + "\n".join(toc)
           + f'<div class="colo">{blk("colophon")}</div>'
           + "\n</div>\n</body>\n</html>\n")
    pages.append(("index.html", idx))
    bad = [f for f, p in pages if HANGUL.search(p)]
    if bad and not DRAFT: raise SystemExit(f"CHECK FAILED: hangul in output {bad}")
    for f, p in pages:
        if DRAFT: p = p.replace("<body>\n", '<body>\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>\n', 1)
        open(os.path.join(out, f), "w", encoding="utf-8").write(p)
    en_fig = os.path.join(FE, "site", "en", "cosmology", "fig"); miss = []
    for p in sorted(set(allfigs)):
        n = os.path.basename(p).replace(".png", ".webp"); s = os.path.join(en_fig, n)
        if os.path.exists(s): shutil.copy2(s, os.path.join(out, "fig", n))
        else: miss.append(n)
    if miss: print("  WARN figures missing:", miss)
    q = sum(1 for c in chs for x in c["lines"] if x.startswith("> "))
    print(f"[{l}{' DRAFT' if DRAFT else ''}] pages: {len(chs)} ({na} chapters + {len(chs) - na} appendices) + index, "
          f"figures: {len(set(allfigs))}, block quotations: {q} → {out}")


fail_any = False
for l in LANGS:
    BOOK, T = load(l)
    failed = check(l, BOOK, T)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/cosmology/ not written (use --draft for a preview)"); continue
    build(l, T)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
