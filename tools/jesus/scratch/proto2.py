import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\jesus")
from teachings_match import Matcher, tokens
m = Matcher()
U = json.load(open('teach_units.json', encoding='utf-8'))
bins = {}
big = []
for k, (en, ctx) in U.items():
    g, cov = m.match(en)
    n = len(en.split())
    b = min(int(cov * 10), 9)
    bins.setdefault(b, [0, 0]); bins[b][0] += 1; bins[b][1] += n
    if cov >= 0.5 and n >= 15: big.append((cov, n, en[:150], [m.cits[i] for i in g][:3]))
for b in sorted(bins): print(b / 10, bins[b])
big.sort(reverse=True)
print(len(big), sum(x[1] for x in big))
for x in big[:10] + big[len(big)//2:len(big)//2+8] + big[-8:]: print(x)
