# Solicitar nombre y edad, se considera mayor apartir de los 18
#si la edad es negativa mostrar error 
#si la persona es menor de edad, calcular cuantos años le faltan para ser mayor
#mostrar nombre, edad ingresada y resultado correspondiente

var_nombre = input("Ingrese su nombre: ")

var_edad = int(input(f"{var_nombre} Por Favor Ingrese Su Edad: "))


if var_edad < 0 :

    print(f"El numero :{var_edad} es negativo")


elif var_edad  >=18 :

    print(f"{var_nombre} Usted es mayor de edad y tienes {var_edad} años")


elif var_edad >0 or var_edad <=17 :

    print(f"{var_nombre} Usted es menor de edad")

    menor = 18 - var_edad

    print(f"{var_nombre} Usted es menor de edad y te faltan {menor} años para ser mayor de edad")







