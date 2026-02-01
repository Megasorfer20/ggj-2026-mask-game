label opcion_confianza_camino:

    # ESCENA 7C – "Pensé que confiabas en mí"
    
    "Caminamos juntos en silencio."
    "Me detengo."
    show personaje at center 
    pj "Pensé que confiabas en mí."
    
    "Isa se queda quieta."
    "Su cuerpo tiembla apenas un segundo."
    "Un pequeño espasmo recorre su cuello."
    "Sus dedos se tensan."
    
    pj "¿Acaba de…?"
    
    "Isa baja la cabeza."
    "Parece concentrada."
    "Como si repitiera algo una y otra vez dentro de su mente."
    "Respira."
    "Se detiene."
    "Vuelve a respirar."
    
    "Por primera vez en todo el día…"
    "Hay un leve atisbo de vida en sus ojos."
    "No es la Isa de siempre."
    "Pero es… algo."
    
    isa "¿Tú…{w=0.5} confías en mí?"
    
    pj "Por supuesto."
    
    "Me acerco."
    
    pj "¿Cómo no hacerlo?"
    
    "Tomo sus manos."
    
    pj "Eres la persona más importante de mi vida."
    
    "La miro fijamente a los ojos."
    
    pj "Y no hay nada que pueda pasar{w=0.5} que cambie eso."
    
    "Las mejillas de Isa se sonrojan."
    "Aparta la mirada por unos segundos."
    "En sus ojos cruza algo extraño."
    "Culpa."
    "Isa duda antes de hablar."
    
    isa "¿Y si yo…{w=0.5} ya no fuera la misma de siempre…?"
    "Traga saliva."
    isa "¿Aún sería lo más importante para ti?"
    
    "Levanto una mano."
    "La poso suavemente sobre su mejilla."
    "La otra sigue entrelazada con su mano."
    
    pj "Está…{w=0.5} helada."
    
    "Un frío antinatural."
    "Pero ya no importa."
    "Me acerco."
    
    pj "No hay nada…"
    
    "Beso a Isa."
    
    pj "…que pueda hacer{w=0.5} que deje de amarte."
    
    "Apoyo mi frente contra la de ella."
    
    pj "Mi querida Isa."
    
    "Isa se queda inmóvil un segundo."
    "Luego, lentamente…"
    "Devuelve el abrazo."
    
    # ESCENA FINAL – Una vida juntos
    
    scene black with fade
    
    "El tiempo pasa."
    "Isa y yo estamos juntos."
    "Reímos. Vivimos. Compartimos una vida."
    
    pj "A veces…{w=0.5} no es la misma."
    pj "Hay momentos en los que Isa es Isa…"
    
    $ renpy.pause(0.5)
    
    pj "y otros en los que es como si fuera alguien más."
    
    "Una mirada vacía. Un gesto que no encaja."
    
    pj "Pero no importa."
    
    "Tomo su mano."
    
    pj "Porque yo amo a Isa."
    pj "Y no hay manera{w=0.5} de que deje de amarla."
    
    "Isa sonríe."
    "Su sonrisa es perfecta."
    "Demasiado perfecta."
    
    # FINAL OBTENIDO
    
    scene black with fade
    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«Dulce máscara»{/size}\n{size=+3}{i}Vivir en una mentira{/i}{/size}" with dissolve
    
    # Esto hace que el juego termine o vuelva al menú principal
    return