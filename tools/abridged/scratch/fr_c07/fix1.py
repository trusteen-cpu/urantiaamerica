import json
from save import save, OUT
D=json.load(open(OUT,encoding='utf-8'))
s=D['53.b40.p']
a='les rebelles internés devraient « ⟦Q 53:9.7|47:2.7⟧devenir comme'
b='on s’attend à ce que les rebelles internés « ⟦Q 53:9.7|47:2.7⟧deviendront comme'
a=a.replace('internés','internés')
assert a in s
s=s.replace(a,b)
save({'53.b40.p':s})
print(s)
