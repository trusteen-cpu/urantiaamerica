# -*- coding: utf-8 -*-
# Theology of The Urantia Book — 영어 원고 → 번역 단위 src/cNN.json (스페인어·프랑스어·포르투갈어판 공용)
#   원고(읽기만): E:\OneDrive\유란시아 작업\theology-book\chNN.py · front.py · theo_style.py
#   극동판 tools/zh/theology/extract_src.py 와 같은 키 체계 (chNN.t / .sub / .sum / .sS / .sS.uU.k / .p / .qQ / .qsN, ui.*, front.*, part.N)
#   인용 단위: {"cit": 절 또는 [절,…], "whole": 절 전체 여부, "text": [영어 인용, …]}
#   theology-book 폴더에 __pycache__ 를 만들지 않도록 바이트코드 쓰기를 끈다.
import glob, importlib, json, os, sys
sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
BOOK = r"E:\OneDrive\유란시아 작업\theology-book"
sys.path.insert(0, BOOK)
import theo_style as TS  # noqa: E402
import front as FR  # noqa: E402

# 번역 묶음: 장 범위 (도우미 한 명이 한 묶음)
CHUNKS = {"c01": range(1, 7), "c02": range(7, 13), "c03": range(13, 19), "c04": range(19, 26),
          "c05": range(26, 32), "c06": range(32, 38)}

UI_EN = {
    "ui.ch": "Chapter {}",
    "ui.part": "Part {}",
    "ui.summ": "IN THIS CHAPTER",
    "ui.qs": "Questions for Reflection",
    "ui.toc": "Contents",
    "ui.preface": "Preface",
    "ui.prev": "← Previous",
    "ui.next": "Next →",
    "ui.contents": "Contents",
    "ui.note": "Quotations are taken word for word from the original English text. Click a reference to open the text.",
    "ui.eyebrow_index": "THE URANTIA BOOK",
}


def load_chapters():
    names = sorted(os.path.basename(f)[:-3] for f in glob.glob(os.path.join(BOOK, "ch[0-9][0-9].py")))
    return {importlib.import_module(n).CH["no"]: importlib.import_module(n).CH for n in names}


def chapter_units(ch):
    p = f"ch{ch['no']:02d}"
    D = {f"{p}.t": ch["en_t"], f"{p}.sub": ch["en_sub"], f"{p}.sum": ch["en_sum"]}
    for si, s in enumerate(ch["secs"], 1):
        D[f"{p}.s{si}"] = s["en"]
        for ui, u in enumerate(s["units"], 1):
            b = f"{p}.s{si}.u{ui}"
            D[b + ".k"] = u["en_k"]
            D[b + ".p"] = u["en_p"]
            for qi, (ref, kr, er) in enumerate(u["q"], 1):
                refs = ref if isinstance(ref, list) else [ref]
                D[f"{b}.q{qi}"] = {"cit": ref, "whole": er is None, "text": TS.quote_text("en", ref, er)}
                assert len(D[f"{b}.q{qi}"]["text"]) == len(refs)
    for qi, q in enumerate(ch["en_qs"], 1):
        D[f"{p}.qs{qi}"] = q
    return D


def words(v):
    if isinstance(v, dict): return sum(len(t.split()) for t in v["text"])
    return len(v.split())


def main():
    chs = load_chapters()
    assert sorted(chs) == list(range(1, 38))
    parts = {n: chs[n]["part"]["no"] for n in chs}
    os.makedirs(os.path.join(H, "src"), exist_ok=True)
    for cid, rng in CHUNKS.items():
        D = {}
        if cid == "c01":
            D.update(UI_EN)
            D["front.title"] = FR.TITLE["en"]
            D["front.sub"] = FR.SUB["en"]
            D["front.author"] = FR.AUTHOR["en"]
            for i, para in enumerate(FR.PREFACE["en"], 1):
                D[f"front.preface{i}"] = para
            for n, (_, en) in FR.PARTS.items():
                D[f"part.{n}"] = en
        for n in rng:
            D.update(chapter_units(chs[n]))
        json.dump(D, open(os.path.join(H, "src", cid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        prose = sum(words(v) for v in D.values() if not isinstance(v, dict))
        quote = sum(words(v) for v in D.values() if isinstance(v, dict))
        nq = sum(isinstance(v, dict) for v in D.values())
        print(f"{cid}: ch{rng.start:02d}-ch{rng.stop - 1:02d}  units {len(D)}  prose words {prose}  quotations {nq} ({quote} words)")
    json.dump({str(k): v for k, v in parts.items()}, open(os.path.join(H, "src", "parts.json"), "w", encoding="utf-8"))


main()
