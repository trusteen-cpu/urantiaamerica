# 새 독자 안내서(A New Reader's Guide to The Urantia Book) 스페인어·프랑스어·포르투갈어판 — 영어 원고에서 번역 단위 뽑기
#   극동판 tools/zh/newcomer/extract_src.py 를 옮긴 것(키 형식 그대로: "<파일>:<줄번호>", "ui:<이름>", "terms:<영어 낱말>").
#   원고: E:\OneDrive\유란시아 작업\newreader-book\en\wNN.md · closing.md · reading.md · wNN_terms.tsv, front_en\{preface,howto,colophon}.md
#   결과: src/c01..c03.json (영어 단위; 묶음을 1만2천~1만6천 낱말로 다시 나눔). 다시 돌리면 src/ 를 새로 쓴다(<l>/ 는 건드리지 않음).
#   build_newcomer_am.py 가 영어 원고를 다시 읽고 같은 줄을 번역 단위로 바꿔 끼운다(머리표 #, -, 1., >, ::: 는 빌더가 붙인다).
import csv, glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
BOOK = r"E:\OneDrive\유란시아 작업\newreader-book"

FILES = ([("preface", os.path.join(BOOK, "front_en", "preface.md")), ("howto", os.path.join(BOOK, "front_en", "howto.md"))]
         + [(f"w{n:02d}", os.path.join(BOOK, "en", f"w{n:02d}.md")) for n in range(1, 13)]
         + [("closing", os.path.join(BOOK, "en", "closing.md")), ("reading", os.path.join(BOOK, "en", "reading.md")),
            ("colophon", os.path.join(BOOK, "front_en", "colophon.md"))])
QRE = re.compile(r"^>\s*(.+?)\s*\[([\d:.\-–, ]+)\]\s*$")
# 아메리카판에는 영어 오디오북(같은 주 12장 낭독 슬라이드)을 싣지 않는다(극동판 중국어판과 같이). 그 안내 줄은 번역 단위에서 빼고 빌더도 건너뛴다.
SKIP = lambda name, s: name == "howto" and s.startswith("- **Companion audiobook**")


def read(p):
    return open(p, encoding="utf-8-sig").read().splitlines()


def units(name, lines):
    """줄 → (키, 값). 값: 문자열, 표 줄은 [칸…], 인용은 {"q":…, "cit":…}, @part 는 [제목, 부제]."""
    out = []
    for i, l in enumerate(lines, 1):
        s = l.strip(); k = f"{name}:{i}"
        if not s or s == ":::" or SKIP(name, s): continue
        if s.startswith(":::"):
            kind = s[3:].strip()
            if kind.startswith("box") and kind[3:].strip(): out.append((k, kind[3:].strip()))
            continue
        if s.startswith("@part"):
            t, _, sub = s[5:].strip().partition("|"); out.append((k, [re.sub(r"\s{2,}", " ", t.strip()), sub.strip()])); continue
        m = re.match(r"^# Week \d+\s+(.+)", s)
        if m: out.append((k, m.group(1).strip())); continue
        if s.startswith("Text:"): out.append((k, s[5:].strip())); continue
        for p in ("### ", "## ", "# "):
            if s.startswith(p): out.append((k, s[len(p):])); break
        else:
            m = re.match(r"^\[\[Figure\s*\|\s*([^|]+?)\s*\|\s*(.+?)\]\]$", s)
            if m: out.append((k, m.group(2))); continue
            if s.startswith("Table:"): out.append((k, s[6:].strip())); continue
            if s.startswith("|"):
                if not set(s) <= set("|-: "): out.append((k, [c.strip() for c in s.strip("|").split("|")]))
                continue
            if s.startswith(">"):
                m = QRE.match(s)
                out.append((k, {"q": m.group(1), "cit": m.group(2)} if m else s.lstrip("> "))); continue
            if s.startswith("- "): out.append((k, s[2:])); continue
            if re.match(r"^\d+\.\s", s): out.append((k, re.sub(r"^\d+\.\s+", "", s))); continue
            out.append((k, s))
    return out


def term_rows():
    """부록 1 낱말: {영어 낱말: (뜻풀이, 처음 나온 주 번호)} — 영어 알파벳 순서."""
    T = {}
    for f in sorted(glob.glob(os.path.join(BOOK, "en", "w[0-9][0-9]_terms.tsv"))):
        for row in csv.reader(open(f, encoding="utf-8-sig"), delimiter="\t"):
            if len(row) >= 3 and row[0].strip() and row[0].strip().lower() not in {k.lower() for k in T}:
                m = re.search(r"\d+", row[3] if len(row) > 3 else "")
                T[row[0].strip()] = (row[2].strip(), int(m.group()) if m else 0)
    return dict(sorted(T.items(), key=lambda x: x[0].lower()))


def terms():
    return [(f"terms:{t}", {"term": t, "def": d}) for t, (d, _) in term_rows().items()]


# 화면 글자(UI). 값은 영어판 그대로 — 번역자가 바꾼다. {n} {week} {text} 자리표시는 남긴다.
UI = {
 "ui:title": "A New Reader's Guide to The Urantia Book",
 "ui:sub": "Twelve Weeks on the Great Road of the Revelation",
 "ui:eyebrow_index": "THE URANTIA BOOK",
 "ui:author": "Jay Han",
 "ui:contents": "Contents",
 "ui:sec_preface": "PREFACE",
 "ui:sec_howto": "HOW TO USE THIS BOOK",
 "ui:sec_contents": "CONTENTS",
 "ui:week_label": "Week {n}",
 "ui:week_eyebrow": "WEEK {n}",
 "ui:text_label": "Text: {text}",
 "ui:figure_label": "Figure {week}.{n}",
 "ui:figure_label_nw": "Figure {n}",
 "ui:table_label": "Table {week}.{n}",
 "ui:table_label_nw": "Table {n}",
 "ui:box_points": "Key Points This Week",
 "ui:box_questions": "Questions to Consider",
 "ui:box_next": "Read for Next Week",
 "ui:part_after": "Afterword and Appendices",
 "ui:appx1": "Appendix 1. New Words",
 "ui:appx1_intro": "The terms introduced in this book, in alphabetical order. The week in parentheses is where the term first appears.",
}

CHUNKS = {"c01": ["ui", "preface", "howto", "w01", "w02", "w03", "w04"],
          "c02": ["w05", "w06", "w07", "w08", "w09"],
          "c03": ["w10", "w11", "w12", "closing", "reading", "colophon", "terms"]}


def words(v, quotes=False):
    if isinstance(v, dict):
        if "q" in v: return len(v["q"].split()) if quotes else 0
        return sum(words(x) for x in v.values())
    if isinstance(v, list): return sum(words(x) for x in v)
    return len(re.sub(r"<[^>]+>", " ", v).split())


def main():
    by = {name: units(name, read(p)) for name, p in FILES}
    by["terms"] = terms(); by["ui"] = list(UI.items())
    assert sorted(sum(CHUNKS.values(), [])) == sorted(by), "chunk map incomplete"
    os.makedirs(os.path.join(H, "src"), exist_ok=True)
    rep = {}
    for c, names in CHUNKS.items():
        D = {k: v for n in names for k, v in by[n]}
        json.dump(D, open(os.path.join(H, "src", c + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        rep[c] = dict(units=len(D), prose_words=sum(words(v) for v in D.values()),
                      quotation_words=sum(words(v, True) for v in D.values() if isinstance(v, dict)),
                      quotations=sum(1 for v in D.values() if isinstance(v, dict) and "q" in v), files=names)
        print(c, rep[c])
    json.dump(rep, open(os.path.join(H, "src", "_stats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
