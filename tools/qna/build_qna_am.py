# -*- coding: utf-8 -*-
# 「A Thousand Questions and Answers」(qna) 스페인어·프랑스어·포르투갈어판 → site/<es|fr|pt>/qna/ (data.json + index.html)
#   영어 단위: src/units.json (prep.py 가 극동판 tools/zh/qna/src 에서 복사; 손대지 않음), 조각: src/chunks.json
#   번역:      <l>/cNN.json  (같은 키·같은 구조)
#   표시:      ⟦P k⟧ → tools/data/<l>.json[k] 통째로(빌더가 채움) ;  ⟦Q k⟧공식 번역 인용⟦/Q⟧ → amq.check 로 글자 그대로인지 검사
#   화면:      극동판 영어 화면 site/en/qna/index.html (읽기만) 의 글자를 ui.* 로 바꾼다.
#   검사(하나라도 걸리면 아무것도 쓰지 않음): 키·구조, 문단 수, 절 번호 참조, ⟦P⟧ 그대로, ⟦Q⟧ 순서·글자 그대로, 한글 없음,
#        영어가 남은 듯한 글(영어 기능어 비율), 자리표시 {n} 등, 질문 수·순서 = 영어판과 같음
#   python build_qna_am.py es [fr pt] [--chunk c03] [--report 100]
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(H, ".."))
SITE = os.path.normpath(os.path.join(TOOLS, "..", "site"))
sys.path.insert(0, TOOLS)
import amq  # noqa: E402

FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\qna"
EN_DATA = json.load(open(os.path.join(FE, "data.json"), encoding="utf-8"))
EN_PAGE = open(os.path.join(FE, "index.html"), encoding="utf-8").read()
U = json.load(open(os.path.join(H, "src", "units.json"), encoding="utf-8"))
CH = json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))

QM = re.compile(r"⟦Q ([^⟧\s]+)⟧(.*?)⟦/Q⟧", re.S)
PM = re.compile(r"⟦P ([^⟧\s]+)⟧")
REF = re.compile(r"\d+:\d+\.\d+")
HANGUL = re.compile(r"[ᄀ-ᇿ㄰-㆏가-힯]")
EN_FW = re.compile(r"\b(?:the|and|of|which|with|is|are|that|this|was|were|his|from|have|has|by)\b")
LANG_HTML = {"es": "es", "fr": "fr", "pt": "pt-BR"}

args = [a for a in sys.argv[1:]]
REPORT = int(args[args.index("--report") + 1]) if "--report" in args else 40
ONLY = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in amq.LANGS] or list(amq.LANGS)


def check_text(l, c, where, e, z, errors, stat):
    if not isinstance(z, str) or not z.strip():
        errors.append((c, where, "empty or not a string")); return
    if HANGUL.search(z): errors.append((c, where, "Hangul left"))
    if PM.findall(e) != PM.findall(z): errors.append((c, where, f"⟦P⟧ tokens differ: {PM.findall(e)} vs {PM.findall(z)}"))
    eq, zq = [m.group(1) for m in QM.finditer(e)], [m.group(1) for m in QM.finditer(z)]
    if eq != zq: errors.append((c, where, f"⟦Q⟧ citations differ (order/count): en {eq} vs {zq}"))
    if z.count("⟦") != z.count("⟧") or len(re.findall(r"⟦Q ", z)) != z.count("⟦/Q⟧"):
        errors.append((c, where, "broken ⟦ ⟧ marker"))
    for m in QM.finditer(z):
        stat["q"] += 1
        k, q = m.group(1), m.group(2)
        ok = k in amq._load(l) and q.strip() and amq.check(l, k, q)
        if not ok:
            stat["bad"] += 1; errors.append((c, where, f"quotation not verbatim in {l}.json[{k}]: {q[:70]}"))
    er, zr = set(REF.findall(e)), set(REF.findall(z))
    if er - zr: errors.append((c, where, f"references missing: {sorted(er - zr)[:8]}"))
    for ph in re.findall(r"\{\w+\}", e):
        if ph not in z: errors.append((c, where, f"placeholder {ph} missing"))
    if re.search(r"[`<>]|\$\{", z) and not re.search(r"[`<>]|\$\{", e): errors.append((c, where, "characters ` < > ${ not allowed"))
    plain = PM.sub("", QM.sub("", z))
    words = re.findall(r"[A-Za-zÀ-ÿ]+", plain)
    if len(words) >= 8:
        fw = len(EN_FW.findall(plain))
        if fw / len(words) > 0.04: errors.append((c, where, f"looks untranslated (English function words {fw}/{len(words)})"))
    if z.strip() == e.strip() and len(e) > 20: errors.append((c, where, "identical to English"))
    if len(e.split("\n\n")) != len(z.split("\n\n")):
        errors.append((c, where, f"paragraph count {len(z.split(chr(10) * 2))} ≠ English {len(e.split(chr(10) * 2))}"))
    if e.count("**") != z.count("**"): errors.append((c, where, "** bold markers differ"))


def load(l):
    T, missing = {}, []
    for c in CH:
        p = os.path.join(H, l, f"{c}.json")
        if os.path.exists(p):
            T[c] = json.load(open(p, encoding="utf-8"))
        else:
            missing.append(c)
    return T, missing


def build(l):
    T, missing = load(l)
    errors, stat = [], {"q": 0, "bad": 0}
    for c, keys in CH.items():
        if ONLY and c != ONLY: continue
        if c not in T: continue
        Z = T[c]
        for key in keys:
            e = U[key]
            if key not in Z: errors.append((c, key, "missing")); continue
            z = Z[key]
            if isinstance(e, dict):
                if not isinstance(z, dict) or set(z) != set(e): errors.append((c, key, "structure differs")); continue
                for f in e: check_text(l, c, f"{key}.{f}", e[f], z[f], errors, stat)
            else:
                check_text(l, c, key, e, z, errors, stat)
        for key in Z:
            if key not in keys: errors.append((c, key, "extra key (belongs to another chunk or unknown)"))
    print(f"[{l}] chunks present {len(T)}/{len(CH)}  quotations checked {stat['q']} bad {stat['bad']}  errors {len(errors)}")
    if missing: print(f"[{l}] MISSING: {', '.join(missing)}")
    for c, k, m in errors[:REPORT]: print(f"  {c} {k}: {m}")
    if len(errors) > REPORT: print(f"  … {len(errors) - REPORT} more (--report N)")
    if ONLY or missing or errors:
        if not ONLY: print(f"[{l}] CHECK FAILED — nothing written")
        return not errors

    Z = {}
    for c in CH: Z.update(T[c])
    UI = {k[3:]: v for k, v in Z.items() if k.startswith("ui.")}
    render = lambda a: QM.sub(lambda m: m.group(2), PM.sub(lambda m: amq.text(l, m.group(1)), a))
    out = []
    for x in EN_DATA:
        n = int(x["number"]); u = Z[f"q{n:03d}"]
        q = u["question"].strip()
        out.append({"id": x["id"], "number": x["number"], "title": UI["title_form"].replace("{n}", str(n)).replace("{question}", q),
                    "question": q, "answer": render(u["answer"]), "date": x["date"]})
    assert len(out) == len(EN_DATA) == len([k for k in U if k.startswith("q")]) and [d["number"] for d in out] == [d["number"] for d in EN_DATA]
    for d, x in zip(out, EN_DATA):
        assert len(d["answer"].split("\n\n")) == len(x["answer"].split("\n\n")), d["number"]

    t = EN_PAGE
    esc = lambda s: s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")
    jsq = lambda s: s.replace("\\", "\\\\").replace("'", "\\'")
    R = [
        ('<html lang="en">', f'<html lang="{LANG_HTML[l]}">'),
        ('<title>A Thousand Questions and Answers — The Urantia Book</title>', f'<title>{esc(UI["page_title"])}</title>'),
        ('<meta property="og:title" content="A Thousand Questions and Answers — The Urantia Book">', f'<meta property="og:title" content="{esc(UI["page_title"])}">'),
        ('<meta property="og:description" content="Questions and answers about The Urantia Book">', f'<meta property="og:description" content="{esc(UI["og_description"])}">'),
        ('<meta property="og:url" content="https://urantiafareast.com/en/qna/">', f'<meta property="og:url" content="https://america.urantiareaders.com/{l}/qna/">'),
        ('<h1 id="titleLink">A Thousand Questions and Answers</h1>', f'<h1 id="titleLink">{esc(UI["h1"])}</h1>'),
        ('<div class="sub">Questions and answers about The Urantia Book — choose a question on the left</div>', f'<div class="sub">{esc(UI["sub"])}</div>'),
        ('placeholder="Find a question (number or word)"', f'placeholder="{esc(UI["search_placeholder"])}"'),
        ('<div id="loading" class="loading">Loading…</div>', f'<div id="loading" class="loading">{esc(UI["loading"])}</div>'),
        ('<button class="back-btn" id="backBtn">← All questions</button>', f'<button class="back-btn" id="backBtn">{esc(UI["back"])}</button>'),
        ('<div id="emptyView" class="empty" hidden>No questions yet.</div>', f'<div id="emptyView" class="empty" hidden>{esc(UI["empty"])}</div>'),
        ("const badgeOf = item => item.number ? `Q ${item.number}` : '';", "const badgeOf = item => item.number ? `" + esc(UI["badge"]).replace("{n}", "${item.number}") + "` : '';"),
        ("$('cnt').textContent = `${DATA.length} questions`;", "$('cnt').textContent = `" + UI["count"].replace("{n}", "${DATA.length}") + "`;"),
        ("← Previous ${badgeOf(older)}<b>", esc(UI["prev"]).replace("{badge}", "${badgeOf(older)}") + "<b>"),
        ("Next ${badgeOf(newer)} →<b>", esc(UI["next"]).replace("{badge}", "${badgeOf(newer)}") + "<b>"),
        ("v.replace(/^q\\s*/i, '')", "v.replace(/^(?:q|p|n[ºo°.]?)\\s*/i, '')"),
        ("$('cnt').textContent = v ? `${n} found` : `${DATA.length} questions`;",
         "$('cnt').textContent = v ? `" + UI["found"].replace("{n}", "${n}") + "` : `" + UI["count"].replace("{n}", "${DATA.length}") + "`;"),
        ("'<div class=\"loading\">The questions could not be loaded.</div>'", "'<div class=\"loading\">" + jsq(esc(UI["load_error"])) + "</div>'"),
        ("linkRefs(renderInline(p.trim()), '/en/book/#')", f"linkRefs(renderInline(p.trim()), '/{l}/book/#')"),
    ]
    for a, b in R:
        if a not in t: raise SystemExit("English page changed — not found: " + a[:80])
        t = t.replace(a, b)
    blob = t + json.dumps(out, ensure_ascii=False)
    if HANGUL.search(blob): raise SystemExit(f"[{l}] Hangul left in output")
    if "/en/" in t or "urantiafareast" in t: raise SystemExit(f"[{l}] English-site link left in page")
    assert "/home-button.js" in t
    od = os.path.join(SITE, l, "qna"); os.makedirs(od, exist_ok=True)
    json.dump(out, open(os.path.join(od, "data.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    open(os.path.join(od, "index.html"), "w", encoding="utf-8").write(t)
    refs = sum(len(REF.findall(d["answer"])) for d in out)
    print(f"[{l}] site/{l}/qna: {len(out)} questions, {refs} references → /{l}/book/, {stat['q']} quotations verified")
    return True


ok = all([build(l) for l in LANGS])
sys.exit(0 if ok else 1)
