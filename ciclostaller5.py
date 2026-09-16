# Solicita la cantidad de notas a registrar
cantidad_notas = int(input("¿Cuántas notas deseas registrar?: "))

suma_notas = 0.0

# Recorre con un ciclo for la cantidad especificada
for i in range(1, cantidad_notas + 1):
    nota = float(input(f"Ingresa la nota {i}: "))
    suma_notas += nota  # Acumula la nota ingresada

# Calcula el promedio
if cantidad_notas > 0:
    promedio = suma_notas / cantidad_notas
    print(f"\nEl promedio final es: {promedio:.2f}")

    # Evalúa el estado de aprobación
    if promedio >= 3.0:
        print("Estado: Aprobado")
    else:
        print("Estado: No aprobado")
else:
    print("No se registraron notas.")