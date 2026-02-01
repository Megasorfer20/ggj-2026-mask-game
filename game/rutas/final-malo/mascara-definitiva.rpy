label final_mascara_definitiva:

    # --- ESCENA FINAL: ROSTRO PRESTADO (Final Malo) ---

    pj "¿Dónde está Isa? ¿Qué hiciste con ella?"

    "La criatura ríe."

    "Un sonido seco, quebrado."

    entidad "Isa… ya no existe."

    "Se acerca."

    entidad "Isa soy yo."

    # Pausa
    window hide
    pause 1.0
    window show

    entidad "Pero no por mucho."

    "Los ojos —si es que pueden llamarse así— se clavan en [nombre_jugador]."

    entidad "Ahora… voy a ser tú."

    "La criatura se abalanza."

    # Efecto de golpe o pantalla roja
    # scene black with vpunch
    
    "[nombre_jugador] cae al suelo violentamente."

    "El frío atraviesa el cuerpo, paralizando hasta los huesos."

    pj "(No puedo moverme—)"

    "Un dolor infernal."

    "Garras largas se clavan en el rostro de [nombre_jugador]."

    "Se hunden bajo la piel."

    "La levantan."

    "La piel del rostro se desprende como un pedazo de cuero viejo."

    "Despegándose lentamente."

    "Gritar es imposible."

    "La sangre corre."

    "[nombre_jugador] queda en carne viva."

    "Con los últimos alientos, ve a la criatura tomar su rostro."

    "Se lo coloca."

    "La piel se adapta. Se asimila."

    "Los rasgos de [nombre_jugador] aparecen donde antes no había nada."

    "Recuerdos se filtran. Momentos. Emociones."

    # Aquí la entidad habla con la voz del PJ
    entidad "Vaya…"

    "Se observa las manos."

    entidad "Pensé que este recipiente duraría más."

    "Mira el cuerpo sin rostro en el suelo."

    entidad "No esperaba que alguien lo descubriera tan pronto."

    "Sonríe."

    entidad "Pero bueno… nadie notará tu ausencia."

    window hide
    pause 1.0
    window show

    entidad "Después de todo…"

    "Se inclina."

    entidad "tú eras el único que se preocupaba lo suficiente por ella como para que importara."

    "La criatura se aleja caminando, con el rostro de [nombre_jugador]."

    "El cuerpo queda inmóvil."

    scene black with fade
    
    # Texto centrado grande para el final
    show text "{size=50}FINAL OBTENIDO: La máscara definitiva{/size}" at truecenter
    with dissolve
    pause 3.0
    hide text with dissolve

    return