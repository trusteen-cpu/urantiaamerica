# -*- coding: utf-8 -*-
import io
p = "t01.py"
s = io.open(p, encoding="utf-8").read()
s = s.replace(u"« La Déité et la réalité »", u"« Déité et réalité »")
a = s.index(u"Le même paragraphe ajoute que cette phase")
b = s.index(u"(105:2.5)", a)
s = s[:a] + u"Le même paragraphe ajoute que, « même les mortels, bien que dans la chair, peuvent expérimenter, sur des niveaux spirituels, cette phase du JE SUIS, s’ils adorent notre Père » " + s[b:]
io.open(p, "w", encoding="utf-8").write(s)
