import json, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
t = json.load(open('work/todo_pt_c21.json', encoding='utf-8'))
def V(k): return t_all[k]
t_all = {}
for v in t.values(): t_all.update(v['verses'])
def cut(k, start, end):
    s = V(k); i = s.index(start); j = s.index(end, i) + len(end); return s[i:j]
Q = {
 '159.b5.q': cut('159:1.2', 'Na vossa religi', 'arrependimento.'),
 '159.b25.q': cut('159:4.8', 'A criatura pode', 'a possuem.'),
 '160.b26.q': cut('160:4.16', 'a sabedoria sempre', 'a cultura.'),
 '161.b14.q': cut('161:1.8', 'Que a personalidade de Jesus', 'no homem.'),
 '162.b5.q': cut('162:7.2', 'Vós conhecereis a verdade', 'homens livres.'),
 '162.b23.q': cut('162:5.2', 'Eu sou a luz', 'luz da vida.'),
 '162.b34.q': cut('162:8.3', 'as questões menos', 'Reino celeste'),
 '163.b5.q': cut('163:6.7', 'Vinde a mim', 'o descanso.'),
 '163.b11.q': cut('163:1.4', 'Livremente vós', 'dai livremente.'),
 '163.b34.q': cut('163:6.2', 'não vos sintais', 'listas do céu'),
 '164.b5.q': cut('164:4.9', 'de uma coisa eu sei', 'agora eu vejo'),
 '164.b12.q': cut('164:1.3', 'Vai e faze', 'mesmo modo'),
 '164.b29.q': cut('164:5.3', 'assim como o Pai reside', 'neste evangelho'),
 '165.b5.q': cut('165:5.3', 'Buscai a coisa', 'encontradas nela'),
 '165.b14.q': cut('165:2.8', 'eu vim para que', 'mais abundantemente.'),
 '165.b18.q': cut('165:3.8', 'o Pai nunca obriga', 'no Reino.'),
 '165.b29.q': cut('165:5.3', 'pedi pelo celeste', 'seguirá a essência.'),
 '166.b5.q': cut('166:4.10', 'a saúde não é', 'desagrado de Deus.'),
 '166.b20.q': cut('166:3.3', 'Mesmo a porta', 'esta porta.'),
 '167.b5.q': cut('167:1.5', 'aquele que se exalta', 'será exaltado.'),
}
assert set(Q) == set(t)
json.dump(Q, open('pt/quotes_c21.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
for k, v in Q.items(): print(k, v)
