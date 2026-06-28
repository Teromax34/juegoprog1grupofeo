import juan #juego de Juan cinta 
import piedrapapertijera #juego de Agustin Pierotti
import geografia #juego de Clara Mendoza

newScore = 0
opcion = -1
nombrePlayer = input("ingrese su nombre: ")
while opcion != 5:
    opcion = -1
    while opcion not in range(0,6):
        try:
            print("=======Elija un juego=======")
            opcion = int(input("0...............pelisTrivia\n1........piedrapapeltijeras\n2...........geografiaTrivia\n3........tercerjuegosecreto\n4...............verPuntajes\n5.....................salir\n"))
            if opcion not in range(0,6):
                print("\033[H\033[J", end="")
                print("numero invalido")
        except ValueError:
            print("\033[H\033[J", end="")
            print("solo ingrese numeros")
    match opcion:
        case 0:
            print("\033[H\033[J", end="")
            newScore = juan.peliculas()
        case 1:
            print("\033[H\033[J", end="")
            newScore = piedrapapertijera.pidrapapeltijera(nombrePlayer)
        case 2:
            print("\033[H\033[J", end="")
            newScore = geografia.iniciar_juego()
        case 3:
            print("\033[H\033[J", end="")
            pass
        case 4:
            print("\033[H\033[J", end="")
            pass # aqui deberian poder verse los scores
        case 5:
            break
