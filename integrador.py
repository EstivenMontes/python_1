# ============================================================
# EJERCICIO INTEGRADOR
# Registro y evaluación de notas con manejo de errores
# Combina: variables, condicionales, ciclos y try/except
# ============================================================

# ── Función auxiliar: solicitar un número en un rango ───────
def pedir_numero(mensaje, minimo, maximo):
    """Repite la solicitud hasta recibir un float en [minimo, maximo]."""
    while True:
        try:
            valor = float(input(mensaje))
            if valor < minimo or valor > maximo:
                raise ValueError(f"El valor debe estar entre {minimo} y {maximo}.")
            return valor
        except ValueError as e:
            print("  Entrada inválida: " + str(e) + " Intente de nuevo.")

# ── Solicitar cantidad de estudiantes ───────────────────────
while True:
    try:
        cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))
        if cantidad_estudiantes <= 0:
            raise ValueError("Debe ser un número entero positivo.")
        break
    except ValueError as e:
        print("  Error: " + str(e) + " Intente de nuevo.")

# ── Variables acumuladoras ───────────────────────────────────
suma_promedios_grupo = 0
total_aprobados      = 0
total_reprobados     = 0

# ── Registro de cada estudiante ──────────────────────────────
for estudiante in range(1, cantidad_estudiantes + 1):
    print("\n--- Estudiante", estudiante, "---")

    nombre = input("Nombre del estudiante: ").strip()
    if not nombre:
        nombre = f"Estudiante {estudiante}"   # nombre por defecto si queda vacío

    # Cada nota se valida entre 0.0 y 5.0
    nota1 = pedir_numero("  Primera nota  (0.0 – 5.0): ", 0.0, 5.0)
    nota2 = pedir_numero("  Segunda nota  (0.0 – 5.0): ", 0.0, 5.0)
    nota3 = pedir_numero("  Tercera nota  (0.0 – 5.0): ", 0.0, 5.0)

    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 3.0:
        estado           = "✔ Aprobado"
        total_aprobados  = total_aprobados + 1
    else:
        estado           = "✘ Reprobado"
        total_reprobados = total_reprobados + 1

    print("  " + nombre, "→ Promedio:", round(promedio, 2), "—", estado)
    suma_promedios_grupo = suma_promedios_grupo + promedio

# ── Resumen final ────────────────────────────────────────────
try:
    promedio_grupo = suma_promedios_grupo / cantidad_estudiantes
except ZeroDivisionError:
    promedio_grupo = 0.0

print()
print("=" * 35)
print("        RESUMEN DEL GRUPO")
print("=" * 35)
print("Total de estudiantes :", cantidad_estudiantes)
print("Aprobados            :", total_aprobados)
print("Reprobados           :", total_reprobados)
print("Promedio general     :", round(promedio_grupo, 2))
print("=" * 35)
