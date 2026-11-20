# -*- coding: utf-8 -*-
# 「A Conceptual Overview」 인용 단락 — es/fr/pt 공식 번역에서 amq.cut 으로 글자 그대로 잘라 온다(번역하지 않음).
#   SPEC[(단위 키, 단락 번호)][언어] =
#     None                     → 그 절 전체 (영어 인용이 절 전체일 때)
#     "num"                    → 절 전체에서 맨 앞 "N. " 번호만 뺌 (영어 인용에 번호가 없을 때)
#     (시작, 끝)                → amq.cut(시작, 끝)  (끝=None 이면 절 끝까지)
#     [(시작, 끝), (시작, 끝)]   → 토막들을 " … " 로 이음 (영어의 " ... ")
import os, re, sys

sys.path.insert(0, os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")))
import amq  # noqa: E402

SPEC = {
    ("p2.009.q", 0): {"es": ("El Hijo Eterno es", "Padre Universal."), "fr": ("Le Fils Éternel est", "Père Universel."),
                      "pt": ("O Filho Eterno é", "Pai Universal.")},
    ("p2.031.q", 0): {"es": ("Aunque", "en su función."), "fr": ("Bien que", "seule unité."), "pt": ("Embora", "na sua atuação.")},
    ("p2.043.q", 0): {"es": ("La Primera Fuente", None), "fr": ("La Source-Centre Première", None), "pt": ("A Primeira Fonte", None)},
    ("p3.018.q", 0): {"es": [("Todo impulso", "universo entero."), ("El universo es un todo", "en aislamiento.")],
                      "fr": [("Chaque impulsion", "tout l’univers."), ("L’univers est un tout", "l’isolement.")],
                      "pt": [("Cada impulso", "universo inteiro."), ("O universo é um todo", "em isolamento.")]},
    ("p4.027.q", 0): {"es": ("La cruz", "eterna y amante."), "fr": ("La croix", "de leur salut."), "pt": ("A cruz", "por amor.")},
    ("p4.040.q", 0): {"es": ("Del Padre Universal que habita", None), "fr": ("Du Père Universel qui habite", None),
                      "pt": ("Do Pai Universal que habita", None)},
    ("p4.042.q", 0): {"es": [("Los mortales", "en el universo."), ("Y al visualizar", None)],
                      "fr": [("Les mortels", "service universel."), ("Lorsque nous contemplons", None)],
                      "pt": [("Os mortais", "no universo."), ("Ao contemplarmos", None)]},
    ("p5.005.q", 0): {"es": ("Jesús fundó", "Cristo divino."), "fr": ("Jésus fonda", "au divin Christ."), "pt": ("Jesus fundou", "Cristo divino.")},
    ("p5.007.q", 0): {"es": ("La iglesia, como", "elaborado por Jesús."), "fr": ("L’Église, en tant", "présenté par Jésus."),
                      "pt": ("A igreja, como", "trazido por Jesus.")},
    ("p5.008.q", 0): {"es": ("Así pues", "creyentes espirituales."), "fr": ("Ainsi, durant", "spirituels croyants."),
                      "pt": ("E assim, durante", "espirituais de crença.")},
    ("p5.013.q", 0): {"es": ("En relación con el reino", None), "fr": ("Ses derniers mots", None), "pt": ("A respeito do Reino", None)},
    ("p5.014.q", 0): {"es": ("Para Jesús", None), "fr": ("Pour Jésus", None), "pt": ("Para Jesus", None)},
    ("p5.034.q", 0): {"es": ("Está llegando", None), "fr": ("L’heure est venue", None), "pt": ("É chegada", None)},
    ("p5.035.q", 0): {"es": ("La época", "diecinueve siglos."), "fr": ("Les temps sont", "dix-neuf siècles."), "pt": ("Os tempos", "dezenove séculos.")},
    ("p5.037.q", 0): {"es": [("La religión necesita", "incomparables."), ("que se dedicarán", None)],
                      "fr": [("La religion a besoin", "incomparables enseignements."), ("qui se consacreront", None)],
                      "pt": [("A religião necessita", "incomparáveis."), ("que irão devotar-se", None)]},
    ("p5.042.q", 0): {"es": ("Existe gran esperanza", None), "fr": ("De grands espoirs", None), "pt": ("Há uma grande esperança", None)},
    ("p5.043.q", 0): {"es": ("La triste subdivisión", None), "fr": ("Cette pitoyable", None), "pt": ("Essa subdivisão", None)},
    ("p5.044.q", 0): {"es": ("Pero en esta hermandad", None), "fr": ("Mais, dans cette fraternité", None), "pt": ("Mas, nessa fraternidade", None)},
    ("p6.003.q", 0): {"es": ("La adoración es por", "adoración y oración."), "fr": ("L’adoration se suffit", "l’adoration et la prière."),
                      "pt": ("A adoração existe", "a adoração e a prece.")},
    ("p6.004.q", 0): {"es": ("El orar", "superpensamiento."), "fr": ("La prière est un rappel", "une superpensée."),
                      "pt": ("A prece é como", "o suprapensamento.")},
    ("p6.014.q", 0): {"es": ("La oración primitiva", "paso de las edades."), "fr": ("La prière primitive", "écoulement des âges."),
                      "pt": ("A prece primitiva", "passar das idades.")},
    ("p6.018.q", 0): {"es": ("La oración en desacuerdo", "Deidades del Paraíso."), "fr": ("Les prières incompatibles", "Déités du Paradis."),
                      "pt": ("A prece que é", "Deidades do Paraíso.")},
    ("p6.019.q", 0): {"es": ("La oración no se puede", "del espacio."), "fr": ("On ne doit employer", "de l’espace."),
                      "pt": ("A prece não deve ser", "do espaço.")},
    ("p6.044.q", 0): {"es": ("La comunión directa", "estados psíquicos."), "fr": ("La communion directe", "états psychiques."),
                      "pt": ("A comunhão direta", "estados psíquicos.")},
    ("p6.049.q", 0): {"es": ("El gran desafío", "presencia divina."), "fr": ("Le grand défi", "divine présence."),
                      "pt": ("O grande desafio", "divina presença.")},
}
for i in range(1, 6):  # 144:3.18~22 — 영어 인용에 "1." 번호가 없음
    SPEC[("p6.026.q", i)] = {"es": "num", "fr": "num", "pt": "num"}


def quote(l, key, idx, cit):
    """한 인용 단락의 공식 번역문. 절이 둘이면(공백 구분) 이어 붙인다."""
    sp = SPEC.get((key, idx), {}).get(l)
    cits = cit.split()
    if sp is None:
        return " ".join(amq.text(l, c) for c in cits)
    assert len(cits) == 1, (key, cit)
    c = cits[0]
    if sp == "num":
        return re.sub(r"^\d+\.\s*", "", amq.text(l, c))
    if isinstance(sp, tuple):
        sp = [sp]
    return " … ".join(amq.cut(l, c, a, b) for a, b in sp)


def check(l, cit, text):
    cits = cit.split()
    if len(cits) == 1:
        return amq.check(l, cits[0], text)
    whole = re.sub(r"\s+", "", " ".join(amq.text(l, c) for c in cits))
    return all(re.sub(r"\s+", "", p) in whole for p in re.split(r"\s*…\s*", text) if p.strip())
