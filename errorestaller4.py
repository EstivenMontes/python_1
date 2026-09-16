import math

def raiz_cuadrada(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo.")
    return math.sqrt(n)

# Ejemplo de uso con manejo de excepciones
try:
    numero = float(input("Ingresa un número: "))
    resultado = raiz_cuadrada(numero)
    print(f"La raíz cuadrada de {numero} es {resultado}")
except ValueError as error:
    print(f"Error: {error}")
    