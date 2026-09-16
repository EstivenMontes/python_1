print ("=== tienda merca + 🏤 === ""\n")

#solicitar variables
producto = input("ingrese el nombre del producto: ")
cantidad = int(input(f"ingrese la cantidad a comprar: "))
precio = float(input("ingrese el precio unitario del producto: "))

#crear variables para calcular.
subtotal = cantidad *precio 
iva = subtotal * 0.19
total = subtotal + iva 


print(" \n == resumen de compra === \n")

print(f"""
producto .....................{producto}
cantidad .....................{cantidad}
precio unitario ..............{precio}
subtotal .....................{subtotal}
iva ..........................{iva}
total pagar ..................{total}

""")
#preguntar si quiere incluir propina
propina = input ("desea incluir propina ")

if propina == "si "or propina == "SI"  or propina == "si" :
    valor_propina = subtotal * 0.1
    print(f"""
subtotal .....................{subtotal}
valor propina ................{valor_propina}
iva(19%)......................{iva}
total pagar ..................{total}

""")
    

elif propina == "no" or propina == "NO" or propina == "no": 
    print(" gracias por su compra tacaña")

else: 
    print("opcion no valida,por favor ingrese si o no")