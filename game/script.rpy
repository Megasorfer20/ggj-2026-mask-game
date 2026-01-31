
# El juego comienza aquí.

label start:
 # 3. Pedimos el nombre
    "Antes de comenzar..."
    
    # renpy.input abre el teclado. length es el largo máximo.
    $ nombre_jugador = renpy.input("¿Cuál es tu nombre?", length=15)

    # 4. Limpiamos espacios (strip) y ponemos un valor por defecto si lo dejan vacío
    $ nombre_jugador = nombre_jugador.strip()

    if nombre_jugador == "":
        $ nombre_jugador = "T/N"

    # 5. Usamos el nombre
    pj "¡Hola! Me llamo [nombre_jugador] y esta es mi historia."
    
    "Narrador" "Bienvenido, [nombre_jugador]."
    
    jump main

    return
