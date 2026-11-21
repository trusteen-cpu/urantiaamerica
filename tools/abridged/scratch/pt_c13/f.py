import json,sys
d=json.load(open('../data/pt.json',encoding='utf-8'))
pref=sys.argv[1].split(',') if len(sys.argv)>2 else None
for w in sys.argv[-1].split('|'):
  hits=[(k,v) for k,v in d.items() if w in v and (not pref or any(k.startswith(p+':') for p in pref))]
  print('==',w,len(hits))
  for k,v in hits[:2]:
    i=v.find(w); print('  ',k,'::',v[max(0,i-50):i+70])
