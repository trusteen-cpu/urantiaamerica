s = open('part3.py', encoding='utf-8').read()
a = '\u00ab\u27e6Q 108:3.6\u27e7\u00a1Casi'
b = '\u00ab\u00a1\u27e6Q 108:3.6\u27e7Casi'
assert a in s; s = s.replace(a, b)
a = 'en la tierra. \u00ab\u27e6Q 110:3.4\u27e7La vida'
b = 'en la tierra. Como dice el libro, \u00ab\u27e6Q 110:3.4\u27e7la vida'
assert a in s; s = s.replace(a, b)
open('part3.py', 'w', encoding='utf-8').write(s)
