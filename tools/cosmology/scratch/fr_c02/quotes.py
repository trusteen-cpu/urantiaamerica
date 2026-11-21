# -*- coding: utf-8 -*-
import json,sys
sys.path.insert(0,'..');import amq
c=lambda cit,a,b=None: amq.cut('fr',cit,a,b)
Q={
"w02.017":c("16:3.1","en tant qu’expressions primaires","superuniverselle."),
"w02.021":c("56:6.2","En tant que personne, Dieu","niveaux spirituels."),
"w02.051":c("1:0.3","Du Père Universel qui habite","je suis parfait. »"),
"w02.074":c("1:0.6","Cette recherche sublime"),
"w02.106":c("115:7.1","et le Suprême n’a pu connaitre"),
"w02.113":c("56:6.2","Les réalités de personnalité","grand univers."),
"w02.115":c("17:2.2","Cette union du pouvoir","Être Suprême."),
"w02.134":c("28:6.8","vous devriez comprendre dès maintenant","puis bon."),
"w02.137":c("8:4.2","Dieu est amour","est ministère"),
"w02.184":c("22:7.10","Les Sept Maitres Esprits","couronnées de succès."),
"w02.186":c("32:3.12","En réalité, les créatures","totalité finie."),
"w02.220":c("21:6.1","Toutefois, en observant","plus que finie"),
"w02.246":c("9:1.7","un être provisoirement subordonné","dans l’action."),
"w03.019":c("8:1.8","Et il confirme simplement"),
"w03.029":c("117:7.4","2. Le Suprême ne pourrait","réalité qualifiée"),
"w03.042":c("31:10.13","Et beaucoup d’entre nous spéculent"),
"w03.047":c("12:1.11","Le système Paradis-Havona","maitre univers."),
"w03.074":c("106:3.2","mais l’apparition du Tout-Puissant","Architectes du Maitre Univers."),
"w03.110":c("119:8.8","la demeure humaine de Christ Micaël","chair mortelle"),
"w03.112":c("119:8.6","Micaël, Fils Créateur, est"),
"w03.114":c("21:6.3","la liaison entre un Maitre Fils","niveaux absonites de service"),
"w03.134":c("0:12.5","Les deux Trinités","réalisation dans l’univers."),
"w03.178":c("21:3.14","mais ils pourraient le faire"),
"w03.182":c("31:10.19","On croit de plus en plus","espace extérieur"),
}
t=json.load(open('work/todo_fr_c02.json',encoding='utf-8'))
assert list(t)==list(Q),set(t)^set(Q)
for k in t: assert amq.check('fr',t[k]['cit'],Q[k]),k
json.dump(Q,open('fr/quotes_c02.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',len(Q))
