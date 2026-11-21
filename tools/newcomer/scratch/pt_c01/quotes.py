# -*- coding: utf-8 -*-
import json, os
B = os.path.join(os.path.dirname(__file__), "..", "..")
todo = json.load(open(os.path.join(B, "work", "todo_pt_c01.json"), encoding="utf-8"))
E = "…"
P = {
 "w01:174": [("5. Os Documentos", "fazer essa declaração franca"), E],
 "w01:182": [("Qualquer cosmologia apresentada", "neles.")],
 "w01:239": [("para cada um de vós e para todos nós", "o caminho está aberto"), E],
 "w02:33": [("Não permitais", "o auge da personalidade divina")],
 "w02:57": [("em primeiro lugar, o papel", "um de vós e um convosco"), ("Em segundo lugar está", "de tantas maneiras."), ("E, em terceiro lugar", "humanos de Urântia.")],
 "w02:78": [("A capacidade do Pai", "lugares, ao mesmo tempo.")],
 "w02:90": [("E deveria ser um verdadeiro conforto", "pedir a Ele”.")],
 "w02:106": [("Nada é novo", "em qualquer instante.")],
 "w02:160": [("Ao ponderardes", "a um pai terreno")],
 "w02:196": [("O Pai celeste afetuoso", "o perdão de Pai."), ("Deus, enquanto um Pai", "enquanto juiz.")],
 "w02:200": [("Deus ama o pecador porque", "(potencialmente eterna)"), ("O amor de Deus salva", "destrói o pecado.")],
 "w02:223": [E, ("é verdade que “as coisas", "foram criadas”.")],
 "w02:245": [("Para a ciência", "existe por Si próprio"), ("Contudo, torna-se necessária", "filhos da Terra.")],
 "w02:299": [("O nosso Pai não se esconde", "nos Seus domínios dos universos.")],
 "w02:323": [("Deus dá a escolha soberana", "do arbítrio livre.")],
 "w02:335": [("ainda que eu não possa", "a vossa própria fé”.")],
 "w03:52": [("E, da mesma forma que o fragmento", "avanço espiritual.")],
 "w03:74": [("Os Filhos divinos", "por intermédio do Espírito Infinito")],
 "w03:78": [("na administração dos universos", "distinguir entre Eles."), ("meramente relembrai-vos", "plena de expressão.")],
 "w03:82": [("A Trindade do Paraíso é real.", "do Filho e do Espírito"), ("Pai, Filho e Espírito podem", "como uma Trindade.")],
 "w03:135": [("A Deidade pode causar", "o Paraíso não é uma Deidade")],
 "w03:148": [("Esse é o único conjunto", "Filhos Criadores de Deus")],
 "w03:160": [("ainda que as suas velocidades", "a vigília de uma noite”.")],
 "w03:207": [("Os Sete Espíritos Mestres", "do grande universo.")],
 "w03:223": [("Apenas o Pai Universal", "pelo número.")],
 "w03:266": [("A personalidade é também", "exclusivo do Pai."), ("o Pai Universal é infinito", "da Ilha do Paraíso.")],
 "w03:270": [("A gravidade é a garra", "todas as coisas consistem.")],
 "w04:152": [("Os anjos são os espíritos", "altamente individualizadas."), ("eles possuem naturezas", "dos seres humanos.")],
 "w04:170": [E, ("são os supernafins", "por intermédio do Filho Eterno.")],
 "w04:209": [("A narrativa seguinte", "no universo."), ("escolhemos contar", "raças humanas de Urântia.")],
 "w04:300": [("Os finalitores mortais", "último status do espírito.")],
}
out = {}
for k, v in todo.items():
    verse = v["verse"]
    parts = []
    for p in P[k]:
        if p == E: parts.append(E); continue
        a, b = p
        i = verse.index(a); j = verse.index(b, i) + len(b)
        assert verse.count(a) == 1, (k, a)
        if parts and parts[-1] != E: parts.append(E)
        parts.append(verse[i:j])
    out[k] = " ".join(parts)
assert set(out) == set(todo)
json.dump(out, open(os.path.join(B, "pt", "quotes_c01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
