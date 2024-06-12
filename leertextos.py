import os 
contador_espacios = 0
with open('archivo.txt', 'w') as archivo:
    archivo.write("¡Hola, mundo! waaa")

with open('archivo.txt', 'r') as archivo:
    contenido = archivo.read()
    c_letras = (len(contenido))
    print(contenido , "La cantidad de letras en el archivo es: ", c_letras)
    espacios = contenido.count(" ")
    print ("La cantidad de espacios en el texto es:", espacios , "y la cantidad de letras en el archivo son:", c_letras)
    
# 1.	Crear programa Python que lea archivos
#a.	Debe ser capaz de leer archivos .txt
#b.	Debe contar la cantidad de letras y espacios que contiene el archivo .txt
#c.	El resumen de cantidad de letras y espacio que contiene el archivo debe entregarlos en otro archivo .txt que genere el programa
#2.	Explicar funcionamiento del código
#a.	Se deberá explicar al profesor cómo funciona el código
#3.	Subir su código a GitHub
