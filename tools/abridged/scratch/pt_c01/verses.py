import json,sys
B=json.load(open('../data/pt.json',encoding='utf-8'))
i=json.load(open('work/inline_pt_c01.json',encoding='utf-8'))
t=json.load(open('work/todo_pt_c01.json',encoding='utf-8'))
seen=set()
for k,v in list(i.items()):
  for x in v:
    if x['auto']: continue
    c=x['cit'].split('|')[0]
    print('==',k,c,'|',x['en']); 
    if c not in seen: print(B[c]); seen.add(c)
for k,v in t.items():
  c=v['cit'].split('|')[0]
  print('== TODO',k,c,'|',v['en']); print(B[c])
