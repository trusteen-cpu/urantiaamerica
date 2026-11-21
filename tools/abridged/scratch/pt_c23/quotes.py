import json
Q = {
 "177.b5.q": "Mesmo um adolescente, se o desejo do seu coração é realmente supremo, pode atrair a atenção, desfrutar da companhia plena de amor do Deus de um universo",
 "177.b25.q": "Na sua mente Judas ansiava por honras terrenas, e chegou a amar esse desejo de todo o seu coração",
 "178.b14.q": "é como a semente do ser vivo, que, de geração para geração, ao mesmo tempo em que permanece sendo a mesma semente viva, se desdobra infalivelmente em novas manifestações",
 "178.b26.q": "Como o Pai enviou-me a este mundo, e estou pronto para enviar-vos adiante para que me representeis e termineis a obra inicada por mim.",
 "180.b32.q": "É realmente proveitoso para vós que eu me vá. Se eu não for embora, o novo instrutor não poderá vir até os vossos corações.",
 "181.b10.q": "Neste mundo vós tereis tribulações, mas tendes coragem e alegria; eu triunfei no mundo e vos mostrei o caminho do júbilo e do serviço eterno",
 "181.b20.q": "Vós sois apenas homens finitos, mortais, e aquilo que eu vos ensinei é infinito, divino e eterno. Sede pacientes e tende coragem",
 "182.b25.q": "o espírito havia triunfado sobre a carne; e a fé havia-se afirmado acima de todas as tendências humanas de temer ou de nutrir dúvidas.",
 "183.b11.q": "Aquelas experiências desumanas e chocantes, que Jesus foi levado a suportar, nas horas finais da sua vida mortal, não eram, de modo algum, parte da vontade divina do Pai",
 "185.b5.q": "o meu Reino é a família, pela fé, dos filhos do meu Pai que está no céu.",
 "185.b17.q": "Com esse propósito eu nasci neste mundo, para que pudesse mostrar o Pai a todos os homens e dar o testemunho da verdade de Deus.",
}
base = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged"
d = json.load(open(base + r"\data_check_dummy", encoding="utf-8")) if False else None
pt = json.load(open(r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\pt.json", encoding="utf-8"))
t = json.load(open(base + r"\work\todo_pt_c23.json", encoding="utf-8"))
assert set(t) == set(Q)
for k, v in Q.items():
    vs = t[k]["cit"].split("|")[0]
    assert v in pt[vs], k
json.dump(Q, open(base + r"\pt\quotes_c23.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("ok")
