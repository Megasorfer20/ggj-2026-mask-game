# 1. Definimos la variable por defecto por si acaso
default nombre_jugador = "T/N"

# 2. Definimos el Personaje para que use esa variable como nombre.
# [nombre_jugador] le dice a Ren'Py que inserte el valor de la variable ahí.
define pj = Character("[nombre_jugador]")

