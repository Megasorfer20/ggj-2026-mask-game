default nombre_jugador = "T/N"
define pj = Character("[nombre_jugador]")
define narrador = Character(None)
define isa = Character("Isa", color="#ffcccc") # Puedes cambiar el color
define entidad = Character("Entidad", color="#800000") 

##### DEFINICION PERSONAJES #####
image LisaF = "gui/images/personajes/Lisa_Feliz.png"
image Lisa = "gui/images/personajes/Lisa.png"
image M1 = "gui/images/personajes/Movimiento1.png"
image M2 = "gui/images/personajes/Movimiento2.png"
image M3 = "gui/images/personajes/Movimiento3.png"
image M4 = "gui/images/personajes/Movimiento4.png"

layeredimage personaje:
    group cuerpo:
        # Atributo | "Ruta de la imagen"
        attribute normal default "gui/images/personajes/Movimiento1.png"
        attribute brazo "gui/images/personajes/Movimiento2.png"
        attribute dedo "gui/images/personajes/Movimiento4.png"
        attribute brazo_dedo "gui/images/personajes/Movimiento3.png"

    group cabeza:
        attribute feliz "gui/personaje/expresiones/cara_feliz.png"
        attribute triste "gui/personaje/expresiones/cara_triste.png"
        attribute triste "gui/personaje/expresiones/cara_triste.png"
        attribute triste "gui/personaje/expresiones/cara_triste.png"
        attribute triste "gui/personaje/expresiones/cara_triste.png"
        attribute triste "gui/personaje/expresiones/cara_triste.png"
        attribute triste "gui/personaje/expresiones/cara_triste.png"
        attribute triste "gui/personaje/expresiones/cara_triste.png"

    group pelo:
        attribute normal default "gui/personajes/pelo-normal.png"
        attribute despeinado "gui/personajes/pelo-raro.png"
        attribute mascara "gui/personajes/marimonda-masc.png"


