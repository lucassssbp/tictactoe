tablero = [[" ", " ", " "],
           [" ", " ", " "],
           [" ", " ", " "]]

def mostrar_tablero():
    print("   0   1   2")
    for i, fila in enumerate(tablero):
        print(f"{i}  " + " | ".join(fila))
        if i < 2:
            print("  ---+---+---")
            
def comprobar_ganador(jugador):
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] == jugador:
            return True
    if (tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador) or \
       (tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador):
        return True
    return False

jugador_actual = "X"
turnos = 0

while True:
    mostrar_tablero()
    print(f"Turno del jugador {jugador_actual}")
    
    try:
        fila = int(input("Ingresa la fila (0,1,2): "))
        col = int(input("Ingresa la columna (0,1,2): "))
        if fila not in range(3) or col not in range(3):
            print("Coordenadas fuera de rango.")
            continue
    except ValueError:
        print("Entrada inválida.")
        continue
    
    if tablero[fila][col] == " ":
        tablero[fila][col] = jugador_actual
    else:
        print("La casilla está ocupada.")
        continue

    turnos += 1
    if comprobar_ganador(jugador_actual):
        mostrar_tablero()
        print(f"El jugador {jugador_actual} ha GANADO!!!!")
        break
    
    if turnos == 9:
        mostrar_tablero()
        print("Empate")
        break
        
    jugador_actual = "O" if jugador_actual == "X" else "X"
