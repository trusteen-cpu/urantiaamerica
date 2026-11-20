# -*- coding: utf-8 -*-
# Core Doctrines of The Urantia Book — 영어 원고 → 번역 단위 src/cNN.json (스페인어·프랑스어·포르투갈어판 공용)
#   원고(읽기만): E:\OneDrive\유란시아 작업\doctrine-book\en\ch00_en.json … ch33_en.json, book_style_en.AUDIO_TITLE
#   (극동판 tools/build_doctrine.py 가 site/en/doctrine/ 을 만드는 그 원고; 극동판 tools/zh/doctrine/extract_src.py 와 같은 키 체계)
#   단위 키:  part:<1-7> · audio:<NN> · chNN:label · chNN:title · chNN:sub · chNN:<블록 번호>
#   블록:  "글"(문단·소제목) · {"q": 영어 인용, "cit": 절} · {"cap", "rows"} 표 · {"title", "items"} 생각해 볼 질문
#   src/ 는 손으로 고치지 않는다. 다시 뽑으려면 이 파일을 실행.
import json, os, re, sys
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
BOOK_EN = r"E:\OneDrive\유란시아 작업\doctrine-book\en"
sys.path.insert(0, BOOK_EN)
from book_style_en import AUDIO_TITLE  # noqa: E402

# 번역 묶음: 장 범위 (도우미 한 명이 한 묶음·한 언어)
CHUNKS = {"c01": range(0, 6), "c02": range(6, 12), "c03": range(12, 17), "c04": range(17, 23),
          "c05": range(23, 28), "c06": range(28, 34)}


def wc(x):
    if isinstance(x, str): return len(re.findall(r"\S+", x))
    if isinstance(x, list): return sum(wc(i) for i in x)
    if isinstance(x, dict): return sum(wc(v) for k, v in x.items() if k != "cit")
    return 0


def load(n):
    return json.load(open(os.path.join(BOOK_EN, f"ch{n:02d}_en.json"), encoding="utf-8"))


def split_title(n, d):
    return d["title"].partition(": ") if n not in (0, 33) else (d["title"], "", "")


def units(n, d):
    U = {}
    k = f"ch{n:02d}"
    t, _, s = split_title(n, d)
    U[k + ":label"] = d["label"]; U[k + ":title"] = t
    if s: U[k + ":sub"] = s
    for i, b in enumerate(d["C"]):
        if b[0] in ("h", "p"): U[f"{k}:{i}"] = b[1]
        elif b[0] == "q": U[f"{k}:{i}"] = {"q": b[1], "cit": b[2]}
        elif b[0] == "tt": U[f"{k}:{i}"] = {"cap": b[1], "rows": b[2]}
        elif b[0] == "box": U[f"{k}:{i}"] = {"title": b[1], "items": b[2]}
        elif b[0] == "audio": pass                     # 오디오북 번호만 — 번역할 글 없음 (제목은 audio:NN)
        else: raise SystemExit(f"unknown block {b[0]} in ch{n:02d}")
    return U


def main():
    os.makedirs(os.path.join(H, "src"), exist_ok=True)
    parts = {}
    for n in range(34):
        p = load(n)["part"]
        if p[0]: parts.setdefault(f"part:{p[0]}", p[1])
    stats = {}
    for cid, rng in CHUNKS.items():
        D = {}
        if cid == "c01":
            D.update(parts)
            D.update({f"audio:{a}": t for a, t in sorted(AUDIO_TITLE.items())})
        for n in rng: D.update(units(n, load(n)))
        json.dump(D, open(os.path.join(H, "src", cid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        q = [v for v in D.values() if isinstance(v, dict) and "cit" in v]
        stats[cid] = dict(chapters=f"ch{rng.start:02d}-ch{rng.stop - 1:02d}", units=len(D), quotes=len(q),
                          words_to_translate=wc(list(D.values())) - sum(wc(v["q"]) for v in q))
        print(cid, stats[cid])
    json.dump(stats, open(os.path.join(H, "src", "_stats.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
