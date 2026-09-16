import random

# Genera un número aleatorio entre 1 y 10
numero_secreto = random.randint(1, 10)


while True:
    intento = int(input("Adivina el número (entre 1 y 10): "))
    
    if intento == numero_secreto:
        print("¡Felicidades! Has adivinado el número correcto.")
        break  # Sale del ciclo cuando acierta
    else:
        print("Incorrecto. Intenta de nuevo.")
