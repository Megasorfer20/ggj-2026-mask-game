label escena_verdad_bajo_piel:
    # --- ESCENA COMPARTIDA: La verdad bajo la piel ---
    
    isa "…"
    "Su voz es plana. Vacía."
    isa "Tienes razón. Somos mejores amigos… ¿no?"
    isa "No debería ocultarte nada."

    "Un silencio antinatural."
    "Isa levanta ambas manos y las introduce en los orificios de su propio rostro."
    
    pj "(No… no…)"

    "Se escucha un sonido húmedo. Isa tira."
    "Su rostro se abre en dos. La piel se separa como una máscara viva."
    "Debajo no hay carne humana. Hay algo oscuro. Retorcido."

    "La piel completa de Isa se desprende."
    "Frente a [nombre_jugador] queda una criatura negra y brillante."

    entidad "Lo ves ahora."

    # --- DOCEAVA ELECCIÓN (Rama Confrontación directa) ---
    menu:
        "¿Dónde está Isa?":
            jump final_mascara_definitiva

        "Quedarse paralizado":
            jump final_paralizado
            
label final_paralizado:
    "El miedo te congela."
    entidad "Pobre criatura..."
    "La entidad avanza y todo se vuelve negro."
    
    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«La máscara definitiva (Paralizado)»{/size}"
    return