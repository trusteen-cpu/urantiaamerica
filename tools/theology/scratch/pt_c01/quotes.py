# -*- coding: utf-8 -*-
import json, os, sys
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\theology"
sys.path.insert(0, os.path.join(H, ".."))
import amq

def cut(ref, *pieces):
    v = amq.text("pt", ref)
    out = []
    for a, b in pieces:
        i = v.index(a); j = v.index(b, i) + len(b)
        out.append(v[i:j])
    return " … ".join(out)

Q = {
 "ch01.s1.u2.q1#0": cut("1:0.2", ("As miríades", "amá-Lo em retribuição."), ("“Deus criou os céus", "para que fosse habitado”.")),
 "ch01.s1.u3.q1#0": cut("1:0.3", ("As criaturas sabedoras", "“Sede perfeitos, assim como Eu sou perfeito”.")),
 "ch01.s4.u1.q1#0": cut("1:3.1", ("“Deus é espírito”.", "“Deus é espírito”."), ("Ainda que sejais", "mesmo não sendo de carne e osso.")),
 "ch01.s5.u1.q1#0": cut("1:5.1", ("Não permitais", "Ele, que formou o olho, não verá?”"), ("Deus é tanto infinito", "uma personalidade infinita.")),
 "ch02.s2.u3.q1#0": cut("6:8.4", ("O Filho Eterno é infinito", "alcançar o Filho Eterno.")),
 "ch02.s3.u1.q2#0": cut("9:0.2", ("O Agente Conjunto", "do Pai Universal.")),
 "ch02.s3.u3.q1#0": cut("8:6.4", ("“O amor do espírito”", "também uma Pessoa divina."), ("O Espírito fala a vós", "“O próprio Espírito intercede por vós”.")),
 "ch04.s1.u1.q1#0": cut("0:7.1", ("Deus, o Pai; Deus, o Filho;", "expansão evolucionária do universo-mestre.")),
 "ch04.s3.u3.q1#0": cut("117:4.13", ("E, assim, de cada um", "que tanto depende de cada criatura?")),
 "ch04.s4.u3.q1#0": cut("106:9.12", ("Para as criaturas materiais", "dominada pela bondade.")),
}
for k, v in Q.items():
    print(k, v[-60:])
json.dump(Q, open(os.path.join(H, "pt", "quotes_c01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
