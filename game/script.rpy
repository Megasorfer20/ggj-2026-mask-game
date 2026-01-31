label start:
    # 3. Pedimos el nombre
    "Antes de comenzar..."
    
    # renpy.input abre el teclado.
    $ nombre_jugador = renpy.input("¿Cuál es tu nombre?", length=15)

    # 4. Limpiamos espacios
    $ nombre_jugador = nombre_jugador.strip()

    # Si lo deja vacío, usamos el default
    if nombre_jugador == "":
        $ nombre_jugador = "T/N"

    # 5. Usamos el nombre. 
    # Como 'pj' ya fue definido en definitions.rpy (al inicio), esto ya no fallará.
    pj "¡Hola! Me llamo [nombre_jugador] y esta es mi historia."
    
    "Narrador" "Bienvenido, [nombre_jugador]."
    
    # Saltamos a la historia principal
    jump main