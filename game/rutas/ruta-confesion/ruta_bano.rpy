label ruta_bano_inicio:
    # --- OCTAVA ELECCIÓN - BAÑO ---
    scene BANO  with fade
    "[nombre_jugador] entra al baño y cierra de golpe. Su corazón late con fuerza."

    menu:
        "Esconderse en la bañera":
            jump ruta_banera_descubrimiento
        
        "Cerrar con llave":
            # Según el diagrama, cerrar con llave lleva a Escena X Alterna (te atrapa)
            jump escena_alterna

label ruta_banera_descubrimiento:
    "[nombre_jugador] se acerca lentamente a la bañera."
    "El líquido es espeso. Rojo oscuro. Un olor metálico invade el aire."

    scene bg_bano_sangre  with fade
    
    pj "(Sangre.)"
    
    "Dentro de la bañera… hay un cuerpo. Totalmente desnudo. Sin piel."
    "La piel del rostro ha sido arrancada."

    pj "(No… no…)"

    # --- NOVENA ELECCIÓN ---
    menu:
        "Inspeccionar cadáver":
            jump ruta_inspeccionar_cadaver
        
        "Salir corriendo (Avisar policía)":
            jump final_policia
            
        "Volver con Isa (Huir juntos)":
            jump final_volver_isa

label final_policia:
    "[nombre_jugador] sale del baño corriendo."
    pj "¡Tengo que irme! ¡Hay un cadáver!"
    
    scene black with fade
    "Corres hacia la estación de policía."
    
    "La policía llega. La casa está intacta. No hay sangre. No hay cadáver."
    "Isa no está."
    
    "Nadie me creyó. Fui internado."
    pj "Lo juro… todo fue real."
    
    scene bg_manicomio with dissolve
    pj "Isa…"

    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«Cuando quitar la máscara no es suficiente»{/size}"
    return

label final_volver_isa:
    scene bg_pasillo
    "[nombre_jugador] corre hacia la habitación."

    show personaje brazo_dedo feliz_raro despeinado

    pj "¡Isa! ¡Hay un cadáver en el baño! ¡Vámonos!"

    isa "Eres muy ruidoso. Muy molesto."
    
    "La puerta de la casa se abre. Pero sientes un dolor agudo."
    "Cinco cuchillas invisibles se clavan en tu mejilla."
    
    "Isa te arranca el rostro."
    
    entidad "Este recipiente… me durará un poco más."

    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«Una máscara a la vez»{/size}"
    return

label ruta_inspeccionar_cadaver:
    # --- DÉCIMA ELECCIÓN ---
    "[nombre_jugador] se arrodilla. Observa el cabello rizado y rojo."
    pj "(Es Isa.)"
    show entidad_1
    "Pasos lentos se acercan."
    hide entidad_1
    menu:
        "Esconderse en bañera":
            jump ruta_esconderse_banera_exito
            
        "Correr a la sala (Huir)":
            jump final_verdad_revelada

label final_verdad_revelada:
    show entidad_43
    "[nombre_jugador] corre. Un golpe. La entidad lo alcanza."
    "Manos lo sujetan. El rostro es arrancado."
    hide entidad_43
    show entidad_42
    entidad "Seguiré jugando con Isa… y tú serás la siguiente máscara."
    hide entidad_42
    show entidad_43
    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«La verdad revelada»{/size}"
    return

label ruta_esconderse_banera_exito:
    "[nombre_jugador] se sumerge en la sangre. Aguanta la respiración."
    "La entidad entra, mira y se va."
    
    "[nombre_jugador] sale temblando."

    # --- UNDÉCIMA ELECCIÓN ---
    menu:
        "Huir por ventana":
            jump final_reflejo
            
        "Buscar cuchillo en cocina":
            jump final_rostro_nadie_quiso

label final_reflejo:
    scene bg_ventana
    "[nombre_jugador] llega a una ventana abierta."
    "Sacas tu celular para llamar."
    
    entidad "No hay a dónde huir."
    
    "Te giras. La entidad eres tú."
    entidad "Yo soy tú."
    
    "Te arranca el rostro y se lo pone."
    entidad "Encaja perfecto."

    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«El reflejo que te mira»{/size}"
    return

label final_rostro_nadie_quiso:
    scene bg_cocina
    "[nombre_jugador] corre a la cocina. Agarra un cuchillo."
    
    "La entidad aparece. Atacas."
    "El cuchillo atraviesa la nada. La entidad lo absorbe."
    
    entidad "Tsk. Ni siquiera vales la pena como máscara."
    
    "Te derriba y te desangras solo en la penumbra."

    centered "{size=+10}{b}FINAL OBTENIDO{/b}{/size}\n\n{size=+5}«Rostro que nadie quiso»{/size}"
    return