#=============================================
#INTRODUCION A LAS VARIABLES EN PYTHON
#=============================================

#Una varibale permite almacenar datos para utilizarlo
# posteriormente dentro del programa.

nombre = "Estiven"                 #Variable texto - string
documento = 1214742805                    #Variable numerica - int
direccion = "Cra 46A # 98-24"      #Variable texto - string
tiene_deuda = True                 #Variable Booleano : True o False

# ============================================================
# MOSTRAR EL CONTENIDO DE UNA VARIABLE
# ============================================================

print(nombre)

print("Concatenacion usando + " ) 

print("=" * 30)

print('Mi nombre es : ' + nombre + " Mi documento es: " + str(documento))

print('Mi nombre es : ', nombre , " Mi documento es: " , documento )


# ============================================================
# Tarea: Mostrar nombre, documento, direccion y tiene deuda.
# ============================================================

print(
    " Mi nombre es :",nombre , 
    " Mi documento es : ",documento,
    " Mi direccion es :",direccion, 
    " Tengo deudas: ",tiene_deuda
    )

# ============================================================
# CONCATENACIÓN USANDO F-STRINGS
# ============================================================

print("\nCONCATENACIÓN USANDO F-STRINGS")
print("=" * 30)

# Las f-strings permiten insertar variables directamente
# dentro de un texto.
#
# Se coloca la letra f antes de las comillas y las variables
# se escriben entre llaves { }.

print(f"Mi nombre es: {nombre} y mi documento es: {documento}")

print(f"Mi nombre es: {nombre} y mi documento es: {documento} mi direccion es: {direccion} y tengo deudas {tiene_deuda}" )

# Las f-strings también permiten crear textos
# de varias líneas utilizando triple comilla.

print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deuda}
""")

# También podemos utilizar tres comillas simples (''')
# para crear textos de varias líneas.

print("=" * 30)

print(f"""
Nombre:         {nombre}
Documento:      {documento}
Dirección:      {direccion}
¿Tiene deudas?: {tiene_deuda}
""")

# SALTO DE LÍNEA EN PYTHON

# \n representa un salto de línea.
# Salto de línea al inicio del texto

print(f"\n Hola, {nombre}!")

# Salto de línea al final del texto
print(f"Bienvenido {nombre} a Python.\n")