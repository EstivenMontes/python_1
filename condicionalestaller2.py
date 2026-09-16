var_nombre = input("Ingrese su nombre: ")

calificacion = float(input(f"{var_nombre} Por Favor Ingrese la nota: "))


if calificacion >=4.5 and calificacion <=5.0:
 
 print(f"APROBADO con {calificacion}")

 print("="*30)

 print(f"{var_nombre}  Ademas su nota es EXCELENTE, {calificacion}")

elif calificacion >=3.5 and calificacion <=4.4:

 print(f"APROBADO CON {calificacion}")

 print("="*30)

 print(f"{var_nombre}  Ademas su nota es BUENO, {calificacion}")

elif calificacion >=3.0 and calificacion <=3.4:
 
 print(f"APROBADO CON {calificacion}")

 print("="*30)

 print(f"{var_nombre}  Ademas su nota es ACEPTABLE, {calificacion}")


elif  calificacion >=0.0 and calificacion <2.9:
 
 print(f"REPROBADO CON {calificacion}")

 print("="*30)

 print(f"{var_nombre}  Ademas su nota es INSUFICIENTE, {calificacion}")

else:
  print("Error, La nota ingresada es incorrecta")


