label duda_carnaval:

    # --- ESCENA 6: La duda ---

    "La música continúa, pero [nombre_jugador] apenas la escucha."

    pj "(Algo no está bien.)"

    "[nombre_jugador] mira a Isa, bailando, riendo, siendo… correcta."

    pj "(¿Debería decir algo? ¿Confrontarla? ¿Confesarme como lo planeé desde el inicio?)"

    "Un peso se instala en el pecho."

    pj "(O… ¿simplemente no hacer nada?)"

    # --- ELECCIÓN PRINCIPAL ---

    menu:
        "¿Qué debería hacer [nombre_jugador]?"

        "No hacer nada. Seguir como amigos.":
            jump ruta_no_hacer_nada

        "Confesar lo que siente.":
            jump ruta_confesion_inicio

        "Confrontarla ahora mismo.":
            jump ruta_confrontacion_inicio