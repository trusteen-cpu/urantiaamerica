# -*- coding: utf-8 -*-
import json, os, sys
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools")
import amq
D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, "..", "..", "pt", "quotes_c05.json")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
C = [
 ("ch23:9", "2:2.5", "E todo esquema", "nem autocontido"),
 ("ch23:18", "188:4.1", "Embora não haja", "ofendido e implacável"),
 ("ch23:27", "133:6.6", "A salvação é a espiritualização", "valor de sobrevivência."),
 ("ch23:31", "143:2.6", "A salvação se dá", "pela renúncia da carne"),
 ("ch24:34", "101:10.6", "Tal fé proporciona", "progressivo da Deidade."),
 ("ch24:38", "196:0.12", "A fé de Jesus atingiu", "segurança pessoal absoluta."),
 ("ch25:23", "137:8.8", "E eu vos digo", "de modo nenhum."),
 ("ch26:3", "146:3.7", "O caminho da vida terrena", "não perecerá jamais."),
 ("ch26:21", "47:3.1", "Nos mundos das mansões", "de um corpo diferente"),
 ("ch26:26", "112:5.3", "o sistema de energia deve", "do seu livre-arbítrio."),
 ("ch27:7", "5:4.3", "Todas as atividades humanas", "humanos e supra-humanos."),
 ("ch27:16", "103:2.8", "Quando um ser moral", "pode fazer essa escolha"),
 ("ch27:27", "155:5.11", "A religião do espírito", "dos seus crentes formais."),
 ("ch27:40", "101:2.8", "A razão é a prova", "a filosofia gera a unidade"),
 ("ch27:52", "155:6.3", "a experiência superna", "experiência pessoal."),
]
Q = {}
for k, v, a, b in C:
    s = amq.cut("pt", v, a, b)
    assert s, k
    assert amq.check("pt", v, s), k
    Q[k] = s
todo = json.load(open(os.path.join(D, "..", "..", "work", "todo_pt_c05.json"), encoding="utf-8"))
print(set(todo) ^ set(Q) if isinstance(todo, dict) else todo)
json.dump(Q, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(Q))
