import json, os
B = os.path.dirname(os.path.abspath(__file__))
R = os.path.join(B, '..', '..')
Q = {
"78.b5.q": "muito antes de haverem, as cavalarias bárbaras, conquistado o vale, grande parte da cultura do Jardim já se havia propagado até a Ásia, a África e a Europa, para ali produzir os fermentos que resultaram na civilização do século vinte de Urântia.",
"79.b5.q": "a religião, a verdadeira religião, é a fonte indispensável da energia mais elevada que leva os homens a estabelecer uma civilização superior, baseada na fraternidade humana.",
"79.b20.q": "Algum dia porém um Gautama ainda maior pode surgir para liderar toda a Índia, na procura do Deus vivo",
"79.b30.q": "O estímulo de uma religião desenvolvida e avançada, muitas vezes, é um fator decisivo no desenvolvimento cultural",
"80.b5.q": "é uma falácia presumir classificar os povos brancos como sendo nórdicos, alpinos e mediterrâneos.",
"80.b10.q": "foram essas circunstâncias que determinaram os antecedentes da moderna civilização européia.",
"84.b34.q": "esses verdadeiros pais transmitem aos seus filhos a primeira de uma longa série de revelações ascendentes do amor do Pai, do Paraíso, de todos os filhos do universo.",
}
todo = json.load(open(os.path.join(R, 'work/todo_pt_c11.json'), encoding='utf-8'))
pt = json.load(open(os.path.join(R, '../data/pt.json'), encoding='utf-8'))
for k, v in todo.items():
    assert k in Q, k
    ok = any(Q[k] in pt[c] for c in v['cit'].split('|'))
    print(k, ok)
json.dump({k: Q[k] for k in todo}, open(os.path.join(R, 'pt/quotes_c11.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
