label encuentro_carnaval:

    # --- ESCENA 3: Camino al carnaval ---

    "[nombre_jugador] sale de su habitación con la máscara en las manos."

    pj "(Sea como sea… ya es hora.)"

    # Aquí podrías poner un cambio de fondo y música
    # scene bg_calle_tarde
    # play music "musica_carnaval_lejana.ogg" fadein 2.0
    
    scene carnaval

    "[nombre_jugador] se dirige al lugar acordado, a la hora de siempre. Las calles empiezan a llenarse de música, colores y gente."


    pj "(Isa es una persona maravillosa. De esas que no se encuentran dos veces.)"

    pj "(La conozco más de lo que me conozco a mí mismo. Con ella no tengo que fingir. No tengo que actuar.)"

    show marimonda

    "[nombre_jugador] ajusta la máscara entre sus dedos."

    pj "(Con Isa puedo ser yo. Sin disfraces. Sin sonrisas falsas.)"

    # Pausa dramática
    window hide
    pause 1.0
    window show

    pj "(Ella es una de las pocas personas con las que no necesito usar una máscara…)"


    "[nombre_jugador] mira la máscara un instante más."

    pj "(Excepto cuando se trata de mis sentimientos por ella.)"

    "[nombre_jugador] se coloca la máscara."

    hide marimonda

    pj "(Tal vez esta noche… Eso cambie.)"

    show personas

    "[nombre_jugador] continúa caminando, perdiéndose entre la música y el bullicio del carnaval."


    jump escena_encuentro_isa
    return