import sys, os, re
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
import amq
for a in sys.argv[1:]:
    if a.startswith('t'):
        p = a[1:]
        if '.' in p:
            pp, s = p.split('.')
            print(a, amq.title('es', int(pp), int(s)))
        else:
            print(a, amq.title('es', int(p)))
    else:
        try:
            print(a, amq.text('es', a))
        except KeyError:
            print(a, 'MISSING')
    print()
