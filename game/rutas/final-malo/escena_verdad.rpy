label escena_verdad_bajo_piel:

    # --- ESCENA COMPARTIDA: La verdad bajo la piel ---

    "Isa baja la mirada."

    "Su cuerpo queda rígido."

    isa "…"

    "Cuando vuelve a hablar, su voz es plana. Vacía."

    isa "Tienes razón."

    "Levanta lentamente la cabeza."

    "Su expresión es completamente inexpresiva."

    isa "Somos mejores amigos… ¿no?"

    "Clava la mirada en los ojos de [nombre_jugador]."

    "[nombre_jugador] retrocede un paso sin darse cuenta."

    isa "No debería ocultarte nada."

    # Efectos sugeridos para ambientación
    # stop music fadeout 2.0
    # play audio "sonido_tension_baja.ogg"

    "Un silencio antinatural cae alrededor."

    "Isa levanta ambas manos."

    "Las introduce en los orificios de su propio rostro."

    "Sus dedos se hunden en la nariz. En la boca. En las cuencas de los ojos."

    "La piel se estira de forma imposible."

    # play audio "sonido_piel_rasgando.ogg"
    "Se escucha un sonido húmedo, como cuero mojado desgarrándose."

    pj "(No… no…)"

    "Isa tira."

    "Su rostro se abre en dos, desde la frente hasta el mentón."

    "La piel se separa como una máscara viva."

    "Debajo no hay carne humana."

    "Hay algo oscuro. Retorcido."

    "Isa continúa."

    "Sus hombros se abren. Su torso se desgarra."

    "La ropa cae al suelo, vacía."

    "La piel completa de Isa se desprende, colapsando como un disfraz abandonado."

    "Frente a [nombre_jugador] queda una criatura."

    "Alta. Deforme. Con extremidades alargadas. Piel negra y brillante, como mojada."

    "Su rostro no es un rostro. Es una cavidad cambiante."

    "La criatura inclina la cabeza."

    # Asegúrate de tener: define entidad = Character("Entidad")
    entidad "Lo ves ahora."

    # --- ELECCIÓN ---

    menu:
        "¿Dónde está Isa? ¿Qué hiciste con ella?":
            jump final_mascara_definitiva

        "Quedarte paralizado.":
            jump final_paralizado