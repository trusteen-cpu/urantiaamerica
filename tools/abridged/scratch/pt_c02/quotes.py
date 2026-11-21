import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
AB = os.path.dirname(os.path.dirname(HERE))
Q = {
 "8.b4.q": "nesse exato momento, o Espírito Infinito começa a existir na sua plenitude.",
 "8.b20.q": "Deus é amor, o Filho é misericórdia, o Espírito é o ministério",
 "8.b33.q": "o Criador Conjunto é, não apenas a Terceira Fonte e Centro, mas também uma Pessoa divina.",
 "8.b37.q": "Ao que tem um ouvido, deixai-o ouvir o que o Espírito diz",
 "9.b16.q": "O Criador Conjunto não é energia, não é a fonte da energia, nem o destino da energia; Ele é o manipulador da energia.",
 "9.b44.q": "o Espírito Infinito é a expressão perfeita da mente do Criador, para todas as criaturas",
 "11.b35.q": "O olho não viu, nem o ouvido escutou, nem entraram ainda na mente do homem mortal as coisas que o Pai Universal preparou para aqueles que sobreviverem à vida na carne",
 "12.b4.q": "o Pai não está longe de cada um de vós; Ele reside dentro de vós",
 "15.b5.q": "a vossa esfera é tão precisamente administrada e fomentada, com tanto e tal amor, que é como se ela fosse o único mundo habitado em toda a existência.",
}
sys.path.insert(0, os.path.dirname(AB))
import amq
todo = json.load(open(os.path.join(AB, "work", "todo_pt_c02.json"), encoding="utf-8"))
assert list(todo) == list(Q), (list(todo), list(Q))
for k, v in Q.items():
    cit = todo[k]["cit"].split("|")[0]
    print(k, amq.check("pt", cit, v))
os.makedirs(os.path.join(AB, "pt"), exist_ok=True)
json.dump(Q, open(os.path.join(AB, "pt", "quotes_c02.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
