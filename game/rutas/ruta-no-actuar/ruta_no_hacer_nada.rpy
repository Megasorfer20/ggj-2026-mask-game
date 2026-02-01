label ruta_no_hacer_nada:

    # --- ESCENA FINAL: El silencio ---

    scene bg_calle_noche

    "El carnaval termina. La noche pasa."

    show personaje normal

    pj "(Decidí no decir nada.)"

    # Transición de tiempo
    scene black with fade
    centered "Días después..."
    
    # Aquí puedes restaurar el fondo si quieres, o dejarlo en negro/gris
    
    scene HABITACION

    pj "(A partir de ese día… Isa empezó a alejarse.)"

    show Cel

    "Conversaciones cortas. Mensajes sin emoción."

    hide Cel

    pj "(Ya no se sentía cercana.)"

    pj "(Era como hablar con un robot. Con alguien que sabía exactamente qué decir… pero no cómo sentir.)"

    window hide
    pause 1.0
    window show

    pj "(No parecía humana en su forma actual. No parecía ella.)"

    pj "(Actuaba intentando ser demasiado perfecta. Siendo Isa… pero no de manera natural.)"

    scene black with fade
    centered "Años después..."

    scene bg_cocina

    pj "(Nunca le dije lo que sentía.)"

    "Un día, el silencio es absoluto."

    pj "(Hasta que un día… simplemente desapareció.)"

    # FIN DEL JUEGO PARA ESTA RUTA
    "FINAL: El Silencio."
    return