label ruta_confesion_inicio:

    # --- ESCENA 7: Después del carnaval ---
    scene bg_calle_noche with fade # Placeholder o imagen calle noche
    "El carnaval termina. Caminan juntos en silencio."

    pj "(No. Esto son tonterías mías.)"
    pj "(Excusas para acobardarme. Para volver a esconder mis sentimientos.)"

    "[nombre_jugador] aprieta la máscara."

    pj "(Esta vez no.)"

    # --- ESCENA 8: La habitación ---
    scene HABITACION with fade

    "La habitación de [nombre_jugador]. Las máscaras descansan sobre la cama."
    "Isa está sentada, hablando de cosas triviales."

    pj "(Siento algo extraño en el pecho. En el cuerpo.)"
    pj "(Pero deben ser los nervios.)"

    # Pausa
    window hide
    pause 1.0
    window show

    "[nombre_jugador] respira hondo."

    pj "Isa… yo—"
    "Silencio."
    pj "Me gustas."
    pj "No. Te amo."

    "[nombre_jugador] la mira, esperando algo. Cualquier cosa."
    "Silencio."
    "El rostro de Isa está vacío."

    pj "(Nada.)"
    pj "(Ni sorpresa. Ni risa. Ni enojo. Ni duda.)"
    pj "(Es como un cuenco vacío.)"

    "Isa nota la mirada de [nombre_jugador]."
    "De pronto, reacciona."

    isa "¡Ah—!"
    "Isa ríe torpemente. Sus mejillas se sonrojan."
    isa "Qué tonto eres. No me juegues bromas así."
    "Desvía la mirada."

    # --- ELECCIÓN CUARTA (Confesión) ---
    menu:
        "¿Qué responder?"

        "No es una broma. En serio te amo.":
            # Esto lleva a la Escena 9 (Rechazo -> Terror)
            jump escena_rechazo

        "¿Qué te pasa? No eres la misma. ¿Qué ocultas?":
            # Esto lleva a la revelación directa (compartida con la ruta confrontación)
            jump escena_verdad_bajo_piel