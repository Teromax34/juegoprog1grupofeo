nombrePlayer = "shitass"
#ESTO ES TEMPORAL ACORDATE DE PONER EL SISTEMA DE SCORING GLOBAL GORDO GIL
nombreCPU = "CPU"
vidasPlayer = 3
vidasCPU = 3
elecPlayer = 1
elecCPU = 3

def vidaMetro(nVida):
    # nvida es la cantidad de vida y cuantos corazones tiene que dibujar
    # lo que hace es que basado en nVida lo muestra bonito [ej 2 ♥♥⦸]
    string = ""
    for i in range (0,3):
        if i < nVida:
            string = string + "♥"
        else:
            string = string + "⦸"

    return string

def drawEleccion(eleccion):
    #dibuja iconos basado en el numero
    match eleccion:
        case 1: #piedra
            print("╔══════════╗\n║ ⠄⣴⣶⣿⣿⡆⠄⠄ ║\n║ ⣠⣿⣿⣿⣿⣿⣷⠄ ║\n║ ⢿⣿⣿⡿⣛⣭⣝⡀ ║\n║ ⠄⠛⠛⠃⢿⣿⣿⡿ ║\n╚══════════╝")
        case 2: #papel
            print("╔══════════╗\n║ ⣹⠸⠿⠿⠿⠿⠿⠿ ║\n║ ⣿⠸⠿⠿⠿⠿⠿⠿ ║\n║ ⣿⠸⠿⠿⠿⠿⠿⠿ ║\n║ ⣹⠸⠿⠿⠿⠿⠿⠿ ║\n╚══════════╝")
        case 3: #tijera
            print("╔══════════╗\n║ ⣾⠉⠙⡆⢰⠋⠉⣷ ║\n║ ⠙⠦⠤⣷⣾⠤⠴⠋ ║\n║ ⠄⢀⣰⡿⢿⣆⡀⠄ ║\n║ ⠄⣼⡿⠃⠘⢿⣧⠄ ║\n╚══════════╝")

def comparasion(eleccionCPU,eleccionPlayer):
    match eleccionCPU:
        case 1:
            match eleccionPlayer:
                case 1:
                    return "EMPATE"
                case 2:
                    return ("GANA "+nombrePlayer)
                    vidasCPU -= 1
                case 3:
                    return ("GANA "+nombreCPU)
                    vidasPlayer -= 1
        case 2:
            match eleccionPlayer:
                case 1:
                    return ("GANA "+nombreCPU)
                    vidasPlayer -= 1
                case 2:
                    return "EMPATE"
                case 3:
                    return ("GANA "+nombrePlayer)
                    vidasCPU -= 1
        case 3:
            match eleccionPlayer:
                case 1:
                    return ("GANA "+nombrePlayer)
                    vidasCPU -= 1
                case 2:
                    return ("GANA "+nombreCPU)
                    vidasPlayer -=1
                case 3:
                    return "EMPATE"


def drawUI(eleccionCPU,eleccionPlayer):
    resultado = comparasion(elecCPU,elecPlayer)
    drawEleccion(eleccionCPU)
    print(f"{vidaMetro(vidasCPU)}   {nombreCPU}" )
    print("")
    print(resultado)
    print("")
    print(f"{vidaMetro(vidasPlayer)}   {nombrePlayer}" )
    drawEleccion(eleccionPlayer)

drawUI(elecCPU,elecPlayer)

