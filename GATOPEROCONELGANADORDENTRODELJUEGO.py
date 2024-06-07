lista = [["1","2","3"],["4","5","6"],["7","8","9"]]
def player_vs_player():
    while True:
        if lista[0][0] == "X" and lista[0][1] == "X" and lista[0][2] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        elif lista[1][0] == "X" and lista[1][1] == "X" and lista[1][2] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        elif lista[2][0] == "X" and lista[2][1] == "X" and lista[2][2] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        elif lista[0][0] == "X" and lista[1][0] == "X" and lista[2][0] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        elif lista[0][1] == "X" and lista[1][1] == "X" and lista[2][1] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        elif lista[0][2] == "X" and lista[1][2] == "X" and lista[2][2] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        elif lista[0][0] == "X" and lista[1][1] == "X" and lista[2][2] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        elif lista[0][2] == "X" and lista[1][1] == "X" and lista[2][0] == "X":
                print("¡¡Felicidades, ganaste!!")
                for i in range (3):
                    print (lista[i])
                break
        else: 
            for i in range (3):
                print (lista[i])

        coordenada = int(input("Elige tu posicion: "))
        posicion(coordenada)
        x,y = posicion(coordenada)
        lista [x][y] = ("X")

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

#def player_vs_player():
     #if ganador():
        
        
        
def player_vs_COM():
    while True:
        for i in range (3):
            print (lista[i])

        figura = input("")

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


##elif lista [0][2] and lista [1][1] and lista [2][0] == "X" or "O":
    #print ("¡¡Felicidades, ganaste!!")
    #break


##if lista [0][0] and lista [0][1] and lista [0][2] == "X":
            

## DEFINIR GANADORif lista [["1","2","3"],["4","5","6"],["7","8","9"]] == [["1","X","3"],["4","X","6"],["7","X","9"] 
## HACER UN WHILE GANADOR = FALSE PARA SEGUIR EL JUEGO SINO RETURN TRUE
##  if lista (0, 0), (0, 1), (0, 2) == "X"
##  elif:
    