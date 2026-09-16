from datetime import datetime

try:
    fecha = input("Ingrese una fecha (DD/MM/AAAA): ")

    fecha_valida = datetime.strptime(fecha, "%d/%m/%Y")

    print("Fecha válida:", fecha_valida.strftime("%d/%m/%Y"))

except ValueError:
    print("Error: La fecha debe tener el formato DD/MM/AAAA y ser válida.")
    