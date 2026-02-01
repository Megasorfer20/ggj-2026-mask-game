label escena_alterna:
    # --- ESCENA X ALTERNA / ESCENA X ---
    # Se llega aquí si te quedas (Sexta elección) o si vas a la sala (Séptima elección)
    # o si cierras con llave el baño (Octava elección - lógica del diagrama).

    scene bg_sala_noche with fade
    
    "[nombre_jugador] se queda paralizado frente a Isa (o ella te alcanza)."
    "El aire se vuelve frío."
    "Isa te observa con una expresión vacía."

    isa "No deberías haber dicho eso."

    "[nombre_jugador] respira hondo. No se mueve. No grita."

    isa "¿Eso es todo?"

    "Un paso adelante. Otro."

    # --- DOCEAVA ELECCIÓN (Alternativa en diagrama) ---
    menu:
        "Enfrentarla":
            jump final_mascara_tn

        "Protegerte":
            jump final_mascara_permanente

        "No hacer nada":
            jump final_mascara_verguenza

label final_mascara_tn:
    "[nombre_jugador] aprieta los puños."
    pj "¿Quién eres? ¿Qué has hecho con mi preciosa amiga?"

    "La entidad ríe, un sonido profundo y antinatural."
    entidad "Insignificante… Siempre preguntan eso cuando ya es demasiado tarde."

    "La entidad se acerca. Con ambas manos y garras toma su propio rostro."
    "Rasga su propia piel como si fuera cuero viejo. Se revela su verdadera forma: oscura y deforme."

    entidad "Está bien… sé que te va a encantar mi versión de [nombre_jugador]."

    "La entidad te alcanza y arranca tu rostro con sus garras."

    scene black with fade
    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«Máscara de [nombre_jugador]»{/size}"
    return

label final_mascara_permanente:
    "[nombre_jugador] mira alrededor. Agarra un cuadro con la foto de él e Isa."
    "Lo tira al rostro de la entidad."

    "La entidad se contornea y desprende su piel. Se ríe."
    entidad "Mal movimiento."

    "La entidad salta sobre [nombre_jugador]. Largas garras desgarran tu rostro."
    entidad "Bueno, por tu culpa, ahora tú eres mi máscara permanente."

    scene black with fade
    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«Máscara permanente»{/size}"
    return

label final_mascara_verguenza:
    entidad "Vaya… normalmente para este momento gritan o lloran."
    
    pj "Tú no eres Isa."

    "[nombre_jugador] agarra el cuadro de Isa. Lo rompe contra la mesa."
    "Con uno de los vidrios se corta el rostro."

    pj "Esto es por ti, Isa… porque no pude quitarme esta máscara de vergüenza y decirte lo que siento antes de perderte."

    "Caes al suelo. La sangre brota."

    scene black with fade
    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«Máscara de vergüenza»{/size}"
    return