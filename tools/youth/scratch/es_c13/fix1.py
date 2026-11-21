import io,re
def sub(fn,old,new):
    s=io.open(fn,encoding='utf-8').read(); assert old in s,(fn,old); io.open(fn,'w',encoding='utf-8').write(s.replace(old,new))
q=lambda c:'\u27e6Q '+c+'\u27e7\u27e6/Q\u27e7'
import json
Q=json.load(open('../../work/quotes_es_c13.json',encoding='utf-8'))
def auto(k,i): return Q[k][i]['auto'].rstrip('.')
sub('part02.py',q('140:3.6'),'\u27e6Q 140:3.6\u27e7'+auto('p140.009',0)+'\u27e6/Q\u27e7')
sub('part04.py',q('145:4.2'),'\u27e6Q 145:4.2\u27e7'+auto('p145.015',0)+'\u27e6/Q\u27e7')
sub('part04.py',q('147:5.7'),'\u27e6Q 147:5.7\u27e7'+auto('p147.017',0)+'\u27e6/Q\u27e7')
