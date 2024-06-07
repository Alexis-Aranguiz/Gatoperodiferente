def ganador(lista):
    if (lista[0][0] == lista[0][1] == lista[0][2] == "X" or
        lista[1][0] == lista[1][1] == lista[1][2] == "X" or
        lista[2][0] == lista[2][1] == lista[2][2] == "X" or
        lista[0][0] == lista[1][0] == lista[2][0] == "X" or
        lista[0][1] == lista[1][1] == lista[2][1] == "X" or
        lista[0][2] == lista[1][2] == lista[2][2] == "X" or
        lista[0][0] == lista[1][1] == lista[2][2] == "X" or
        lista[0][2] == lista[1][1] == lista[2][0] == "X"):
        print("¡¡Felicidades, ganaste!!")
        return True
    else:
        return False

def player_vs_player():
    lista = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    while True:
        for i in range(3):
            print(lista[i])

        coordenada = int(input("Elige tu posición (1-9): "))
        x, y = (coordenada - 1) // 3, (coordenada - 1) % 3

        if lista[x][y] == " ":
            lista[x][y] = "X"
            if ganador(lista):
                return
        else:
            print("Esa posición ya está ocupada. Elige otra.")

player_vs_player()
