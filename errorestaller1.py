 

try:

        menu = (input("""
    seleccione una opcion: 

    +
    -
    *
    /


    :

    """))

        if menu == "+" :
        
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                resultado = num1 + num2
                print(f"El resultado de la suma es: {resultado}")

        elif menu == "-" :
                
                        num1 = int(input("Ingrese el primer numero: "))
                        num2 = int(input("Ingrese el segundo numero: "))
                        resultado = num1 -num2
                        print(f"El resultado de la resta es: {resultado}")

        elif menu == "*" :
                        
                                num1 = int(input("Ingrese el primer numero: "))
                                num2 = int(input("Ingrese el segundo numero: "))
                                resultado = num1 *num2
                                print(f"El resultado de la multiplicacion es: {resultado}")

        elif menu == "/" :
                                
                                        num1 = int(input("Ingrese el primer numero: "))
                                        num2 = int(input("Ingrese el segundo numero: "))
                                        resultado = num1 /num2
                                        print(f"El resultado de la division es: {resultado}")

except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")                                        

except ValueError:
        print("Error: Por favor, ingrese un numero valido.")
        
        