# -*- coding: utf-8 -*-
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.abspath(os.path.join(HERE, "..", ".."))
Q = {
"71.b35.q": "A educação é a ocupação maior da vida; deve continuar durante toda a vida",
"72.b5.q": "Eles tornaram-se civilizados a ponto de poder defender vigorosamente a civilização",
"73.b5.q": "O Éden era o único local luminoso em Urântia",
"73.b19.q": "Dos seus confins para o lado exterior, o mundo permanecia nas trevas, na ignorância e selvageria. O Éden era o único local luminoso em Urântia",
"73.b35.q": "eles deviam mobilizar-se para outorgar-se, generosamente, às raças necessitadas da Terra.",
"75.b5.q": "A perfeição é a nossa meta eterna, não a nossa origem.",
"75.b22.q": "se constituiu no mal, porque representava o caminho errado de se alcançar fins probos, pois se distanciava do caminho certo, o plano divino.",
"76.b27.q": "vós sereis chamados do abraço do sono mortal, quando eu vier a Urântia, caso os Filhos subordinados do meu Reino não vos buscarem antes dessa época",
}
todo = json.load(open(os.path.join(AB, "work", "todo_pt_c10.json"), encoding="utf-8"))
assert set(todo) == set(Q), (set(todo) ^ set(Q))
json.dump({k: Q[k] for k in todo}, open(os.path.join(AB, "pt", "quotes_c10.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quotes", len(Q))
