p='p3.py';s=open(p,encoding='utf-8').read()
R=[("na cruz⟦/Q⟧”. “⟦Q 186:5.2⟧o Pai no","na cruz⟦/Q⟧”. E acrescenta que “⟦Q 186:5.2⟧o Pai no"),
("do seu Filho⟦/Q⟧.” Tudo","do seu Filho⟦/Q⟧”. Tudo"),
("mesmo então, “⟦Q 187:4.2⟧Em","mesmo então: “⟦Q 187:4.2⟧Em"),
("Quando o jovem bandido pendurado","O jovem bandido pendurado")]
for a,b in R:
    assert s.count(a)==1,a; s=s.replace(a,b)
open(p,'w',encoding='utf-8').write(s)
