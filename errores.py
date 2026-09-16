
"""

try:
    numero=int(input("Ingrese un numero: "))
    print(f"EL numero ingresado es: {numero}")

except ValueError:
    print("Error: Por favor, ingrese un numero valido.")

    """



menu = 0

while  menu != 3:

    try:

        menu = int(input("""
    seleccione una opcion: 

    1. Sumar
    2. Restar
    3. Salir 

    :

    """))

        if menu == 1:
        
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 + num2
                print(f"El resultado de la suma es: {resultado}")

        elif menu == 2:
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 - num2
                print(f"El resultado de la resta es: {resultado}")

        else:

            print("Opcion invalida.")

    except ValueError:
        print("Error: Por favor, ingrese un numero valido.")

        print("Saliendo del sistema...")






         

     





        


    

