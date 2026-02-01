label main:

    scene HABITACION
    # --- ESCENA 1: Antes de la máscara ---
    
    # Nota: Aquí usamos [nombre_jugador] para que el narrador diga el nombre real.
    
    "[nombre_jugador] está en su habitación. La luz del sol entra por la ventana. Sobre la cama hay telas de colores, pintura, plumas y dos máscaras de marimonda."

    pj "Hoy es el día."

    pj "No recuerdo la última vez que me sentí así…{w} como si el pecho me vibrara por dentro."

    show marimonda

    "[nombre_jugador] toma una de las máscaras y la observa."

    pj "El Carnaval de Barranquilla. Meses hablando de esto… meses planeándolo… y por fin llegó."

    pj "Isa y yo hicimos estas máscaras con nuestras propias manos. Puntada por puntada. Risa tras risa."

    "[nombre_jugador] sonríe, luego suspira."

    pj "Isabela… aunque para mí siempre ha sido Isa."

    pj "La conozco desde que éramos niños. Ha estado ahí en cada etapa de mi vida… y aun así, nunca he sido capaz de decirle lo que siento."

    "[nombre_jugador] aprieta ligeramente la máscara."

    pj "Tal vez porque tengo miedo de romper algo. O porque detrás de esta amistad… prefiero esconderme como detrás de una máscara."

    hide marimonda
    show Cel

    "[nombre_jugador] mira su celular sobre el escritorio."

    pj "Dijimos que nos encontraríamos a la misma hora de siempre. Todo está perfectamente planeado."

    hide Cel

    # Pausa dramática
    window hide
    pause 1.0
    window show

    pj "Pero aun así…"

    # --- ELECCIÓN ---

    menu:
        "¿Qué debería hacer?"

        "Llamar a Isa para escuchar su voz antes de salir.":
            jump opcion_llamar_isa

        "No llamarla. Confiar en el plan y prepararme para salir.":
            jump opcion_no_llamar