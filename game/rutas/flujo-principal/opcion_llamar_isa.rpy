label opcion_llamar_isa:
    
    "[nombre_jugador] toma el teléfono del escritorio."

    "[nombre_jugador] enciende la pantalla. Aparece la foto de Isa: está sacando la lengua, con el cabello alborotado por el viento. [nombre_jugador] recuerda haber tomado esa foto una tarde cualquiera, sin que ella se diera cuenta."

    pj "(Siempre hace esa cara cuando cree que nadie la está mirando.)"

    "[nombre_jugador] duda un segundo… y marca."

    # Aquí podrías poner: play audio "sonido_telefono.ogg"
    "..."

    isa "¿[nombre_jugador]?"

    pj "Isa… hola. Solo quería saber si ya estás lista."

    "Pequeño silencio al otro lado."

    isa "Sí, sí… o sea, casi. Todo bien."

    pj "(Su voz… suena rara.)"

    pj "¿Estás segura? Te noto un poco—"

    isa "Es que… Mira, [nombre_jugador], tengo que colgar."

    pj "¿Ahora?"

    isa "Sí, es que pasó algo y— pero no es nada, de verdad. Nos vemos allá, ¿sí?"

    pj "Isa, espera—"

    # Aquí: play audio "sonido_colgar.ogg"
    "La llamada se corta."

    "[nombre_jugador] se queda mirando la pantalla apagada del teléfono."

    pj "(Eso fue… extraño.)"

    "[nombre_jugador] aprieta el teléfono con fuerza."

    pj "(Tal vez solo son los nervios. El carnaval pone así a cualquiera.)"

    "[nombre_jugador] deja el teléfono y respira hondo."

    pj "Sí… No pasa nada. Todo saldrá bien."

    # Aquí ambas rutas deben unirse de nuevo para ir al Carnaval
    jump encuentro_carnaval