# -*- coding: utf-8 -*-
# 「The Personalities of The Urantia Book」 스페인어·프랑스어·포르투갈어판 → site/<es|fr|pt>/personalities/
#   틀(groups·CSS·head·card·chapter)은 극동판 tools/build_personalities.py 를 exec 로 빌려 쓴다(읽기만, main() 실행 안 함).
#   원고:  src/c01.json        영어 단위(극동판 tools/zh/personalities/src/c01.json 사본, 손대지 않음)
#          src/c01_noq.json    번역용(인용문을 뺀 것)
#          <l>/c01*.json       같은 키의 번역. 인용 객체는 {"cit"} 만 — 인용문은 번역하지 않고
#                              공식 번역(tools/data/<l>.json)에서 글자 그대로 가져온다:
#                              quotes_spec.py 의 (시작, 끝) → amq.cut,  그 밖은 auto_<l>.json (align_quotes.py 가 문장 단위로 맞춘 것)
#   검사(하나라도 걸리면 exit 1): 키·구조 같음 · cit 그대로 · 모든 인용 amq.check · 한글 없음 · /en/ 링크 없음 · 장·카드 수 영어와 같음
#   실행: python build_personalities_am.py [es fr pt]
import glob, html, json, os, re, sys, unicodedata

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(H, ".."))
SITE = os.path.normpath(os.path.join(TOOLS, "..", "site"))
FE_BUILDER = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\build_personalities.py"
sys.path.insert(0, TOOLS); sys.path.insert(0, H)
import amq  # noqa: E402
from quotes_spec import SPEC  # noqa: E402

_src = open(FE_BUILDER, encoding="utf-8").read()
NS = {"__file__": FE_BUILDER, "__name__": "build_personalities_en"}
exec(_src[:_src.rindex("\nmain()")], NS)
esc = html.escape
HANGUL = re.compile(r"[ᄀ-ᇿ㄰-㆏가-힯]")
S = json.load(open(os.path.join(H, "src", "c01.json"), encoding="utf-8"))

FONT = "'Segoe UI',system-ui,sans-serif"
SERIF = "Georgia,'Times New Roman',serif"


def quotes(x, p=""):
    if isinstance(x, dict):
        if "cit" in x: yield p, x
        for k, v in x.items():
            if isinstance(v, (dict, list)): yield from quotes(v, f"{p}.{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x): yield from quotes(v, f"{p}[{i}]")


def strip_q(x):
    if isinstance(x, dict):
        return {"cit": x["cit"]} if "cit" in x else {k: strip_q(v) for k, v in x.items()}
    if isinstance(x, list): return [strip_q(v) for v in x]
    return x


def same_shape(a, b, path, errs):
    if isinstance(a, dict):
        if not isinstance(b, dict) or set(a) != set(b): errs.append(f"{path}: keys differ"); return
        if "cit" in a and a["cit"] != b["cit"]: errs.append(f"{path}: cit changed")
        for k in a: same_shape(a[k], b[k], f"{path}.{k}", errs)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b): errs.append(f"{path}: list length"); return
        for i, (x, y) in enumerate(zip(a, b)): same_shape(x, y, f"{path}[{i}]", errs)
    elif isinstance(a, str):
        if not isinstance(b, str): errs.append(f"{path}: not a string")
        elif a.strip() and not b.strip(): errs.append(f"{path}: empty")


def fr_nb(v):
    """프랑스어 문장부호: ; : ! ? » 앞과 « 뒤의 공백을 줄바꿈 없는 공백으로 (인용문에는 쓰지 않음)."""
    if isinstance(v, str):
        v = re.sub(r" ([;:!?»])", "\u00a0\\1", v)
        return v.replace("« ", "«\u00a0")
    if isinstance(v, list): return [fr_nb(x) for x in v]
    if isinstance(v, dict): return v if "cit" in v else {k: fr_nb(x) for k, x in v.items()}
    return v


def fill_quotes(l, T, err):
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    sp = SPEC.get(l, {}); n = 0
    for k in S:
        for p, q in quotes(T[k], k):
            cit = q["cit"]
            if p in sp: t = " … ".join(amq.cut(l, cit, a, b) for a, b in sp[p])
            elif f"{p}|{cit}" in auto: t = auto[f"{p}|{cit}"]
            else: err.append(f"no quotation for {p} [{cit}]"); continue
            if not amq.check(l, cit, t): err.append(f"quotation not verbatim: {p} [{cit}]")
            q["q"] = t; n += 1
    return n


def merge_ent(e, u):
    n = {k: v for k, v in e.items() if not (k in ("ko", "t") or k.endswith("_ko"))}
    n["t"] = u["name"]
    if e.get("see"): n["note_t"] = u.get("note", ""); return n
    if "aka" in u: n["aka_t"] = u["aka"]
    for k in ("origin", "realm", "number"): n[f"{k}_t"] = u.get(k, "")
    if "roles" in u: n["roles_t"] = u["roles"]
    if "members" in u:
        n["members"] = [{"en": m["en"], "t": z["name"], "note_t": z["note"]} for m, z in zip(e["members"], u["members"])]
    if "quote" in u: n["quote"] = {"ref": e["quote"]["ref"], "en": e["quote"]["en"], "t": u["quote"]["q"]}
    return n


def merge_groups(gs, Z):
    out = []
    for g in gs:
        p = f"g{g['no']:02d}"
        n = {k: v for k, v in g.items() if not (k in ("ko", "items") or k.endswith("_ko"))}
        n["t"] = Z[f"{p}.title"]; n["intro_t"] = Z[f"{p}.intro"]; n["items"] = []
        for i, it in enumerate(g["items"], 1):
            if it.get("sub"):
                s = f"{p}.s{i:02d}"
                si = {k: v for k, v in it.items() if not (k in ("ko", "items") or k.endswith("_ko"))}
                si["t"] = Z[f"{s}.title"]; si["intro_t"] = Z[f"{s}.intro"]
                si["items"] = [merge_ent(e, Z[f"{s}.{j:02d}"]) for j, e in enumerate(it["items"], 1)]
                n["items"].append(si)
            else:
                n["items"].append(merge_ent(it, Z[f"{p}.{i:02d}"]))
        out.append(n)
    return out


def lang_cfg(l, Z):
    fm = dict(title=Z["fm.title"], subtitle=Z["fm.subtitle"], eyebrow=Z["fm.eyebrow"], preface_title=Z["fm.preface_title"],
              howto_title=Z["fm.howto_title"], index_title=Z["fm.index_title"],
              preface=[("q", v["q"], v["cit"]) if isinstance(v, dict) else v for k, v in sorted(Z.items()) if k.startswith("fm.preface.")],
              howto=[tuple(v) for k, v in sorted(Z.items()) if k.startswith("fm.howto.")])
    lbl = {k[7:]: esc(v) for k, v in Z.items() if k.startswith("ui.lbl.")}
    return dict(out=os.path.join(SITE, l, "personalities"), html=l, fm=fm, cite=f"/{l}/book/#", contents=esc(Z["ui.contents"]),
                prev=esc(Z["ui.prev"]), next=esc(Z["ui.next"]), ch="{}", lbl=lbl, see=Z["ui.see_chapter"], index=Z["fm.index_title"],
                font=FONT, serif=SERIF, fonts="family=Source+Serif+4:wght@400")


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def index_page(gs, L, Z):
    slug = NS["slug"]; fm = L["fm"]
    chs = "".join(f'<a href="ch{g["no"]:02d}.html" style="--c:{g["color"]}"><b>{g["no"]}</b><span>{esc(g["t"])}</span></a>' for g in gs)
    ents = []
    for g in gs:
        for it in g["items"]:
            for e in (it["items"] if it.get("sub") else [it]):
                href = f'ch{g["no"]:02d}.html#{slug(e)}'
                ents.append((e["t"], href))
                for a in (e.get("aka_t") or []): ents.append((a, href))
    seen = {}
    for name, href in ents: seen.setdefault(name, href)
    rows = sorted(seen.items(), key=lambda x: (fold(x[0]), x[0]))
    idx, cur = [], None
    for name, href in rows:
        c = fold(name)[:1].upper()
        k = c if c.isalpha() else "#"
        if k != cur: idx.append(f"<h3>{esc(k)}</h3>"); cur = k
        idx.append(f'<a href="{href}">{esc(name)}</a>')
    howto = "".join(f"<dt>{esc(a)}</dt><dd>{esc(b)}</dd>" for a, b in fm["howto"])
    page = (NS["head"](L, fm["title"])
            + f'<header class="top"><div class="eb">{esc(fm["eyebrow"])}</div><h1>{esc(fm["title"])}</h1><p>{esc(fm["subtitle"])}</p>'
              f'<div class="by">{esc(Z["fm.author"])}</div></header>\n<div class="wrap">'
            + f'<h2 class="sec">{esc(fm["preface_title"])}</h2><div class="pref">'
            + "".join(f'<div class="q">“{esc(p[1])}”<a href="{L["cite"]}{esc(p[2])}" target="_blank" rel="noopener">— {esc(p[2])}</a></div>'
                      if isinstance(p, tuple) else f"<p>{esc(p)}</p>" for p in fm["preface"]) + "</div>"
            + f'<h2 class="sec">{esc(fm["howto_title"])}</h2><dl class="howto">{howto}</dl>'
            + f'<h2 class="sec">{L["contents"]}</h2><div class="chs">{chs}</div>'
            + f'<h2 class="sec">{esc(fm["index_title"])}</h2><p class="subi">{esc(Z["ui.index_note"])}</p><div class="idx">{"".join(idx)}</div>'
            + "</div>\n</body>\n</html>\n")
    return page, len(rows)


QDIV = re.compile(r'(<div class="q">)“(.*?)”(<a )', re.S)


def build(l, gs):
    err = []
    T = {}
    for f in sorted(glob.glob(os.path.join(H, l, "c*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        dup = set(d) & set(T)
        if dup: err.append(f"duplicate keys in {os.path.basename(f)}: {sorted(dup)[:5]}")
        T.update(d)
    missing = [k for k in S if k not in T]; extra = [k for k in T if k not in S]
    if missing or extra:
        print(f"[{l}] missing {len(missing)} {missing[:8]}, extra {len(extra)} {extra[:8]}"); return False
    for k in S: same_shape(strip_q(S[k]), T[k], k, err)
    if "{}" not in T["ui.see_chapter"]: err.append("ui.see_chapter must keep {}")
    if l == "fr": T = {k: (v if k.startswith("ui.") else fr_nb(v)) for k, v in T.items()}
    nq = fill_quotes(l, T, err)

    L = lang_cfg(l, T); mg = merge_groups(gs, T)
    pages = {}
    for i, g in enumerate(mg):
        pages[f'ch{g["no"]:02d}.html'] = NS["chapter"](g, "t", L, mg[i - 1] if i else None, mg[i + 1] if i + 1 < len(mg) else None)
    page, nidx = index_page(mg, L, T); pages["index.html"] = page
    if l == "fr":  # 프랑스어 인용 상자는 « » 로
        pages = {fn: QDIV.sub(lambda m: f"{m.group(1)}«\u00a0{m.group(2)}\u00a0»{m.group(3)}", t) for fn, t in pages.items()}
    cards_en = sum(len(it["items"]) if it.get("sub") else 1 for g in gs for it in g["items"])
    cards = sum(len(it["items"]) if it.get("sub") else 1 for g in mg for it in g["items"])
    if cards != cards_en or len(mg) != len(gs): err.append("chapter/card count differs from English")
    for fn, t in pages.items():
        m = HANGUL.findall(t)
        if m: err.append(f"{fn}: Hangul {''.join(m[:10])}")
        if "/en/" in t: err.append(f"{fn}: /en/ link")
        if f'<html lang="{l}">' not in t or "/home-button.js" not in t: err.append(f"{fn}: lang/home button")
    print(f"[{l}] chapters {len(mg)}, cards {cards}, index entries {nidx}, quotations {nq}, errors {len(err)}")
    for x in err[:40]: print("   ·", x)
    if err: return False
    os.makedirs(L["out"], exist_ok=True)
    for fn, t in pages.items():
        open(os.path.join(L["out"], fn), "w", encoding="utf-8").write(t)
    print(f"     → {L['out']} ({len(pages)} pages)")
    return True


def main():
    gs = NS["groups"]()
    ok = all([build(l, gs) for l in (sys.argv[1:] or ["es", "fr", "pt"])])
    if not ok: raise SystemExit("CHECKS FAILED")
    print("ALL CHECKS PASSED")


main()
