import json,sys,re
sys.path.insert(0,'..'); import amq
t=json.load(open('work/todo_fr_c03.json',encoding='utf-8'))
def verses(c):
    m=re.match(r'(\d+):(\d+)\.(\d+)(?:[–-](\d+))?$',c)
    p,s,a,b=m.groups(); b=b or a
    return [f'{p}:{s}.{i}' for i in range(int(a),int(b)+1)]
for k,v in t.items():
    print('=====',k,v['cit'],v['why']); print('EN:',v['en'])
    for c in verses(v['cit']): print('FR',c,':',amq.text('fr',c))
