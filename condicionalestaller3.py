var_nombre = input("\nIngrese el nombre del cliente: ")

total_compra = float(input(f"\n{var_nombre} Ingrese Valor de compra: "))

if total_compra >= 0 and total_compra <= 99999:
    print (f"{var_nombre} El total de su compra es de {total_compra} y no tienes descuento")

elif total_compra >= 100000 and total_compra <= 299999:
    descuento = total_compra * 0.10
    total_descuento = total_compra - descuento
    print (f"{var_nombre} El total de su compra es de {total_compra} y el descuento es de {descuento} y el total a pagar es de {total_descuento}")

elif total_compra >= 300000 and total_compra <= 499999:
    descuento = total_compra * 0.15
    total_descuento = total_compra - descuento
    print (f"{var_nombre} El total de su compra es de {total_compra} y el descuento es de {descuento} y el total a pagar es de {total_descuento}")

elif total_compra >= 500000:
    descuento = total_compra * 0.20
    total_descuento = total_compra - descuento
    print (f"{var_nombre} El total de su compra es de {total_compra} y el descuento es de {descuento} y el total a pagar es de {total_descuento}")

else:
    print ("Error, El total de la compra ingresada es incorrecta")
    
















