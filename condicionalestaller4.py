#Ejercicio 4: Condicionales clima

var_ciudad = input("\nIngrese la CIUDAD: ")

var_grados = float(input("\nIngrese grados celsius:"))

if var_grados >32:
    print (f"{var_ciudad} Esta MUY CALIENTE , la temperatura es de {var_grados}° grados celsius")

elif var_grados >=26 and var_grados <=32:
    print (f"{var_ciudad} Esta CALIENTE , la temperatura es de {var_grados}° grados celsius")

elif var_grados >=18 and var_grados <=25:
    print (f"{var_ciudad} Esta TEMPLADO , la temperatura es de {var_grados}° grados celsius")

elif var_grados >=10 and var_grados <=17:
    print (f"{var_ciudad} Esta FRIA, se recominda usar ABRIGO , la temperatura es de {var_grados}° grados celsius")

elif var_grados <10:
    print (f"{var_ciudad} Esta MUY FRIO, se recominda usar ABRIGO , la temperatura es de {var_grados}° grados celsius")        
