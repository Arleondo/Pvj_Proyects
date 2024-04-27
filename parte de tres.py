import random

tablero = [["", "", ""], ["", "", ""], ["", "", ""]]
jugadores = ["X", "O"]
turno_actual = random.choice(jugadores)
posiciones_validas = [(i, j) for i in range(3) for j in range(3)]
ganador = ""

print("  +---+---+---+")
for i in range(3):
    fila = str(i) + "  "
    for j in range(3):
        fila += tablero[i][j] + " | "
    print(fila)
    print("  +---+---+---+")

while ganador == "" and len(posiciones_validas) > 0:
    jugada_valida = 0
    while not jugada_valida:
        posicion = input(f"Turno de {turno_actual}. Ingresa la posición de tu jugada (fila, columna): ")
        try:
            fila, columna = map(int, posicion.split(","))
            if (fila, columna) in posiciones_validas:
                tablero[fila][columna] = turno_actual
                posiciones_validas.remove((fila, columna))
                jugada_valida = 1
            else:
                print("Jugada inválida, la posición ya fue ocupada o no existe.")
        except ValueError:
            print("Jugada inválida, debes ingresar dos números separados por coma.")
        except IndexError:
            print("Jugada inválida, debes ingresar dos números entre 0 y 2.")
    print("  +---+---+---+")
    for i in range(3):
        fila = str(i) + " | "
        for j in range(3):
            fila += tablero[i][j] + "  "
        print(fila)
        print("  +---+---+---+")
    for jugador in jugadores:
        if tablero[0][0] == jugador and tablero[0][1] == jugador and tablero[0][2] == jugador:
            ganador = jugador
        elif tablero[1][0] == jugador and tablero[1][1] == jugador and tablero[1][2] == jugador:
            ganador = jugador
        elif tablero[2][0] == jugador and tablero[2][1] == jugador and tablero[2][2] == jugador:
            ganador = jugador
        elif tablero[0][0] == jugador and tablero[1][0] == jugador and tablero[2][0] == jugador:
            ganador = jugador
        elif tablero[0][1] == jugador and tablero[1][1] == jugador and tablero[2][1] == jugador:
            ganador = jugador
        elif tablero[0][2] == jugador and tablero[1][2] == jugador and tablero[2][2] == jugador:
            ganador = jugador
        elif tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
            ganador = jugador
        elif tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
            ganador = jugador
    if turno_actual == "X":
        turno_actual = "O"
    else:
        turno_actual = "X"
if ganador != "":
    print(f"¡El jugador {ganador} ha ganado!")
