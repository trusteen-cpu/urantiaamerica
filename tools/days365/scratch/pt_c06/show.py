import json,sys
d=json.load(open('work/src_c06.json',encoding='utf-8'))
r=json.load(open('work/ref_pt_c06.json',encoding='utf-8'))
a,b=int(sys.argv[1]),int(sys.argv[2])
for k in list(d)[a:b]:
  v=d[k]; print('=====',k,v['_ref'],'|',v['t']); print('PTREF:',' / '.join(r[k]['pt']))
  for i,p in enumerate(v['msg']): print(i,p)
  print('PR',v['pr'])
