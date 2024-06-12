import os

contador_espacios = 0

with open('archivo.txt', 'w') as archivo:
    archivo.write("¡Hola, mundo! waaa")

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    c_letras = len(contenido)
    print(contenido, "La cantidad de letras en el archivo es:", c_letras)
    espacios = contenido.count(" ")
    print("La cantidad de espacios en el texto es:", espacios)