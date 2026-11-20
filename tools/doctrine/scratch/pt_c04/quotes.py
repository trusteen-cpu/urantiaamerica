import json, os
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
V = json.load(open(os.path.join(root, '..', 'data', 'pt.json'), encoding='utf-8'))
todo = json.load(open(os.path.join(root, 'work', 'todo_pt_c04.json'), encoding='utf-8'))

C = [
 ("ch17:8", "93:2.1", "Maquiventa outorgou-se", "olhos humanos."),
 ("ch17:25", "93:3.8", "a quem ele tão vividamente", "do Pai do Paraíso."),
 ("ch17:27", "93:8.1", "A decisão de Melquisedeque", "como um ser sobrenatural"),
 ("ch17:44", "96:0.2", "que a religião de um só Deus", "ele pudesse surgir."),
 ("ch17:46", "93:9.10", "E assim, ao perder", "do Filho prometido"),
 ("ch18:5", "119:0.4", "O propósito dessas encarnações", "compreensivos na misericórdia"),
 ("ch18:17", "120:0.4", "Um Filho Criador pode governar", "sete auto-outorgas nos universos."),
 ("ch18:27", "120:1.4", "Na tua outorga de Urântia", "o teu Pai do Paraíso."),
 ("ch18:32", "120:2.8", "Essa tua grande missão", "especialmente às criaturas da carne."),
 ("ch18:36", "129:4.6", "constituindo-se, ao mesmo tempo", "do Criador Infinito."),
 ("ch19:13", "129:4.4", "O Filho do Homem experimentou", "um ser de raro bom humor"),
 ("ch19:41", "140:5.2", "Como Filho de Deus, ele ama", "ama os mortais como um irmão"),
 ("ch19:51", "196:0.13", "Jesus, de um modo muito tocante", "“Siga-me”."),
 ("ch20:3", "139:0.1", "UM TESTEMUNHO", "exaltação pessoal."),
 ("ch20:11", "138:1.1", "Explicou a eles que mais tarde", "com os seus semelhantes."),
 ("ch20:43", "193:4.13", "na personalidade, ele ser isolado", "incapaz de perdoar"),
 ("ch20:46", "193:4.3", "Que Judas não tivesse", "casos de Tomé e de Natanael"),
 ("ch20:54", "192:2.1", "Então, João, deixa de lado", "buscar a salvação."),
 ("ch20:56", "192:2.13", "Nunca esqueçais de que", "pode ser comum."),
 ("ch21:6", "159:5.16", "jamais, antes da vinda de Jesus", "para a casa do Pai."),
 ("ch21:8", "169:1.2", "Mas eu vim mostrar-vos", "Deus está buscando encontrar-vos."),
 ("ch21:11", "169:1.3", "mas vos asseguro que o Pai", "o progresso espiritual."),
 ("ch21:29", "140:5.3", "que eles pudessem começar a ver", "o começo de um afeto paterno."),
 ("ch21:35", "140:5.11", "A mansidão genuína", "um homem cooperando com Deus"),
 ("ch21:42", "159:5.10", "que os seus seguidores devessem ser sábios", "do que o mal mais maligno."),
 ("ch21:52", "159:5.17", "Todavia, a maior força", "uma nova concessão de afeto."),
 ("ch22:14", "179:5.2", "A velha Páscoa comemorava", "como um símbolo da nova dispensação"),
 ("ch22:16", "179:5.6", "pois em todas essas ocasiões", "do crente com Michael."),
 ("ch22:24", "186:5.2", "Foi o homem, e não Deus", "dos acontecimentos humanos em Urântia"),
 ("ch22:27", "182:3.11", "o espírito havia triunfado", "de nutrir dúvidas."),
 ("ch22:34", "187:5.5", "Era um pouco antes das três", "encomendo o meu espírito”."),
 ("ch22:36", "187:5.6", "Jesus morreu com nobreza", "durante todo esse trágico dia."),
]
out = {}
for k, ref, s, e in C:
    v = V[ref]
    i = v.index(s); j = v.index(e, i) + len(e)
    out[k] = v[i:j]
assert set(out) == set(todo), (set(todo) ^ set(out))
out = {k: out[k] for k in todo}
json.dump(out, open(os.path.join(root, 'pt', 'quotes_c04.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(out))
