import json, os
B = os.path.join(os.path.dirname(__file__), '..', '..')
V = json.load(open(os.path.join(B, '..', 'data', 'pt.json'), encoding='utf-8'))
T = json.load(open(os.path.join(B, 'work', 'todo_pt_c06.json'), encoding='utf-8'))

def cut(ref, start, end):
    v = V[ref]
    i = v.index(start)
    j = v.index(end, i) + len(end)
    return v[i:j]

SPEC = {
 "ch28:12": [("A adoração existe", "na verdadeira adoração")],
 "ch28:32": [("A experiência da adoração", "aspirações da alma humana")],
 "ch29:1": [("A prece é o respirar", "a vontade do Pai.")],
 "ch29:8": [("Deus responde à prece", "da experiência humana")],
 "ch29:18": [("de um modo tal que o homem", "o Pai Universal.")],
 "ch29:27": [("A vossa persistência", "para com o espírito.")],
 "ch29:51": [("Todos os pedidos genuínos", "no tempo e no espaço")],
 "ch29:56": [("Não há outra técnica", "Aquele que o criou")],
 "ch30:13": [("O homem sofre, em primeiro lugar", "leis da vida e da luz.")],
 "ch30:29": [("Foi a fé e não o tocar", "carreira terrena de Jesus")],
 "ch30:35": [("foi indicado a nós", "põe fim à ansiedade.")],
 "ch30:37": [("era uma vítima do sentimento", "pegar o seu leito e andar.")],
 "ch30:41": [("ele desejava ensinar", "as doenças humanas.")],
 "ch31:10": [("No entusiasmo de Pentecostes", "estrada de Damasco.")],
 "ch31:39": [("mesmo o cristianismo do século vinte", "para o bem na Terra")],
 "ch32:7": [("Cristo Michael apresentou", "A essência do seu ensinamento foi amor e serviço")],
 "ch32:26": [("O cristianismo, de Paulo,", "para tornar-se um com a divindade")],
 "ch32:32": [("embora o conceito cristão", "às relações espirituais.")],
 "ch32:38": [("Mais cedo ou mais tarde", "no coração daquele que crê")],
 "ch32:42": [("mas devíeis compreender", "oportunidade mais plena para desenvolver-se.")],
 "ch33:2": [("As criaturas de vontade", "reconhecer o Pai Universal.")],
}
out = {}
for k, t in T.items():
    parts = [cut(t['cit'], a, b) for a, b in SPEC[k]]
    out[k] = ' … '.join(parts)
    print(k, len(out[k]), len(t['en']), out[k][:60])
assert set(out) == set(T)
json.dump(out, open(os.path.join(B, 'pt', 'quotes_c06.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
