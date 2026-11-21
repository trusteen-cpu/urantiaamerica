import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
AB = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Q = {
 "86.b5.q": "E os Ajustadores divinos, desde então, têm trabalhado para transmutar o temor de Deus em amor a Deus.",
 "89.b16.q": "ensinando-lhe a arte de aumentar a fração que corresponde à sua etapa de vida, diminuindo o denominador das demandas pessoais, em vez de tentar sempre aumentar o numerador da gratificação egoísta.",
 "90.b5.q": "A religião finalmente alcança a compreensão profundamente simples de um amor todo-poderoso",
 "90.b19.q": "A evolução infalivelmente alcança os seus objetivos: ela imbui o homem daquele medo supersticioso do desconhecido e do receio do não visível, e estes são andaimes na construção do conceito de Deus.",
 "92.b36.q": "Mas podem realizar, e algum dia realizarão, a unidade na adoração verdadeira do Pai de todos",
 "93.b5.q": "Eu sou Melquisedeque, sacerdote de El Elyon, o Altíssimo, o único Deus",
 "93.b28.q": "Deus concorda em fazer tudo; o homem apenas concorda em acreditar nas promessas de Deus e em seguir as suas instruções.",
}
todo = json.load(open(os.path.join(AB, "work", "todo_pt_c12.json"), encoding="utf-8"))
for k, v in Q.items():
    assert k in todo
    vt = "".join(list(todo[k]["verses"].values()))
    assert "".join(v.split()) in "".join(vt.split()), k
assert set(Q) == set(todo)
json.dump({k: Q[k] for k in todo}, open(os.path.join(AB, "pt", "quotes_c12.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok", len(Q))
