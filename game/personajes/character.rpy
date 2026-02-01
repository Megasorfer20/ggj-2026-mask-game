default nombre_jugador = "T/N"
define pj = Character("[nombre_jugador]",color="#de6617")
define narrador = Character(None)
define isa = Character("Isa", color="#e2bd15") # Puedes cambiar el color
define entidad = Character("Entidad", color="#800000") 

##### DEFINICION PERSONAJES #####

layeredimage personaje:
    group cuerpo:
        # Atributo | "Ruta de la imagen"
        attribute normal default "gui/images/personajes/Movimiento1.png"
        attribute brazo "gui/images/personajes/Movimiento2.png"
        attribute dedo "gui/images/personajes/Movimiento4.png"
        attribute brazo_dedo "gui/images/personajes/Movimiento3.png"

    group cabeza:
        attribute neutral default "gui/personajes/cara1.png"
        attribute neutra_larga "gui/personajes/cara2.png"
        attribute feliz "gui/personajes/cara3.png"
        attribute feliz_entre "gui/personajes/cara4.png"
        attribute feliz_entre_abajo_izq "gui/personajes/cara5.png"
        attribute preocupada_derecha "gui/personajes/cara6.png"
        attribute serira_raro "gui/personajes/cara7.png"
        attribute feliz_raro_peq "gui/personajes/cara8.png"
        attribute enojada_raro "gui/personajes/cara9.png"
        attribute enojada_raro_izquierda "gui/personajes/cara11.png"
        attribute alegre_miedo_izquierda "gui/personajes/cara12.png"
        attribute seria_duda_derecha "gui/personajes/cara13.png"
        attribute feliz_derecha "gui/personajes/cara14.png"
        attribute preocupada_abajo "gui/personajes/cara15.png"
        attribute preocupada "gui/personajes/cara16.png"
        attribute preocupada_raro "gui/personajes/cara17.png"
        attribute preocupada "gui/personajes/cara18.png"
        attribute feliz_raro "gui/personajes/cara19.png"

    group pelo:
        attribute normal default "gui/personajes/pelo-normal.png"
        attribute despeinado "gui/personajes/pelo-raro.png"
        attribute mascara "gui/personajes/marimonda-masc.png"


