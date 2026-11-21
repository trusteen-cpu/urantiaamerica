import json
from save import save, OUT
D=json.load(open(OUT,encoding='utf-8'))
s=D['53.b40.p']
a='Lorsqu’il sera rendu, on s’attend à ce que les rebelles'
b='On prévoit que, lorsqu’il sera rendu, les rebelles'
assert a in s
save({'53.b40.p':s.replace(a,b)})
