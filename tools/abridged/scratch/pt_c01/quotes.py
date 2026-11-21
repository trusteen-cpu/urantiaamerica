# -*- coding: utf-8 -*-
import json
Q = {
"0.b0.q": "Esta introdução não é, pois, uma exposição final e acabada em si, passando, assim, a ser apenas um guia orientador e definidor, destinado a ajudar os leitores dos documentos apresentados a seguir",
"1.b6.q": "Sede perfeitos, assim como Eu sou perfeito",
"2.b63.q": "Deus, enquanto um Pai, transcende Deus, enquanto juiz.",
"3.b6.q": "O homem sai à procura de um amigo, enquanto o verdadeiro amigo vive dentro do seu próprio coração.",
"4.b6.q": "a palavra de ordem do universo deve ser progresso",
"4.b23.q": "a natureza não é Deus. A natureza não é um objeto de adoração.",
"5.b12.q": "Deus é acessível; o Pai é alcançável, o caminho está aberto",
"5.b25.q": "A mente mortal consente em adorar; a alma imortal anseia pela adoração e inicia esse ato; a presença do Ajustador divino conduz essa adoração",
"5.b44.q": "o portal da eternidade abre-se apenas em resposta à escolha, feita em livre-arbítrio, pelos filhos, com livre-arbítrio do Deus do arbítrio livre.",
"6.b7.q": "Deus é o pensamento inicial e o Filho é a palavra plena de expressão.",
"6.b54.q": "o mortal consciente de Deus certamente irá alcançar o Paraíso e, algum dia, chegará à presença pessoal deste grandioso Filho entre os Filhos.",
"6.b56.q": "Deus é amor, o Filho é misericórdia. A misericórdia é o amor aplicado",
"7.b6.q": "O mundo espiritual é o hábito e a conduta pessoal do Filho",
"7.b48.q": "quem tiver visto um Filho do Paraíso, haverá visto o Filho Eterno de Deus.",
}
t = json.load(open('work/todo_pt_c01.json', encoding='utf-8'))
assert set(t) == set(Q), set(t) ^ set(Q)
json.dump({k: Q[k] for k in t}, open('pt/quotes_c01.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok', len(Q))
