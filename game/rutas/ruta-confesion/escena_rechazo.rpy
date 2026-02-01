label escena_rechazo:
    # --- ESCENA 9: La confesión rechazada ---

    show personaje brazo_dedo feliz_raro despeinado

    pj "No es una broma. En serio te amo."
    "[nombre_jugador] traga saliva."
    pj "Te conozco desde siempre… y eres con quien quiero pasar mi vida."

    show personaje normal neutra_larga despeinado

    "Isa lo mira."
    "No hay sorpresa. No hay enojo. No hay risa."
    "Solo vacío."

    pj "(No significa nada para ella.)"

    show personaje normal preocupada despeinado

    "Isa suspira, aburrida. Lo observa con una expresión extraña."
    "No es desprecio. Es lástima. Como la que se le dedica a un insecto a punto de ser aplastado."

    "Su mirada se endurece."

    isa "¿Sabes qué?"
    "Su voz es fría."
    isa "Me estoy aburriendo de esto."
    isa "En serio. Para con eso. Eres molesto."

    "Se acerca un paso."

    show personaje normal enojada_raro_izquierda despeinado

    isa "¿No lo ves?"
    "Sientes un nudo en el estómago."
    isa "Incluso todo este tema de las máscaras me parece absurdo."
    
    "Señala la cama."

    isa "¿Por qué hacerlo? Si todo el mundo vive con máscaras todo el tiempo…"
    isa "No es necesaria una de juguete como las del carnaval para portar una máscara."
    
    "Silencio."
    
    isa "¿O sí?"

    "La habitación se siente más fría."
    pj "(La temperatura…)"
    
    "Un escalofrío."
    pj "(Tengo que salir de aquí.)"
    
    "[nombre_jugador] intenta moverse. No puede."
    pj "(Mi cuerpo no responde.)"
    pj "(Corre.)"

    # --- SEXTA ELECCIÓN ---
    menu:
        "Correr":
            jump ruta_correr_escape

        "Quedarse":
            jump escena_alterna

label ruta_correr_escape:

    hide personaje
    
    "[nombre_jugador] logra liberarse y corre fuera de la habitación."
    scene bg_pasillo with vpunch
    "Tu respiración es errática."

    # --- SÉPTIMA ELECCIÓN ---
    menu:
        "Ir a la sala":
            # Según el diagrama, ir a la sala lleva a la Escena X alterna (te atrapa igual)
            jump escena_alterna
        
        "Ir al baño":
            jump ruta_bano_inicio