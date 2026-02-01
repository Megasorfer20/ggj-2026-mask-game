label escena_encuentro_isa:

    # --- ESCENA 4: El encuentro ---

    "La multitud se mueve al ritmo de la música. Entre colores, risas y máscaras, [nombre_jugador] la ve."

    pj "(Ahí está.)"

|   show personajes

    "Por un instante, el mundo parece detenerse."

    pj "(Isa… Se ve radiante.)"

    "Una sensación fría recorre la espalda de [nombre_jugador]."

    pj "(Pero…)"

    "[nombre_jugador] la observa con más atención."

    pj "(Es ella. Igual que siempre. Hermosa. Deslumbrante.)"

    # Pausa dramática
    window hide
    pause 1.0
    window show

    pj "(Y aun así… algo no cuadra.)"

    pj "(No es su sonrisa. No es su ropa. No es su maquillaje.)"

    "Un leve escalofrío."

    pj "(Todo está bien… y al mismo tiempo, algo está mal.)"

    "[nombre_jugador] traga saliva."

    pj "(Solo son nervios. Tiene que ser eso.)"

    "[nombre_jugador] se acerca."

    # --- ELECCIÓN ---

    menu:
        "¿Qué decirle a Isa?"

        "Hola, Isa. Estoy emocionado… ¿y tú?":
            jump saludo_emocionado

        "Hola… um, Isa, ¿te hiciste algún cambio en el cabello?":
            jump saludo_cabello



# --- ESCENA 4A ---
label saludo_emocionado:

    pj "Hola, Isa. Estoy emocionado… ¿y tú?"

    "Isa se queda en silencio un segundo de más."

    isa "Ah… Sí, claro."

    "Su sonrisa parece distante por un instante."

    pj "(¿Siempre tardaba tanto en responder?)"

    "Isa parpadea… y de pronto su expresión cambia."

    isa "¡Obvio que sí! Es el carnaval, [nombre_jugador]."

    "Isa ríe, cálida, brillante. Como el sol."

    isa "Vamos, ¿no? No podemos llegar tarde."

    "Isa se coloca la máscara y mira a [nombre_jugador]."

    isa "Póntela."

    # Unimos con la escena 5
    jump escena_baile_carnaval



# --- ESCENA 4B ---
label saludo_cabello:

    pj "Hola… um, Isa, ¿te hiciste algún cambio en el cabello?"

    "Isa se queda completamente inmóvil."

    "Su mirada se clava en [nombre_jugador]."

    pj "(Esa mirada…)"

    "Un escalofrío recorre a [nombre_jugador]."

    pj "(Nunca la había visto así.)"

    # Pausa tensa
    "Pasa un segundo."
    "Luego otro."

    "Isa parpadea."

    isa "¿Eh?"

    "La sonrisa vuelve, suave, familiar."

    isa "No, ¿por qué?"

    "Isa ríe, como siempre."

    isa "Vamos, [nombre_jugador]. El carnaval ya empezó."

    "Isa toma su máscara y se la pone."

    isa "Póntela tú también."

    # Unimos con la escena 5
    jump escena_baile_carnaval