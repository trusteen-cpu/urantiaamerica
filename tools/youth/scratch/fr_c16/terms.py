import json,re,collections,sys
sys.stdout.reconfigure(encoding='utf-8')
d=json.load(open('../data/fr.json',encoding='utf-8'))
t=' '.join(d.values())
for p in sys.argv[1:]:
  print(p, collections.Counter(re.findall(p,t)).most_common(5))
