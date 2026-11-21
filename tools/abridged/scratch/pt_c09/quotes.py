import json, os
H = os.path.dirname(os.path.abspath(__file__))
B = os.path.normpath(os.path.join(H, '..', '..'))
todo = json.load(open(os.path.join(B, 'work', 'todo_pt_c09.json'), encoding='utf-8'))
def cut(key, verse, start, end):
    v = todo[key]['verses'][verse]
    i = v.index(start); j = v.index(end, i) + len(end)
    return v[i:j]
Q = {
 "65.b5.q": cut("65.b5.q", "65:8.5", "se o indiv", "obstáculos do tempo."),
 "66.b10.q": cut("66.b10.q", "66:1.5", "E eu não compreendi", "orgulho da personalidade."),
 "67.b5.q": cut("67.b5.q", "67:7.5", "o pecado de um ser qualquer", "sobrevivência da personalidade."),
}
assert set(Q) == set(todo)
json.dump(Q, open(os.path.join(B, 'pt', 'quotes_c09.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in Q.items(): print(k, v.encode('ascii', 'backslashreplace').decode())
