with open('prueba.txt', 'w') as archivo:
    archivo.write("Esto es una prueba")
# 1.	Crear programa Python que lea archivos
#a.	Debe ser capaz de leer archivos .txt
#b.	Debe contar la cantidad de letras y espacios que contiene el archivo .txt
#c.	El resumen de cantidad de letras y espacio que contiene el archivo debe entregarlos en otro archivo .txt que genere el programa
#2.	Explicar funcionamiento del código
#a.	Se deberá explicar al profesor cómo funciona el código
#3.	Subir su código a GitHub
def menu():
    while True:
        print ("1-. Leer un archivo \n2-. Salir")
        opcion = int(input("Ingresa una opcion (1-2): "))
        if opcion == 1:
            lectura_archivo()
        elif opcion == 2:
            break
        else: 
            print ("Opcion no valida \nIntenta nuevamente")
def lectura_archivo():
    nombre_archivo = (input("Ingresa el nombre del archivo que quieres leer: "))
    with open (nombre_archivo, 'r') as archivo:
        texto = archivo.read()
        c_letras = (len(texto))
        c_espacios = texto.count(" ") 
        total_letras = c_letras - c_espacios
        with open ('archivo.txt', 'w') as archivo:
            archivo.write(f"La cantidad de letras del archivo que ingresaste es {total_letras} y la cantidad de espacios que contiene es {c_espacios}")
        print(f"La cantidad de letras del archivo que ingresaste es {total_letras} y la cantidad de espacios que contiene es {c_espacios}")  
menu()


