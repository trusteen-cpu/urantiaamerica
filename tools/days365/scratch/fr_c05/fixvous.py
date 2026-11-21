import io,sys
p=sys.argv[1]; s=io.open(p,encoding='utf-8').read()
R=[l.split(' => ') for l in io.open(sys.argv[2],encoding='utf-8').read().splitlines() if ' => ' in l]
for a,b in R:
    n=s.count(a)
    if n!=1: print('COUNT',n,a)
    s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
