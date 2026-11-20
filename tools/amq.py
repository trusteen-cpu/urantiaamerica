# -*- coding: utf-8 -*-
"""Urantia America 공용 인용 도구 — 스페인어·프랑스어·포르투갈어 공식 번역에서 인용을 글자 그대로 잘라 오고 검사한다.
   import sys; sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools"); import amq
   amq.text("es", "1:0.1")                       → 그 절 전체
   amq.cut("es", "1:0.1", "El Padre", "seres.")  → 시작 문구부터 끝 문구까지(끝 문구 포함) 글자 그대로
   amq.check("es", "1:0.1", 인용문)               → 인용문(… 로 줄인 곳 허용)이 그 절에 글자 그대로 있으면 True
   amq.title("fr", 5) / amq.title("fr", 5, 2)    → 편 제목 / 장 제목
   amq.link("pt", "1:0.1")                       → "/pt/book/#1:0.1"
   amq.find("es", "Ajustador del Pensamiento", n=5) → 그 낱말이 나오는 절 번호(용어 확인용)
   명령줄: python amq.py es 1:0.1   (절 보기)  ·  python amq.py es "?Ajustador"  (낱말 찾기)"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
_T, _TT = {}, {}
LANGS = ("es", "fr", "pt")
BOOK = {"es": "El libro de Urantia", "fr": "Le Livre d’Urantia", "pt": "O Livro de Urântia"}


def _load(l):
    if l not in _T:
        _T[l] = json.load(open(os.path.join(HERE, "data", f"{l}.json"), encoding="utf-8"))
        _TT[l] = json.load(open(os.path.join(HERE, "data", f"{l}_titles.json"), encoding="utf-8"))
    return _T[l]


def text(l, cit):
    return _load(l)[cit]


def title(l, paper, sec=None):
    _load(l)
    P = _TT[l][str(paper)]
    return P["title"] if sec is None else P["sec"][str(sec)]


def link(l, cit):
    return f"/{l}/book/#{cit}"


def _norm(s):
    return re.sub(r"\s+", "", s.replace("\u00a0", " "))


def cut(l, cit, start, end=None):
    t = text(l, cit)
    i = t.find(start)
    if i < 0: raise ValueError(f"[{l} {cit}] 시작 문구를 못 찾음: {start!r}")
    if end is None: return t[i:]
    j = t.find(end, i)
    if j < 0: raise ValueError(f"[{l} {cit}] 끝 문구를 못 찾음: {end!r}")
    return t[i:j + len(end)]


def check(l, cit, quote):
    t = _norm(text(l, cit))
    parts = [p for p in re.split(r"\s*(?:…|\.\.\.)\s*", quote) if p.strip()]
    pos = 0
    for p in parts:
        p = _norm(p).strip("«»“”\"'")
        k = t.find(p, pos)
        if k < 0: return False
        pos = k + len(p)
    return True


def find(l, word, n=10):
    d = _load(l)
    return [c for c, v in d.items() if word in v][:n]


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    l, x = sys.argv[1], sys.argv[2]
    if x.startswith("?"):
        for c in find(l, x[1:], 15): print(c, "|", text(l, c)[:160])
    else:
        print(text(l, x))
