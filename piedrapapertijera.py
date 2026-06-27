def drawPapel():
    print("""╔══════════╗
    ║ ⣹⠸⠿⠿⠿⠿⠿⠿ ║
    ║ ⣿⠸⠿⠿⠿⠿⠿⠿ ║
    ║ ⣿⠸⠿⠿⠿⠿⠿⠿ ║
    ║ ⣹⠸⠿⠿⠿⠿⠿⠿ ║
    ╚══════════╝""")

def drawPiedra():
    print("""╔══════════╗
    ║ ⠄⣴⣶⣿⣿⡆⠄⠄ ║
    ║ ⣠⣿⣿⣿⣿⣿⣷⠄ ║
    ║ ⢿⣿⣿⡿⣛⣭⣝⡀ ║
    ║ ⠄⠛⠛⠃⢿⣿⣿⡿ ║
    ╚══════════╝""")

def drawTijera():
    print("""╔══════════╗
    ║ ⣾⠉⠙⡆⢰⠋⠉⣷ ║
    ║ ⠙⠦⠤⣷⣾⠤⠴⠋ ║
    ║ ⠄⢀⣰⡿⢿⣆⡀⠄ ║
    ║ ⠄⣼⡿⠃⠘⢿⣧⠄ ║
    ╚══════════╝""")

def vidaMetro(nVida, uiDireccion = True):
    # nvida es la cantidad de vida y cuantos corazones tiene que dibujar, 
    # uidireccion es para que acople lindo al resto de la interfaz, True ▲ false ▼
    # lo que hace es que basado en nVida lo muestra bonito [ej 2 ♥♥⦸]
    string = ""
    for i in range (0,3):
        if i < nVida:
            string = string + "♥"
        else:
            string = string + "⦸"

    return string



print(f"{vidaMetro(2)}")

#print("\033[H\033[2J", end="")