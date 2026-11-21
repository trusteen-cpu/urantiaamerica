import io
p='p32.py'; s=io.open(p,encoding='utf-8').read()
R=[("ausente da mente dos seus filhos. Nos universos do espa","ausente da mente dos Seus filhos. Nos universos do espa"),
("Nos universos do espaço ele está","Nos universos do espaço Ele está"),
("na mente dos seus filhos mortais","na mente dos Seus filhos mortais"),
("presente nos seus Filhos (32:3.6)","presente nos Seus Filhos (32:3.6)"),
("\"Pessoalmente presente, mas ausente da mente dos seus filhos\"","\"Pessoalmente presente, mas ausente da mente dos Seus filhos\""),
("pensar nele como","pensar Nele como"),
("que as suas criaturas precisam","que as Suas criaturas precisam"),
("por isso ele se retira","por isso Ele Se retira"),
("nesse retiro, ele participa","nesse retiro, Ele participa"),
("que ordenou (32:4.2)","que Ele ordenou (32:4.2)"),
("fonte da sua personalidade","fonte da personalidade deles"),
("Um fragmento do seu esp","Um fragmento do Seu esp"),
("Deus não é uma personalidade egocêntrica. Ele abriu","Deus não é uma personalidade egocêntrica. Ele abriu"),
("reservou para si, ele dá","reservou para Si, Ele dá"),
("disseminou a si próprio","disseminou a Si próprio"),
("os seus tesouros são nossos","os Seus tesouros são nossos"),
("mas ele está presente no Filho","mas Ele está presente no Filho"),
("deu-se a si próprio a nós, para que possamos ser como ele.","deu-Se a Si próprio a nós, para que possamos ser como Ele."),
]
for a,b in R:
    assert s.count(a)>=1,a; s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
