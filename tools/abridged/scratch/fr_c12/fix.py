import glob,os,io
H=os.path.dirname(os.path.abspath(__file__))
R=[('coûteuse','couteuse'),('naître','naitre'),('naît','nait')]
for f in glob.glob(os.path.join(H,'p*.py')):
    s=io.open(f,encoding='utf-8').read(); t=s
    for a,b in R: t=t.replace(a,b)
    if t!=s: io.open(f,'w',encoding='utf-8').write(t); print('fixed',f)
