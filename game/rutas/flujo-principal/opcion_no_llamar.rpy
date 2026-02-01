label opcion_no_llamar:

    "[nombre_jugador] deja el teléfono sobre el escritorio."

    pj "(No hace falta llamarla. Todo está planeado.)"

    "[nombre_jugador] se acerca a la mesita de noche y toma un cuadro."
    
    show Cuadro

    "En la foto, Isa y [nombre_jugador] están en el Malecón del Río Magdalena. El sol cae de fondo, el río brilla y ambos sonríen sin posar."

    pj "(Ese día…)"

    "[nombre_jugador] acaricia el borde del cuadro."

    pj "(Caminábamos sin rumbo, hablando de cualquier cosa. El viento le movía el cabello… y de repente lo supe.)"

    # Pausa para efecto dramático
    window hide
    pause 1.0
    window show

    pj "(Ahí fue cuando me di cuenta de que me gustaba. De verdad.)"

    "[nombre_jugador] observa la sonrisa de Isa en la foto."

    pj "(Hoy puede ser diferente.)"

    "[nombre_jugador] deja el cuadro en su lugar y mira la máscara sobre la cama."

    hide Cuadro

    pj "(Tal vez después de esta noche. Después del carnaval. Después de bailar, reír… y quitarnos las máscaras…)"

    "[nombre_jugador] sonríe con nervios."

    pj "(Tal vez hoy sea el día.)"

    # Aquí unimos la historia con la otra ruta
    jump encuentro_carnaval