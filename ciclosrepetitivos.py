# ciclo for = permite que se repita varias veces
#ciclo while = se repite hasta que se cumpla la condicion

#Ejemplo mostrar mensaje "Hola mundo" 10 veces

"""""""""
mensaje = input("Que mensaje quieres Mostrar: ")
cantidad = int(input("Cuantas veces quieres mostrar el mensaje: "))

for i in range(cantidad):
    print(f"{i+1} - {mensaje}") 

    """""""""

""""""""""
#ciclo que se repita 3 veces
import random


numero_secreto = random.randint(1,10)
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el numero secreto (Entre el 1 y el 10): "  ))

    if numero == numero_secreto:
        print("FELICIDADES!!,Adivinaste el numero secreto")
        break
    else:
        intentos_restantes= intentos - (i+1)
        print(f"LO SIENTO, NO adivinaste el numero secreto, te quedan {intentos_restantes} intentos")

        if intentos_restantes == 0:
            print("Se acabaron tus intentos, el numero secreto era: ", numero_secreto)


            
"""""""""



import random


numero_secreto = random.randint(1,10)
intentos = 3

for i in range(intentos):
    numero = int(input("Adivina el numero secreto (Entre el 1 y el 10): "  ))

    if numero == numero_secreto:
        print("FELICIDADES!!,Adivinaste el numero secreto")
        break
    else:
        intentos_restantes= intentos - (i+1)
        print(f"LO SIENTO, NO adivinaste el numero secreto, te quedan {intentos_restantes} intentos")

        if numero > numero_secreto:
            print("El numero es muy alto")

        if numero < numero_secreto:
                print("El numero es muy bajo")

        if intentos_restantes == 0:
            print("Se acabaron tus intentos, el numero secreto era: ", numero_secreto)
            








"""""""""""


    # Ejercicio 1: Mostrar la tabla de multiplicar de un número forma 1 

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(20):          # recorre los valores del 1 al numero que pongas entre ()
    print(f"{numero} x {i+1} = {numero * i+1}")



# Ejercicio 1: Mostrar la tabla de multiplicar de un número forma 2

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

for i in range(1, 11):          # recorre los valores del 1 al 10
    print(f"{numero} x {i} = {numero * i}")


    # Ejercicio 2: Sumar los primeros n números naturales

n = int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, n + 1):
    suma = suma + i

print(f"La suma de los primeros {n} números naturales es: {suma}")

"""""""""""""""""""""












