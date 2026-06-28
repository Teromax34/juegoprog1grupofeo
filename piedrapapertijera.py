import random

nombrePlayer = "shitass"
#ESTO ES TEMPORAL ACORDATE DE PONER EL SISTEMA DE SCORING GLOBAL GORDO GIL
nombreCPU = "CPU"
vidasPlayer = 5
vidasCPU = 5
elecPlayer = 0
elecCPU = 0

def vidaMetro(nVida):
    # nvida es la cantidad de vida y cuantos corazones tiene que dibujar
    # lo que hace es que basado en nVida lo muestra bonito [ej 2 ♥♥⦸]
    string = ""
    for i in range (0,5):
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
    #compara las elecciones y le quita vida al que perdio
    global vidasPlayer
    global vidasCPU
    match eleccionCPU:

        case 1:
            match eleccionPlayer:
                case 1:
                    return "EMPATE"
                case 2:
                    vidasCPU -= 1
                    return ("GANA "+nombrePlayer)
                case 3:
                    vidasPlayer -= 1
                    return ("GANA "+nombreCPU)
        case 2:
            match eleccionPlayer:
                case 1:
                    vidasPlayer -= 1
                    return ("GANA "+nombreCPU)
                case 2:
                    return "EMPATE"
                case 3:
                    vidasCPU -= 1
                    return ("GANA "+nombrePlayer)
        case 3:
            match eleccionPlayer:
                case 1:
                    vidasCPU -= 1
                    return ("GANA "+nombrePlayer)
                case 2:
                    vidasPlayer -=1
                    return ("GANA "+nombreCPU)
                case 3:
                    return "EMPATE"


def drawUI(eleccionCPU,eleccionPlayer):
    #muestra la interfaz

    resultado = comparasion(elecCPU,elecPlayer)
    drawEleccion(eleccionCPU)
    print(f"{vidaMetro(vidasCPU)}   {nombreCPU}" )
    print("")
    print(resultado)
    print("")
    print(f"{vidaMetro(vidasPlayer)}   {nombrePlayer}" )
    drawEleccion(eleccionPlayer)

while vidasCPU > 0 and vidasPlayer > 0:
    elecCPU = random.randrange(1,4)
    elecPlayer = 0
    while elecPlayer not in range(1,4):
        print("ingrese: 1.piedra 2.papel 3.tijera")
        try:
            elecPlayer = int(input())
            if elecPlayer not in range(1,4):
                print("numero invalido")
        except ValueError:
            print("caracter invalido")

    print("\033[H\033[J", end="")
    drawUI(elecCPU,elecPlayer)

print("\033[H\033[J", end="")
if vidasCPU == 0:
    print("""
    ╔════════╗
    ║⢶⣜⢿⣦⣤⣤⡀⠄║
    ║⠄⢙⣛⣛⣛⣛⣃⣀║
    ║⠄⢈⣤⣹⣡⣌⣏⣿║
    ║⠄⠸⣄⣉⣁⣼⠇⠄║
    ╚════════╝""")
    print(nombrePlayer,"gana")
if vidasPlayer == 0:
    print("""
    ╔════════╗
    ║⣠⣾⣿⣿⣿⡿⠋⡇║
    ║⡇⠄⡆⢰⠄⡇⠄⡇║
    ║⡇⠐⠤⠤⠂⡇⡠⠃║
    ║⡭⡭⣭⠭⠭⣥⢀⠜║
    ╚════════╝""")
    print(nombreCPU,"gana")