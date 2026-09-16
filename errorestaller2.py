try:
    nombre_archivo = input("Ingrese el nombre del archivo: ")

    archivo = open(nombre_archivo, "r")
    contenido = archivo.read()

    print("\nContenido del archivo:")
    print(contenido)

    archivo.close()

except FileNotFoundError:
    print("Error: El archivo no fue encontrado.")