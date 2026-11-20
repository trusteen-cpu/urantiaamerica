import json, os, sys
sys.path.insert(0, '..')
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
V = json.load(open('../data/es.json', encoding='utf-8'))

def cut(ref, start, end):
    v = V[ref]
    i = v.index(start)
    j = v.index(end, i) + len(end)
    return v[i:j]

Q = {
 "ch12:9": cut("111:2.8", "el impulso de la mente finita", "la experiencia de la criatura."),
 "ch12:11": cut("111:2.2", "La mente material del hombre mortal", "significados divinos"),
 "ch12:16": cut("111:2.9", "Esta transacción excelsa", "las realidades superanimales"),
 "ch12:18": cut("111:2.10", "el nacimiento gradual de un alma", "el Monitor Misterioso."),
 "ch12:32": cut("111:3.7", "Siempre y cuando", "se volverá indestructible."),
 "ch12:34": cut("111:3.2", "Durante la vida la voluntad mortal", "la entidad emergente alma morontial"),
 "ch13:16": cut("62:6.5", "cuando, al año,", "ya reconocidas como humanas."),
 "ch14:24": cut("64:6.14", "Como desarrollaron un espíritu fraternal", "iba expandiéndose en Asia."),
 "ch15:10": cut("53:2.5", "Debe haber existido", "si no del universo entero."),
 "ch15:19": cut("53:5.7", "la vida material corre peligro", "en términos de vida eterna."),
 "ch15:29": cut("54:3.1", "La habilidad del hombre", "esta libertad de otorgamiento divino"),
 "ch15:49": cut("67:7.5", "pero jamás el pecado", "del individuo mismo."),
 "ch16:5": cut("51:3.3", "Un Adán y Eva Planetarios", "a los hijos del tiempo."),
 "ch16:8": cut("51:5.6", "Cuando este linaje", "de la lucha anterior."),
 "ch16:49": cut("76:5.7", "sino que el mal y el pecado", "del Padre Paradisiaco."),
}
os.makedirs('es', exist_ok=True)
json.dump(Q, open('es/quotes_c03.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(Q))
