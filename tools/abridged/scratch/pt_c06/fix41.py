import io
p='p41.py'; s=io.open(p,encoding='utf-8').read()
R=[("cerca de uma tonelada por polegada cúbica","cerca de sessenta quilos por centímetro cúbico"),
("de apenas quinze pés de espessura","de apenas cinco metros de espessura"),
("uma camada de cálcio de seis mil milhas de espessura","uma camada de cálcio de quase dez mil quilômetros de espessura"),
("Está saindo do seu sexto bilionésimo ano","Tem atualmente cerca de seis bilhões de anos")]
for a,b in R:
    assert a in s,a; s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
