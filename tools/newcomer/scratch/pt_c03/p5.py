import json, os
from common import QOUT
PT = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\pt.json", encoding="utf-8"))
E = " … "


def c(cit, a, b):
    t = PT[cit]
    i = t.index(a)
    j = t.index(b, i) + len(b)
    return t[i:j]


Q = {
"w10:61": c("99:6.2", "Há um propósito", "da bondade;") + E + c("99:6.2", "elevar os serviços", "a adoração grupal."),
"w10:65": c("99:6.3", "No entanto, quando", "dos sentimentos;") + E + c("99:6.3", "o desvio da religião", "em vez de ministradores;") + E + c("99:6.3", "e a perda gradativa", "da salvação eterna."),
"w10:95": c("107:0.3", "Tendo comandado", "esse Ajustador divino"),
"w10:99": c("107:1.2", "todos estão de acordo", "do Deus infinito.") + E + c("107:1.2", "eles são de Deus", "eles são Deus."),
"w10:103": c("107:0.6", "O Ajustador é a essência", "criatura finita.") + E + c("107:0.6", "O Ajustador é a realidade", "na direção de Deus."),
"w10:107": c("108:5.3", "Os anjos e outros", "sete grupos deles."),
"w10:127": c("110:3.4", "A grande meta", "Ajustador residente;") + E + c("110:3.4", "E, no entanto, um esforço", "êxito na Terra.") + E + c("110:3.4", "a vida ideal", "apreensões temerosas."),
"w10:133": c("107:0.7", "desde a chegada do Ajustador", "Controladores do Pensamento."),
"w10:174": c("111:2.4", "Há três fatores", "são:") + " " + PT["111:2.5"] + " " + c("111:2.6", "2. O espírito divino", "nessa mente humana") + E + PT["111:2.7"],
"w10:190": c("111:3.7", "Todavia, para sempre", "a pena terminar."),
"w10:196": c("112:0.1", "Urântia é o vosso", "guia perfeito;") + E + c("112:0.1", "E, passando por todas", "na presença da mudança."),
"w10:224": c("100:2.7", "Jesus retratou", "absolutamente inatingível"),
"w10:250": c("91:8.11", "Deus responde", "da experiência humana"),
"w10:311": c("117:6.23", "O homem pode descobrir", "de todos os outros homens"),
"w10:315": c("117:6.3", "a sua deidade", "que é amor."),
"w11:59": c("120:1.4", "Na tua outorga", "o Pai Universal de todos."),
"w11:81": c("121:1.1", "Quando Michael encarnou", "desde então."),
"w11:119": c("126:2.2", "Este jovem carpinteiro", "estava para nascer."),
"w11:155": c("132:4.2", "A ênfase da sua mensagem", "fazendo perguntas a elas.") + E + c("132:4.2", "Via de regra, aos que", "ansiosos e tristes"),
"w11:183": c("134:8.8", "Quanto a todos", "seja feita”."),
"w11:206": c("136:2.6", "E esse foi o batismo", "dos assuntos do seu Pai"),
"w11:212": c("136:2.3", "muitos observadores", "muito me comprazo”."),
"w11:232": c("141:5.1", "Vós não tendes que ver", "origem, natureza e destino."),
"w11:242": c("137:8.9", "o Reino do meu Pai", "aí está o Reino do céu."),
"w11:295": c("149:2.4", "Não é da nossa intenção", "fraternidade entre os homens."),
"w11:303": c("196:0.13", "Jesus não exige", "filiação ao Pai celeste."),
"w12:77": c("187:5.6", "Jesus morreu com nobreza", "trágico dia.") + E + c("187:5.6", "Depois de uma vida assim", "“Está acabado”."),
"w12:89": c("188:4.1", "Embora não haja sido", "obtivesse a salvação") + " …",
"w12:97": c("188:4.7", "Embora muito dificilmente", "mais claro e certo") + " …",
"w12:115": c("188:5.9", "A cruz é aquele símbolo", "devoção de amor."),
"w12:148": c("189:2.7", "O sepulcro de José", "dissolução especial e única") + " …",
"w12:160": c("189:4.10", "E enquanto elas pesavam", "“Meu Senhor, e meu Mestre!”"),
"w12:202": c("193:5.2", "Amai aos homens", "como eu servi a vós.") + E + c("193:5.2", "O meu amor vos abriga", "Adeus"),
"w12:224": c("194:3.6", "essa dádiva do espírito", "em todo o mundo.") + E + c("194:3.6", "Afinal, a verdadeira", "individuais dos homens."),
"w12:258": c("196:2.1", "Vós podeis pregar", "ressuscitado e glorificado."),
"w12:283": c("196:0.13", "Jesus não exige", "filiação ao Pai celeste."),
}
todo = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\newcomer\work\todo_pt_c03.json", encoding="utf-8"))
assert set(todo) == set(Q), (set(todo) ^ set(Q))
D = {k: Q[k] for k in todo}
json.dump(D, open(QOUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quotes", len(D))
