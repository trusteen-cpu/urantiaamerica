# -*- coding: utf-8 -*-
# 영어판 주제별 연구 원고(urantiafareast 홈페이지/tools/topics_en/data/tNNN.json, 읽기만 함)에서 번역 단위를 뽑는다.
#   src/cNN.json   : 주제 10개씩(c01 = 1–10 …, c10 = 91–100). 산문 단위만(문자열).
#   src/quotes.json: 인용 단위 {키: {"cit": 절, "q": 영어 인용}}  — 번역하지 않고 공식 번역에서 잘라 온다(align_quotes.py, quotes_spec.py).
#   단위 키: tNNN.t (주제 이름) · tNNN.sum (개요) · tNNN.sK.h (소제목) · tNNN.sK.iJ (항목; K·J 는 1부터)  — 극동판 중국어판과 같은 규칙.
import glob, json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
EN_DIR = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\topics_en\data"


def units(D, n):
    U = {f"t{n:03d}.t": D["t"], f"t{n:03d}.sum": D["sum"]}
    for k, s in enumerate(D["sections"], 1):
        U[f"t{n:03d}.s{k}.h"] = s["h"]
        for j, it in enumerate(s["items"], 1):
            key = f"t{n:03d}.s{k}.i{j}"
            U[key] = {"cit": it["r"], "q": it["q"]} if "q" in it else it["x"]
    return U


def load_en():
    files = sorted(glob.glob(os.path.join(EN_DIR, "t*.json")))
    assert len(files) == 100, len(files)
    return {int(os.path.basename(f)[1:4]): json.load(open(f, encoding="utf-8")) for f in files}


if __name__ == "__main__":
    EN = load_en()
    os.makedirs(os.path.join(H, "src"), exist_ok=True)
    Q = {}
    for c in range(10):
        P = {}
        for n in range(c * 10 + 1, c * 10 + 11):
            for k, v in units(EN[n], n).items():
                if isinstance(v, dict): Q[k] = v
                else: P[k] = v
        json.dump(P, open(os.path.join(H, "src", f"c{c + 1:02d}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(f"c{c + 1:02d}: prose units {len(P)}, words {sum(len(v.split()) for v in P.values())}")
    json.dump(Q, open(os.path.join(H, "src", "quotes.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("quotations", len(Q))
