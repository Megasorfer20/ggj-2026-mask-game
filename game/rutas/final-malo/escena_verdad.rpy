label escena_verdad_bajo_piel:
    # --- ESCENA COMPARTIDA: La verdad bajo la piel ---
    
    show entidad_6
    isa "…"
    "Su voz es plana. Vacía."
    isa "Tienes razón. Somos mejores amigos… ¿no?" 
    isa "No debería ocultarte nada."

    "Un silencio antinatural."
    "Isa levanta ambas manos y las introduce en los orificios de su propio rostro."
    
    pj "(No… no…)"

    "Se escucha un sonido húmedo. Isa tira."

    hide entidad_6
    show entidad_20

    "Su rostro se abre en dos. La piel se separa como una máscara viva."
    "Debajo no hay carne humana. Hay algo oscuro. Retorcido."

    hide entidad_20
    show entidad_26

    "La piel completa de Isa se desprende."
    "Frente a [nombre_jugador] queda una criatura negra y brillante."

    entidad "Lo ves ahora."
    hide entidad_26
    show entidad_32
    # --- DOCEAVA ELECCIÓN (Rama Confrontación directa) ---

    hide entidad_32
    show entidad_43
    menu:
        "¿Dónde está Isa?":
            jump final_mascara_definitiva

        "Quedarse paralizado":
            jump final_paralizado
    
    hide entidad_43
    show entidad_46
    
label final_paralizado:
    "El miedo te congela."
    entidad "Pobre criatura..."
    "La entidad avanza y todo se vuelve negro."
    scene black with fade
    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«La máscara definitiva (Paralizado)»{/size}"
    return