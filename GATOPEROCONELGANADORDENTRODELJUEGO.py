lista = [["1","2","3"],["4","5","6"],["7","8","9"]]
import os
import random
def validacion_ganador(simbolo, player):
    status = False
    if lista[0][0] == simbolo and lista[0][1] == simbolo and lista[0][2] == simbolo:
                status = True
    elif lista[1][0] == simbolo and lista[1][1] == simbolo and lista[1][2] == simbolo:
                status = True
    elif lista[2][0] == simbolo and lista[2][1] == simbolo and lista[2][2] == simbolo:
                status = True
    elif lista[0][0] == simbolo and lista[1][0] == simbolo and lista[2][0] == simbolo:
                status = True
    elif lista[0][1] == simbolo and lista[1][1] == simbolo and lista[2][1] == simbolo:
                status = True
    elif lista[0][2] == simbolo and lista[1][2] == simbolo and lista[2][2] == simbolo:
                status = True
    elif lista[0][0] == simbolo and lista[1][1] == simbolo and lista[2][2] == simbolo:
                status = True
    elif lista[0][2] == simbolo and lista[1][1] == simbolo and lista[2][0] == simbolo:
                status = True
    if status == True:
        ver_lista()
        print ("Ganaste", player)
        for i in range(3):
            for j in range(3):
                lista[i][j] = str(i * 3 + j + 1)
        return True
        
        
        
    return status 
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')
def ver_lista(): 
    limpiar_consola()
    for i in range(3):
        print(lista[i])

def player_vs_player():
    while True:
        ver_lista()
        print ("--TURNO PLAYER 1--")
        coordenada = int(input("Elige tu posicion: "))
        posicion(coordenada)
        x,y = posicion(coordenada)
        lista [x][y] = ("X")
        if validacion_ganador("X","Player 1"):
            break
        else: ver_lista()
        print ("--TURNO PLAYER 2--")
        coordenada = int(input("Elige tu posicion: "))
        posicion(coordenada)
        x,y = posicion(coordenada)
        lista [x][y] = ("O")
        if validacion_ganador("O","Player 2"):
            break
        else : ver_lista()

def posicion(coordenada):
    if coordenada == 1:
        x = 0
        y = 0
        return (x,y)
    if coordenada == 2:
        x = 0
        y = 1
        return (x,y)
    if coordenada == 3:
        x = 0
        y = 2
        return (x,y)
    if coordenada == 4:
        x = 1
        y = 0
        return (x,y)
    if coordenada == 5:
        x = 1
        y = 1
        return (x,y)
    if coordenada == 6:
        x = 1
        y = 2
        return (x,y)
    if coordenada == 7:
        x = 2
        y = 0
        return (x,y)
    if coordenada == 8:
        x = 2
        y = 1
        return (x,y)
    if coordenada == 9:
        x = 2
        y = 2
        return (x,y)

def player_vs_COM():
        while True:
            ver_lista()
            coordenada = int(input("Elige tu posicion: "))
            x, y = posicion(coordenada) 
            if lista[x][y] != "X" and lista [x][y] != "O":  
                lista[x][y] = "X"  
                if validacion_ganador("X","Player 1"):
                    break
                posiciones_disponibles = [coordenada for coordenada in range(1, 10) if lista[posicion(coordenada)[0]][posicion(coordenada)[1]] not in ["X","O"]]
                coordenada = random.choice(posiciones_disponibles)
                x, y = posicion(coordenada)  
                if lista[x][y] != "O" and lista [x][y] != "X": 
                    lista[x][y] = "O"
                    if validacion_ganador("O","COM"):
                        break  
            else:
                 print ("Elige otra casilla")
        
def menu():
    while True:
        print ("Bienvenido al juego GATO")
        print ("Menu: ")
        print ("1-. Nueva partida (Player 1 vs COM)")
        print ("2-. Versus (P1 VS P2)")
        print ("3-. Salir")
        respuesta = int(input("Elige una opcion (1-3): "))
        if respuesta == 1: 
            player_vs_COM()
        elif respuesta == 2:
            player_vs_player()
        else:
            respuesta == 3
            break

menu()


## Intentar sacar las combinaciones ganadoras y ponerlas en una funcion
## 
## 

## sacar las combinaciones ganadoras y ponerlas en una funcion
## En player vs player no sobreponer las jugadas
##  