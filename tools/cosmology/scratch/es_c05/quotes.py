import json, os
H = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Q = {
"w08.016": "Dios el Supremo, Dios el Último y Dios el Absoluto son personalidades de Deidad que están actualizándose y que corresponden a las épocas post-Havona en el tiempo y en el espacio y a las esferas en la trascendencia del espacio y el tiempo de la expansión evolucionaria del universo maestro.",
"w08.022": "Havona, en sí misma y por sí misma, es una creación perfecta pero limitada por su perfección",
"w08.040": "este derecho a gobernar no lo han ganado experiencialmente y por lo tanto estan destinados en un futuro a ser reemplazados por el Ser Supremo, un soberano experiencial",
"w08.049": "Sabemos que el Havona de la era universal anterior era un tanto diferente del Havona de la edad presente.",
"w08.069": "estos hijos trinidizados por criaturas, aunque se encuentran en la presente edad universal, son realmente de la próxima edad universal —la edad que seguirá cuando se complete el crecimiento del Supremo.",
"w08.091": "En los albores de la eternidad, tanto el Padre como el Hijo se hacen infinitamente conocedores de su mutua interdependencia, su eterna y absoluta singularidad",
"w08.161": "Pero Havona misma no es trascendental —es Havona.",
"w09.057": "Una cosa es segura: nuestro estado está fijado por el abrazo de la Trinidad, y la experiencia ya no eventúa en crecimiento.",
"w09.070": "Lo que es trascendental no es necesariamente algo que no se desarrolla, pero es superevolucional en el sentido finito;",
"w09.100": "Dios, como superpersona, eventúa; Dios, como persona, crea; Dios, como prepersona, fragmenta;",
"w09.119": "Pero, tales Hijos, en unión con las Hijas del Espíritu Infinito, pueden crear solamente una Brillante Estrella Matutina en cada universo,",
"w09.131": "porque el abrazo de la Trinidad parece precipitar de la corriente del tiempo futuro muchos de los potenciales no alcanzados de las criaturas.",
"w09.141": "Las criaturas glorificadas que se ocupan de tales aventuras de trinidización sólo pueden participar en una de tales experiencias, mientras que las Deidades del Paraíso no parecen tener límites a la actuación continuada de episodios de trinidización.",
"w09.152": "Las relaciones existen entre dos objetos, pero tres o más objetos resultan en un sistema,",
"w09.162": "son omnipersonales —están antes de la personalidad, son la personalidad y están después de la personalidad.",
"w09.200": "recibirá el privilegio del «contacto personal» con el Brillo Central del Paraíso, será abrazado por las Personas Luminosas, y desaparecerá del reconocimiento de sus camaradas espirituales, para no volver jamás a reaparecer entre aquellos de su clase.",
"w09.206": "y en la producción de los Servitales de Havona, prevalece la ley del dominio del espíritu; la relación establecida indica tres seres espirituales para uno semifísico.",
}
todo = json.load(open(os.path.join(H, "work", "todo_es_c05.json"), encoding="utf-8"))
assert set(todo) == set(Q), set(todo) ^ set(Q)
Q = {k: Q[k] for k in todo}
json.dump(Q, open(os.path.join(H, "es", "quotes_c05.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quotes", len(Q))
