import sys,io
p=sys.argv[1]; s=io.open(p,encoding='utf-8').read()
R=[("ébranlent ton cœur","ébranlent votre cœur"),("avant de t’efforcer","avant de vous efforcer"),("demande-toi d’abord si tu demeures","demandez-vous d’abord si vous demeurez"),("Puis décide de","Puis décidez de"),
("demande-toi si tu fais","demandez-vous si vous faites"),("et confie ton cœur","et confiez votre cœur"),
("S’il y a aujourd’hui dans ta vie","S’il y a aujourd’hui dans votre vie"),("dépose-le honnêtement","déposez-le honnêtement"),("n’apaise pas ton cœur","n’apaise pas votre cœur"),("Chaque fois que tu pries, demande que ta volonté","Chaque fois que vous priez, demandez que votre volonté"),
("Prends une chose qu’il t’est difficile d’accepter et prie du fond","Prenez une chose qu’il vous est difficile d’accepter et priez du fond"),
("Si tu subis aujourd’hui","Si vous subissez aujourd’hui"),("ne le prends pas","ne le prenez pas"),("Choisis plutôt","Choisissez plutôt"),
("Rappelle-toi une injustice que tu as subie récemment, et écris l’amour et la sincérité que tu peux","Rappelez-vous une injustice que vous avez subie récemment, et écrivez l’amour et la sincérité que vous pouvez")]
for a,b in R:
    if a not in s: print('MISSING',a)
    s=s.replace(a,b)
io.open(p,'w',encoding='utf-8').write(s)
