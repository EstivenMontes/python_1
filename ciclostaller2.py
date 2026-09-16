# Solicita un número entero positivo al usuario
numero = int(input("Ingresa un número entero mayor que 0: "))

# Verifica que el número sea válido antes de iniciar
if numero > 0:
    # Recorre desde el número ingresado hasta 0
    while numero >= 0:
        print(numero)
        numero -= 1  # Decrementa el valor en cada iteración
    
    print("¡La cuenta regresiva ha terminado!")
else:
    print("El número ingresado debe ser mayor que 0.")