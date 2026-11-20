import json, os
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(H, "..", "..")
PT = json.load(open(os.path.join(T, "..", "data", "pt.json"), encoding="utf-8"))
TODO = json.load(open(os.path.join(T, "work", "todo_pt_c05.json"), encoding="utf-8"))

def piece(v, a, b):
    i = v.index(a)
    if b is None:
        return v[i:]
    j = v.index(b, i) + len(b)
    return v[i:j]

C = {
 "ch26.s1.u3.q1#0": [("A sua vinda", None)],
 "ch26.s2.u3.q1#0": [("Se bem que", "carne e do sangue."), ("Mesmo Abraão", "sacrifício convencional.")],
 "ch27.s2.u2.q2#0": [("Conquanto Moisés", "Horeb e do deserto.")],
 "ch27.s3.u1.q1#0": [("Nessa época", "estava proclamada.")],
 "ch28.s1.u2.q1#0": [("Tendo promulgado", "de reabilitação.")],
 "ch28.s3.u3.q1#0": [("Jesus aboliu", "filhas mortais.")],
 "ch29.s1.u2.q1#0": [("Por conseguinte", "auto-outorgas nos universos.")],
 "ch29.s3.u1.q2#0": [("Atenção, todavia!", "revelação do Pai à alma.")],
 "ch29.s3.u3.q2#0": [("A fé de Jesus", "de uma criança."), ("Nessa inteligência", "consciência religiosa."), ("Não obstante", "nenhum sentido.")],
 "ch29.s4.u1.q1#0": [("Jesus não exige", "Pai celeste."), ("Jesus, de um modo", "“Siga-me”.")],
 "ch29.s4.u3.q1#0": [("A cruz é aquele", "devoção de amor.")],
 "ch30.s1.u2.q1#0": [("João perguntou", "de ser como Deus.")],
 "ch31.s1.u2.q1#0": [("Do modo como vivi", "Reino do espírito."), ("Como o meu Pai", "toda a verdade.")],
}
out = {}
for k, info in TODO.items():
    v = PT[info["cit"]]
    out[k] = " … ".join(piece(v, a, b) for a, b in C[k])
    print(k, "|", out[k], "\n")
json.dump(out, open(os.path.join(T, "pt", "quotes_c05.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), len(TODO))
