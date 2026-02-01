label ruta_confrontacion_inicio:

    # --- ESCENA 7B: En el camino ---

    "Caminan juntos. De pronto, [nombre_jugador] se detiene."

    pj "Isa."

    "Ella se detiene."

    pj "Has estado actuando rara. Hoy pasó algo."

    pj "Nos conocemos desde siempre. Creo que tenemos la suficiente confianza…"

    "[nombre_jugador] la mira con seriedad."

    pj "Puedes decírmelo. ¿Qué ocurre?"

    "Isa sonríe."

    isa "No es nada."

    isa "Te lo estás imaginando."

    isa "Seguro fue el ambiente del carnaval. Las máscaras, la gente… te alteraste un poco."

    # Pausa inquietante
    window hide
    pause 1.0
    window show

    isa "Pero no pasa nada raro. Soy yo."

    "Sonríe, rígida."

    isa "Una persona totalmente normal."

    "Un escalofrío recorre a [nombre_jugador]."

    pj "(Eso… no es algo que Isa diría.)"

    # --- ELECCIÓN RUTA CONFRONTACIÓN ---

    menu:
        "¿Qué decir ahora?"

        # CAMBIO AQUÍ: Ahora salta a la escena de horror
        "¿Qué te pasa? No eres la misma de siempre. ¿Qué me estás ocultando?":
            jump escena_verdad_bajo_piel

        "Pensé que confiabas en mí.":
            jump opcion_confianza_camino