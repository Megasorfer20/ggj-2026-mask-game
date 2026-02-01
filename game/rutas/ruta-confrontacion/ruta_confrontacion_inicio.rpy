label ruta_confrontacion_inicio:
    # --- ESCENA 7B: En el camino ---
    scene bg_calle_noche
    "Caminan juntos. De pronto, [nombre_jugador] se detiene."

    pj "Isa. Has estado actuando rara. Hoy pasó algo."
    pj "Puedes decírmelo. ¿Qué ocurre?"

    isa "No es nada. Te lo estás imaginando. Soy yo, una persona totalmente normal."

    "Un escalofrío recorre a [nombre_jugador]."
    pj "(Eso… no es algo que Isa diría.)"

    # --- TERCERA ELECCIÓN (CRÍTICA / CONFRONTACIÓN) ---
    menu:
        "¿Qué te pasa? No eres la misma. ¿Qué ocultas?":
            jump escena_verdad_bajo_piel

        "Pensé que confiabas en mí.":
            jump opcion_confianza_camino