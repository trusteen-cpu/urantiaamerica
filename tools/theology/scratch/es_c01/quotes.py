# -*- coding: utf-8 -*-
import json, os
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
Q = {
 "ch01.s1.u3.q1#0": "Las criaturas que conocen a Dios tienen una sola ambición suprema, un solo ardiente deseo, y ése es llegar —como son en sus esferas— a ser semejantes a como es él en su perfección paradisiaca de personalidad y en su esfera universal de supremacía recta. Del Padre Universal que habita la eternidad ha emanado el mandato supremo: «Sed vosotros perfectos, así como yo soy perfecto».",
 "ch02.s2.u2.q1#0": "El circuito de gravedad espiritual es el canal básico para transmitir las oraciones sinceras del corazón humano creyente desde el nivel de la conciencia humana hasta la verdadera conciencia de la Deidad. Aquello que representa verdadero valor espiritual en vuestras peticiones será aprehendido por el circuito universal de la gravedad espiritual y pasará inmediata y simultáneamente a todas las personalidades divinas competentes",
 "ch02.s2.u3.q1#0": "El Hijo Eterno es infinito, pero es accesible a través de las personas de sus Hijos Paradisiacos y mediante el paciente ministerio del Espíritu Infinito. Sin el servicio de autootorgamiento de los Hijos Paradisiacos y el amante ministerio de las criaturas del Espíritu Infinito, los seres de origen material difícilmente podrían esperar alcanzar al Hijo Eterno.",
 "ch02.s3.u3.q1#0": "«El amor del Espíritu» es real, como también lo son sus pesares; por tanto «no aflijáis al Espíritu de Dios». Sea que contemplemos al Espíritu Infinito como Deidad del Paraíso o como Espíritu Creador del universo local, hallamos que el Creador Conjunto no es sólo la Tercera Fuente y Centro sino también una persona divina. … El Espíritu os habla: «El que tenga oídos, que escuche lo que dice el Espíritu». «El Espíritu mismo intercede por vosotros».",
 "ch02.s4.u2.q2#0": "La mente trasmuta los valores del espíritu en significados del intelecto; la volición tiene el poder de fructificar los significados de la mente a los dominios material y espiritual.",
 "ch04.s3.u3.q1#0": "Así pues la decisión aguarda a cada uno de vosotros así como antaño aguardó a cada uno de nosotros: ¿Fallarás al Dios del tiempo, que tanto depende de las decisiones de la mente finita? ¿Fallarás a la personalidad suprema de los universos por la indolencia de la retrogresión animalística? ¿Fallarás al gran hermano de todas las criaturas, que tanto depende de cada una de ellas?",
}
json.dump(Q, open(os.path.join(H, "es", "quotes_c01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(Q))
