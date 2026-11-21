import json
p="es/c05.json"; D=json.load(open(p,encoding="utf-8"))
m=D["d104"]["msg"]; s=m[5]
a="hacia el ser verdaderos adoradores"; assert a in s
m[5]=s.replace(a,"hasta llegar a ser verdaderos adoradores")
json.dump(D,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
