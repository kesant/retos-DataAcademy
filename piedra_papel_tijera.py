def ganador (jugador1,jugador2):#funcion que elije el ganador en una ronda
    victoria=(jugador1,jugador2)
    gano=[("piedra","tijera"),("tijera","papel"),("papel","piedra")]
    perdio=[("tijera","piedra"),("papel","tijera"),("piedra","papel")]
    empate=[("tijera","tijera"),("papel","papel"),("piedra","piedra")]
    if victoria in gano:
        return "jugador1"
    elif victoria in perdio:
        return "jugador2"  
    else:
        return "empate"

def proceso():#elije el ganador del juego
    opciones=["piedra","papel","tijera"]
    puntuacion=[]
    while len(puntuacion)<3:
        i=0
        while i==0:
            jugador1=input("selecione su opcion jugador 1:")
            jugador2=input("selecione su opcion jugador 2 :")
            if (jugador1 in opciones) and (jugador2 in opciones):
                 i=1
            else:
                print("Deben ingresar una opcion valida !!!!!")    
        if ganador(jugador1,jugador2)=="jugador1":
            print("El jugador 1 gano esta ronda")
            puntuacion.append(1)  
        elif ganador(jugador1,jugador2)=="jugador2":
            print("EL jugador 2 gano esta ronda") 
            puntuacion.append(2)   
        else:
            print("Es un empate") 

    if puntuacion.count(1)>=2:
        print("El jugador 1 gano el juego")  
    else :
        print("El jugador 2 gano el juego")    
    
def ingreso():
    print(" Piedra,papel o tijera")
    proceso()


if __name__=="__main__":
    ingreso()
