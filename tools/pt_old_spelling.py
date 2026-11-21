# -*- coding: utf-8 -*-
"""포르투갈어 번역 글을 공식 번역(브라질, 1990 협정 이전 철자)과 같은 철자로 바꾼다.
   import pt_old_spelling as P; P.fix(s)  — ⟦Q⟧…⟦/Q⟧ 인용 부분은 건드리지 않는다.
   python pt_old_spelling.py <json 파일들…>   — 파일 안 모든 문자열(dict 안 "q" 제외)을 고쳐 다시 쓴다."""
import json, re, sys

W = {
    # 강세 (éi, ói)
    "ideia": "idéia", "assembleia": "assembléia", "europeia": "européia", "epopeia": "epopéia", "plateia": "platéia",
    "estreia": "estréia", "geleia": "geléia", "colmeia": "colméia", "odisseia": "odisséia", "panaceia": "panacéia",
    "heroico": "heróico", "heroica": "heróica", "paranoico": "paranóico", "estoico": "estóico", "estoica": "estóica",
    "joia": "jóia", "boia": "bóia", "apoio": None, "jiboia": "jibóia", "androide": "andróide", "asteroide": "asteróide",
    "esferoide": "esferóide", "elipsoide": "elipsóide", "coloide": "colóide", "alcaloide": "alcalóide",
    # 트레마 (ü)
    "cinquenta": "cinqüenta", "frequente": "freqüente", "frequentes": "freqüentes", "frequentemente": "freqüentemente",
    "frequência": "freqüência", "frequências": "freqüências", "consequência": "conseqüência", "consequências": "conseqüências",
    "consequente": "conseqüente", "consequentes": "conseqüentes", "consequentemente": "conseqüentemente",
    "subsequente": "subseqüente", "subsequentes": "subseqüentes", "subsequentemente": "subseqüentemente",
    "sequência": "seqüência", "sequências": "seqüências", "sequencial": "seqüencial", "sequenciais": "seqüenciais",
    "tranquilo": "tranqüilo", "tranquila": "tranqüila", "tranquilos": "tranqüilos", "tranquilas": "tranqüilas",
    "tranquilidade": "tranqüilidade", "eloquente": "eloqüente", "eloquência": "eloqüência", "linguística": "lingüística",
    "linguístico": "lingüístico", "delinquente": "delinqüente", "delinquência": "delinqüência", "quinquagésimo": "qüinquagésimo",
    "aguentar": "agüentar", "ubiquidade": "ubiqüidade", "equidistante": "eqüidistante", "equivalência": None,
    "arguição": "argüição", "unguento": "ungüento", "pinguim": "pingüim", "bilíngue": "bilíngüe", "sagui": None,
    "frequentar": "freqüentar", "frequentado": "freqüentado", "consequencial": "conseqüencial",
    # ^ (êem, ôo)
    "creem": "crêem", "leem": "lêem", "veem": "vêem", "deem": "dêem", "releem": "relêem", "preveem": "prevêem",
    "voo": "vôo", "voos": "vôos", "enjoo": "enjôo", "abençoo": "abençôo", "perdoo": "perdôo",
    # 붙임표
    "autossuficiente": "auto-suficiente", "autossuficiência": "auto-suficiência", "autorrevelação": "auto-revelação",
    "autossacrifício": "auto-sacrifício", "autorrealização": "auto-realização", "autossustentado": "auto-sustentado",
    "antessala": "ante-sala", "contrassenso": "contra-senso", "semirreligioso": "semi-religioso",
    "infraestrutura": "infra-estrutura", "extraordinário": None, "ultrassom": "ultra-som",
    "autorrespeito": "auto-respeito", "autorrevelações": "auto-revelações", "autorreflexão": "auto-reflexão",
    "antirreligioso": "anti-religioso", "contrarreforma": "contra-reforma", "neorrealismo": "neo-realismo",
    "semideus": "semideus",
}
W = {k: v for k, v in W.items() if v and v != k}
_RX = re.compile(r"\b(" + "|".join(sorted(map(re.escape, W), key=len, reverse=True)) + r")(s?)\b", re.I)
MARK = re.compile(r"⟦Q [^⟧]+⟧.*?⟦/Q⟧")


def _one(m):
    w, s = m.group(1), m.group(2)
    r = W.get(w.lower())
    if r is None: return m.group(0)
    if w[0].isupper(): r = r[0].upper() + r[1:]
    if w.isupper(): r = r.upper()
    return r + s


def fix(s):
    out, pos = [], 0
    for m in MARK.finditer(s):
        out.append(_RX.sub(_one, s[pos:m.start()])); out.append(m.group()); pos = m.end()
    out.append(_RX.sub(_one, s[pos:]))
    return "".join(out)


def fix_obj(v):
    if isinstance(v, str): return fix(v)
    if isinstance(v, list): return [fix_obj(x) for x in v]
    if isinstance(v, dict): return {k: (x if k == "q" else fix_obj(x)) for k, x in v.items()}
    return v


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    for p in sys.argv[1:]:
        d = json.load(open(p, encoding="utf-8"))
        n = json.dumps(d, ensure_ascii=False); d2 = fix_obj(d); n2 = json.dumps(d2, ensure_ascii=False)
        json.dump(d2, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(p, "changed" if n != n2 else "same")
