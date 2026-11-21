import json
Q = {
"94.b29.q": "A Deidade Absoluta não se esforça em lutas, contudo, é sempre vitoriosa; não força a humanidade, mas permanece sempre pronta para responder aos seus desejos verdadeiros",
"95.b34.q": "Pois, quando três homens falam juntos, Deus está presente como um quarto",
"96.b5.q": "O aspecto mais singular e espantoso da história religiosa dos hebreus diz respeito a essa contínua evolução do conceito da Deidade",
"96.b20.q": "O Deus eterno é o vosso refúgio e ele tem os seus braços eternos por debaixo de vós",
"96.b33.q": "Aquele que orar a Deus receberá o favorecimento dele e, em júbilo, verá a sua face, pois Deus dará ao homem a dádiva da divina retidão",
"97.b5.q": "Deus não esqueceria nem abandonaria",
"97.b10.q": "A Força de Israel não mentirá nem se arrependerá, pois ele não é um homem para poder se arrepender",
"98.b37.q": "Ele deixou, há muito, de ser a religião de Jesus, embora ainda retrate valentemente uma bela religião sobre Jesus",
"99.b26.q": "a verdadeira religião existe para vos fazer conhecer a Deus como o vosso Pai, e ao homem como vosso irmão",
}
todo = json.load(open('work/todo_pt_c13.json', encoding='utf-8'))
assert set(todo) == set(Q), set(todo) ^ set(Q)
json.dump({k: Q[k] for k in todo}, open('pt/quotes_c13.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('quotes', len(Q))
