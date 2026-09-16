suma = 0
cantidad = 0

while True:
    entrada = input("Ingresa un número (o 'fin' para terminar): ")
    
    if entrada.lower() == 'fin':
        break
        
    try:
        numero = float(entrada)
        suma += numero
        cantidad += 1
    except ValueError:
        print("Entrada inválida, se ignorará.")

if cantidad > 0:
    promedio = suma / cantidad
    print(f"\nCantidad de valores aceptados: {cantidad}")
    print(f"Promedio: {promedio}")
else:
    print("\nNo se ingresaron números válidos.")
    