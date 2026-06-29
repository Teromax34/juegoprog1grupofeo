import os
import juan                    # juego de Juan
import piedrapapertijera       # juego de Agustin
import geografia               # juego de Clara
import game_campo              # juego de Santi

ARCHIVO = "puntajes.txt"

nombrePlayer = input("Ingrese su nombre: ")
newScore = 0


def iniciarArchivo():
    if not os.path.exists(ARCHIVO):
        with open(ARCHIVO, "w") as f:
            f.write("[pelisTrivia]\n")
            f.write("\n")
            f.write("[piedrapapeltijeras]\n")
            f.write("\n")
            f.write("[geografiaTrivia]\n")
            f.write("\n")
            f.write("[tercerjuegosecreto]\n")

def leerPuntajes():
    iniciarArchivo()
    puntajes = {
        "pelisTrivia": [],
        "piedrapapeltijeras": [],
        "geografiaTrivia": [],
        "tercerjuegosecreto": []
    }
    juegoActual = ""
    with open(ARCHIVO, "r") as f:
        for linea in f:
            linea = linea.strip()
            if linea == "":
                continue
            if linea.startswith("["):
                juegoActual = linea[1:-1]
            else:
                nombre, puntaje = linea.split(";")
                puntajes[juegoActual].append((nombre, int(puntaje)))
    return puntajes

def guardarPuntajes(puntajes):
    with open(ARCHIVO, "w") as f:
        for juego in puntajes:
            f.write(f"[{juego}]\n")
            for nombre, puntaje in puntajes[juego]:
                f.write(f"{nombre};{puntaje}\n")
            f.write("\n")

def agregarScore(juego, nombre, score):
    puntajes = leerPuntajes()
    puntajes[juego].append((nombre, score))
    puntajes[juego].sort(key=lambda x: x[1], reverse=True)
    puntajes[juego] = puntajes[juego][:10]
    guardarPuntajes(puntajes)

def mostrarPuntajes():
    puntajes = leerPuntajes()
    print("\n========== HIGHSCORES ==========\n")
    for juego in puntajes:
        print("----", juego, "----")
        if len(puntajes[juego]) == 0:
            print("Sin puntajes.")
        else:
            puesto = 1
            for nombre, score in puntajes[juego]:
                print(f"{puesto}. {nombre} - {score}")
                puesto += 1
        print()
iniciarArchivo()
opcion = -1
while opcion != 5:
    opcion = -1
    while opcion not in range(0, 6):
        try:
            print("=======Elija un juego=======")
            opcion = int(input(
"""0...............pelisTrivia
1........piedrapapeltijeras
2...........geografiaTrivia
3........tercerjuegosecreto
4...............verPuntajes
5.....................salir
"""))
            if opcion not in range(0, 6):
                print("\033[H\033[J", end="")
                print("Numero invalido")
        except ValueError:
            print("\033[H\033[J", end="")
            print("Solo ingrese numeros")
    match opcion:
        case 0:
            print("\033[H\033[J", end="")
            newScore = juan.peliculas()
            agregarScore("pelisTrivia", nombrePlayer, newScore)
        case 1:
            print("\033[H\033[J", end="")
            newScore = piedrapapertijera.pidrapapeltijera(nombrePlayer)
            agregarScore("piedrapapeltijeras", nombrePlayer, newScore)
        case 2:
            print("\033[H\033[J", end="")
            newScore = geografia.iniciar_juego()
            agregarScore("geografiaTrivia", nombrePlayer, newScore)
        case 3:
            print("\033[H\033[J", end="")
            newScore = game_campo.campo()
            agregarScore("tercerjuegosecreto", nombrePlayer, newScore)
        case 4:
            print("\033[H\033[J", end="")
            mostrarPuntajes()
            input("\nPresione ENTER para volver al menu...")
        case 5:
            break