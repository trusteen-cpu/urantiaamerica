# -*- coding: utf-8 -*-
# 「예수의 삶과 가르침」(jesus-book)·「예수의 열두 사도」(apostles-book) 스페인어·프랑스어·포르투갈어판 — 영어 원본에서 번역 단위 뽑기
#   원본(읽기만): 극동판 site/en/jesus-book/, site/en/apostles-book/ (index.html, data/intro.js, toc.js, chNN.js)
#   결과
#     src/<book>/skeleton.json      구조(번역하지 않음): 장·블록 순서, 인용 정보, chunk 목록
#     src/<book>/cNN.json           영어 단위(인용 단위는 dict {"en","cits","wrap"} — 번역하지 않음)
#     work/<book>/src_cNN.json      번역할 단위(인용 dict 제외) — 세 언어 공용, 읽기 전용
#     auto_<l>.json                 자동으로 잘라 온 공식 번역 인용 {"<book>:<key>": "토막 … 토막"}
#     work/<book>/todo_<l>_cNN.json  손으로 잘라야 할 인용 {"key": {"cits", "en", "verses", "why"}}
#     work/<book>/inline_<l>_cNN.json 산문 속 ⟦Q⟧ 인용 {"key": [{"cit", "en", "verses", "auto"?}]}
#   python extract_src.py          (<l>/ 번역본은 건드리지 않음)
import html, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en"
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
ORDER = list(EN)                     # verse order
POS = {c: i for i, c in enumerate(ORDER)}
LANGS = ("es", "fr", "pt")
BOOKS = ("jesus", "apostles")
FOLDER = {"jesus": "jesus-book", "apostles": "apostles-book"}
TARGET, MAXW = 7000, 8500            # chunk size (English words), whole chapters
MIN_INLINE_WORDS = 6                 # quoted speech in prose shorter than this is not marked

N = lambda s: re.sub(r"[^a-z0-9]", "", s.lower().replace("’", "").replace("'", ""))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
SENT = re.compile(r"(?<=[.?!])[\"”’»\)]*\s+(?=[\"“‘«(¿¡—–]*\s?[A-ZÀ-ÖØ-Þ0-9])")
CLAUSE = re.compile(r"(?<=[;:])\s+")
OPEN = {"es": "«", "fr": "«", "pt": "“"}; CLOSE = {"es": "»", "fr": "»", "pt": "”"}
QCH = "“”\"'‘’«» "
NV = {c: N(t) for c, t in EN.items()}


def rd(p):
    s = open(p, encoding="utf-8").read().strip()
    return json.loads(s[s.index("(") + 1:s.rindex(")")])


def splits(t, rx):
    out, pos = [], 0
    for m in rx.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def qsegs(t, marks):
    """text split at quotation marks → list of segments (outside / inside alternating)."""
    return [s for s in re.split("[%s]" % marks, t)]


# ------------------------------------------------------------------ locating English quotations in en.json
def locate(part, prefer=()):
    """verse citations (1 or 2 consecutive) whose English contains the part (punctuation/case ignored)."""
    n = N(part)
    if len(n) < 12: return None
    pool = list(prefer) + ORDER
    for c in pool:
        if n in NV[c]: return [c]
    for i, c in enumerate(ORDER[:-1]):
        if n in NV[c] + NV[ORDER[i + 1]]: return [c, ORDER[i + 1]]
    return None


def fuzzy(part, papers):
    """best guess verses (for the todo list) by shared 4-word sequences."""
    w = re.findall(r"[a-z0-9]+", part.lower())
    grams = {tuple(w[i:i + 4]) for i in range(len(w) - 3)}
    if not grams: return []
    sc = []
    for c, t in EN.items():
        if papers and int(c.split(":")[0]) not in papers: continue
        v = re.findall(r"[a-z0-9]+", t.lower())
        g = {tuple(v[i:i + 4]) for i in range(len(v) - 3)}
        k = len(grams & g)
        if k: sc.append((k, c))
    sc.sort(key=lambda x: (-x[0], POS[x[1]]))
    return [c for k, c in sc[:3] if k >= max(2, len(grams) // 5)]


def split_across(part, cits):
    """English part that runs over two verses → [(sub, cit), (sub, cit)]."""
    if len(cits) == 1: return [(part, cits[0])]
    a, n = NV[cits[0]], N(part)
    for k in range(len(n), 0, -1):            # longest prefix of the part that is a suffix of verse 1
        if a.endswith(n[:k]) and NV[cits[1]].startswith(n[k:]): break
    else: return None
    # map normalized index k back into the raw part
    cnt = 0
    for i, ch in enumerate(part):
        if re.match(r"[a-z0-9]", ch.lower().replace("’", "")) and ch not in "’'":
            if cnt == k: return [(part[:i].strip(), cits[0]), (part[i:].strip(), cits[1])]
            cnt += 1
    return [(part, cits[0])]


def _span(n, a):
    for i in range(len(a)):
        acc = ""
        for j in range(i, len(a)):
            acc += N(a[j])
            if acc == n: return i, j
            if len(acc) > len(n): break
    return None


def _sane(en, out):
    if not out: return False
    r = len(out) / max(1, len(en))
    if not 0.65 <= r <= 2.0: return False
    return sorted(re.findall(r"\d+", en)) == sorted(re.findall(r"\d+", out)) or not re.findall(r"\d+", en)


def cut_one(l, sub, cit):
    """official words corresponding to an English sub-span of one verse, or None."""
    t, o, n = EN[cit], amq.text(l, cit), N(sub)
    if not n: return None
    if n == N(t): return o.strip()
    levels = [(t, o)]
    a, b = qsegs(t, "“”\""), qsegs(o, OPEN[l] + CLOSE[l])
    if len(a) == len(b) and len(a) > 1:
        levels += list(zip(a, b))
    for x, y in levels:
        if n == N(x) and x is not t: return y.strip(QCH)
        for rx in (SENT, SPLIT, CLAUSE):
            p, q = splits(x, rx), splits(y, rx)
            if len(p) != len(q) or len(p) < 2: continue
            sp = _span(n, p)
            if sp:
                r = " ".join(q[sp[0]:sp[1] + 1]).strip(QCH)
                if _sane(" ".join(p[sp[0]:sp[1] + 1]), r): return r
    return None


def official(l, en, cits):
    """English quotation (pieces joined with …) → official text with the same … joins, or None."""
    out = []
    for part in [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", en.strip(QCH)) if p.strip(QCH + ".,;:")]:
        loc = locate(part, cits)
        if not loc or any(c not in cits for c in loc): return None
        pieces = split_across(part, loc)
        if not pieces: return None
        got = []
        for sub, c in pieces:
            r = cut_one(l, sub, c)
            if r is None: return None
            got.append(r)
        out.append(" ".join(got))
    return " … ".join(out) if out else None


def qcheck(l, text, cits):
    hay = re.sub(r"\s+", "", "".join(amq.text(l, c) for c in cits)); pos = 0
    for piece in re.split(r"…|\.\.\.", text):
        piece = re.sub(r"\s+", "", piece).strip(QCH)
        if not piece: continue
        k = hay.find(piece, pos)
        if k < 0: return False
        pos = k + len(piece)
    return True


# ------------------------------------------------------------------ inline quotation marking (verbatim quoted speech in prose)
QSEG = re.compile(r"“([^“”]+)”")


def mark_inline(text, papers):
    pref = [c for c in ORDER if int(c.split(":")[0]) in papers]
    def rep(m):
        inner = m.group(1)
        if len(inner.split()) < MIN_INLINE_WORDS or "⟦" in inner: return m.group(0)
        parts = [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", inner) if p.strip(QCH + ".,;:")]
        cits = []
        for p in parts:
            loc = locate(p, pref)
            if not loc: return m.group(0)
            for c in loc:
                if c not in cits: cits.append(c)
        if any(POS[a] > POS[b] for a, b in zip(cits, cits[1:])): return m.group(0)
        return "“⟦Q " + ",".join(cits) + "⟧" + inner + "⟦/Q⟧”"
    return QSEG.sub(rep, text)


# ------------------------------------------------------------------ papers of a chapter (from its src line)
def papers_of(src):
    nums = [int(x) for x in re.findall(r"\b(1\d\d)\b", src)]
    return set(range(min(nums), max(nums) + 1)) if nums else set()


PURE_SRC = re.compile(r"^(?:Papers?|sections?|[0-9]+|[ ,;–-])+$")


# ------------------------------------------------------------------ one book
def ui_units(book, ix):
    g = lambda rx: html.unescape(re.search(rx, ix).group(1))
    U = {
        "ui.title": g(r"<title>(.*?)</title>"),
        "ui.desc": g(r'<meta name="description" content="(.*?)">'),
        "ui.og_title": g(r'<meta property="og:title" content="(.*?)">'),
        "ui.hub": g(r'<a class="ur-home-btn"[^>]*title="(.*?)"'),          # back button "← Jesus Study"
        "ui.contents": g(r'<button id="tg">(.*?)</button>'),
        "ui.smaller": g(r'<button id="fm" title="(.*?)"'),
        "ui.larger": g(r'<button id="fp" title="(.*?)"'),
        "ui.night": g(r'<button id="dk" title="(.*?)"'),
        "ui.loading": g(r'<div class="empty">(.*?)</div>'),
        "ui.toc_about": "About",
        "ui.toc_about_long": "About the Book & Preface",
        "ui.about_book": "About the Book",
        "ui.and_preface": "& Preface",
        "ui.preface": "Preface",
        "ui.illustration": "Illustration: {title}",
        "ui.ub": "The Urantia Book",
        "ui.prologue": "Prologue",
        "ui.chapter": "Chapter {n}",
        "ui.epilogue": "Epilogue",
    }
    for s in ("<i>About</i><span>About the Book &amp; Preface</span>", "['intro','About the Book','& Preface']",
              "<h3>About the Book</h3>", "<h3 id=\"pre\">Preface</h3>", "alt=\"Illustration: '", "<em>The Urantia Book</em>, "):
        assert s in ix, (book, "index.html changed", s)
    return U


def extract(book):
    D = os.path.join(FE, FOLDER[book])
    ix = open(os.path.join(D, "index.html"), encoding="utf-8").read()
    U, GROUP = {}, {}
    def put(k, v, g):
        assert k not in U, k
        U[k] = v; GROUP[k] = g
    for k, v in ui_units(book, ix).items(): put(k, v, "intro")
    SK = {"book": book, "folder": FOLDER[book], "chapters": [], "quotes": {}}

    # intro
    I = rd(os.path.join(D, "data", "intro.js"))
    sk = {"keys": list(I)}
    for f in ("title", "sub", "kick", "one"):
        if f in I: put("intro." + f, I[f], "intro")
    for f in ("coverAlt", "heroAlt"):
        if f in I: put("intro.alt", I[f], "intro"); sk["alt"] = f
    for f in ("cover", "hero"):
        if f in I: sk["img"] = [f, os.path.basename(I[f])]
    sk["meta"] = len(I["meta"]); sk["about"] = len(I["about"])
    for i, t in enumerate(I["meta"]): put(f"intro.meta{i + 1}", t, "intro")
    for i, t in enumerate(I["about"]): put(f"intro.about{i + 1}", t, "intro")
    sk["lists"] = []
    for i, (h, items) in enumerate(I.get("lists", [])):
        put(f"intro.list{i + 1}.title", h, "intro")
        for j, t in enumerate(items): put(f"intro.list{i + 1}.{j + 1}", t, "intro")
        sk["lists"].append(len(items))
    sk["preface"] = []
    for i, (ty, t) in enumerate(I["preface"]):
        k = f"intro.pre{i + 1}"
        if t == "Jay Han": sk["preface"].append([ty, None, t]); continue
        m = re.match(r"^“(.+)”\s*\((\d+:\d+\.\d+)\)$", t)
        if m:
            put(k, {"en": m.group(1), "cits": [m.group(2)], "wrap": True, "tail": f" ({m.group(2)})"}, "intro")
        else: put(k, t, "intro")
        sk["preface"].append([ty, k, None])
    SK["intro"] = sk

    # chapters
    toc = rd(os.path.join(D, "data", "toc.js"))
    parts = []
    for f in sorted(x for x in os.listdir(os.path.join(D, "data")) if re.match(r"ch\d+\.js$", x)):
        c = rd(os.path.join(D, "data", f))
        n = c["n"]; p = f"ch{n:02d}"; g = p
        lab = c["label"]
        kind = "prologue" if lab == "Prologue" else "epilogue" if lab == "Epilogue" else "chapter"
        assert kind != "chapter" or lab == f"Chapter {n}", lab
        if c["part"] and c["part"] not in parts:
            parts.append(c["part"]); put(f"part{len(parts)}", c["part"], g)
        put(p + ".title", c["title"], g)
        ch = dict(n=n, file=f, kind=kind, part=parts.index(c["part"]) + 1 if c["part"] else 0,
                  img=os.path.basename(c["img"]) if c["img"] else "", blocks=[])
        if PURE_SRC.match(c["src"]): ch["src"] = c["src"]
        else: put(p + ".src", c["src"], g); ch["src"] = None
        pap = papers_of(c["src"]) or set(range(120, 197))
        if kind == "epilogue": pap |= {196}
        heads = []
        for i, (ty, t) in enumerate(c["b"]):
            k = f"{p}.b{i + 1:03d}"
            if ty == "q":
                put(k, {"en": t, "wrap": t.startswith("“") and t.endswith("”"), "papers": sorted(pap)}, g)
            else:
                if ty == "p": t = mark_inline(t, pap)
                put(k, t, g)
            if ty == "h": heads.append(t)
            ch["blocks"].append([ty, k])
        tt = next(x for x in toc if x[0] == n)
        assert [tt[1], tt[2], tt[3], tt[4]] == [lab, c["title"], c["part"], heads], (book, n, "toc differs")
        SK["chapters"].append(ch)
    SK["parts"] = len(parts)
    return U, GROUP, SK


def words(v):
    if isinstance(v, dict): return 0
    return len(re.sub(r"⟦/?Q[^⟧]*⟧", "", v).split())


def main():
    auto = {l: {} for l in LANGS}
    report = []
    for book in BOOKS:
        U, GROUP, SK = extract(book)
        # locate quotations
        for k, v in U.items():
            if not isinstance(v, dict): continue
            if "cits" not in v:
                cits = []
                for part in [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", v["en"].strip(QCH)) if p.strip(QCH + ".,;:")]:
                    loc = locate(part, [c for c in ORDER if int(c.split(":")[0]) in set(v["papers"])])
                    if not loc: cits = None; break
                    for c in loc:
                        if c not in cits: cits.append(c)
                if cits and any(POS[a] > POS[b] for a, b in zip(cits, cits[1:])): cits = None
                v["found"] = bool(cits)
                v["cits"] = cits or fuzzy(v["en"], set(v["papers"]))
            del_p = v.pop("papers", None)
            SK["quotes"][k] = {x: v[x] for x in ("cits", "wrap", "tail", "found") if x in v}
        # chunks: c01 = ui + intro + first chapters; whole chapters, ~7,000 words
        order = list(U)
        groups = []
        for k in order:
            if not groups or groups[-1][0] != GROUP[k]: groups.append([GROUP[k], []])
            groups[-1][1].append(k)
        chunks, cur, n = [], [], 0
        for g, ks in groups:
            w = sum(words(U[k]) for k in ks)
            if cur and n >= 4000 and (n + w > MAXW or n >= TARGET): chunks.append(cur); cur, n = [], 0
            cur += ks; n += w
        if cur: chunks.append(cur)
        SK["chunks"] = ["c%02d" % (i + 1) for i in range(len(chunks))]
        SK["chunk_of"] = {}
        sd, wd = os.path.join(H, "src", book), os.path.join(H, "work", book)
        os.makedirs(sd, exist_ok=True); os.makedirs(wd, exist_ok=True)
        stats = {l: dict(q_auto=0, q_todo=0, i_auto=0, i_todo=0) for l in LANGS}
        print(f"== {book}")
        tot = 0
        for i, ks in enumerate(chunks):
            c = "c%02d" % (i + 1)
            S = {k: U[k] for k in ks}
            for k in ks: SK["chunk_of"][k] = c
            json.dump(S, open(os.path.join(sd, c + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            P = {k: v for k, v in S.items() if not isinstance(v, dict)}
            json.dump(P, open(os.path.join(wd, f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            w = sum(words(v) for v in P.values()); tot += w
            chs = sorted({GROUP[k] for k in ks if GROUP[k].startswith("ch")})
            line = []
            for l in LANGS:
                todo, inl = {}, {}
                for k, v in S.items():
                    if isinstance(v, dict):
                        r = official(l, v["en"], v["cits"]) if v.get("found", True) and v["cits"] else None
                        if r and qcheck(l, r, v["cits"]): auto[l][f"{book}:{k}"] = r; stats[l]["q_auto"] += 1
                        else:
                            todo[k] = {"cits": v["cits"], "en": v["en"].strip(QCH),
                                       "verses": {x: amq.text(l, x) for x in v["cits"]},
                                       "why": "automatic cut failed" if v.get("found", True) else
                                              "English not found verbatim; verses are best guesses"}
                            stats[l]["q_todo"] += 1
                        continue
                    for m in re.finditer(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", v):
                        cits = m.group(1).split(",")
                        e = {"cit": m.group(1), "en": m.group(2)}
                        a = official(l, m.group(2), cits)
                        if a and qcheck(l, a, cits): e["auto"] = a; stats[l]["i_auto"] += 1
                        else: stats[l]["i_todo"] += 1
                        e["verses"] = {x: amq.text(l, x) for x in cits}
                        inl.setdefault(k, []).append(e)
                json.dump(todo, open(os.path.join(wd, f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                json.dump(inl, open(os.path.join(wd, f"inline_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
                line.append(f"{l} todo {len(todo)}")
            nq = len(S) - len(P); ni = sum(v.count("⟦Q ") for v in P.values())
            print(f"{c}: {chs[0] if chs else 'intro'}–{chs[-1] if chs else ''}  {len(P)} units, {w} words, "
                  f"{nq} quotations, {ni} inline  ({', '.join(line)})")
        print(f"{book}: {len(chunks)} chunks, {tot} words")
        for l in LANGS:
            s = stats[l]
            msg = (f"  {l}: block quotations auto {s['q_auto']} / by hand {s['q_todo']} · inline quotations with automatic "
                   f"official text {s['i_auto']} / to cut by hand {s['i_todo']}")
            print(msg); report.append(f"{book} {msg.strip()}")
        json.dump(SK, open(os.path.join(sd, "skeleton.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
