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
        attribute neutral default "gui/images/personajes/cara1.png"
        attribute neutra_larga "gui/images/personajes/cara2.png"
        attribute feliz "gui/images/personajes/cara3.png"
        attribute feliz_entre "gui/images/personajes/cara4.png"
        attribute feliz_entre_abajo_izq "gui/images/personajes/cara5.png"
        attribute preocupada_derecha "gui/images/personajes/cara6.png"
        attribute serira_raro "gui/images/personajes/cara7.png"
        attribute feliz_raro_peq "gui/images/personajes/cara8.png"
        attribute enojada_raro "gui/images/personajes/cara9.png"
        attribute enojada_raro_izquierda "gui/images/personajes/cara11.png"
        attribute alegre_miedo_izquierda "gui/images/personajes/cara12.png"
        attribute seria_duda_derecha "gui/images/personajes/cara13.png"
        attribute feliz_derecha "gui/images/personajes/cara14.png"
        attribute preocupada_abajo "gui/images/personajes/cara15.png"
        attribute preocupada "gui/images/personajes/cara16.png"
        attribute preocupada_raro "gui/images/personajes/cara17.png"
        attribute preocupada_feliz "gui/images/personajes/cara18.png"
        attribute feliz_raro "gui/images/personajes/cara19.png"

    group pelo:
        attribute normal_pelo default "gui/images/personajes/pelo-normal.png"
        attribute despeinado "gui/images/personajes/pelo-raro.png"
        attribute mascara "gui/images/personajes/marimonda-masc.png"


