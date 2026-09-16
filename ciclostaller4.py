from datetime import datetime

while True:
    print("\n--- MENÚ INTERACTIVO ---")
    print("1) Mensaje de bienvenida")
    print("2) Fecha y hora actual")
    print("3) Salir del programa")
    
    opcion = input("Selecciona una opción (1-3): ")

    if opcion == "1":
        print("¡Hola! Te damos la bienvenida al programa.")
    elif opcion == "2":
        ahora = datetime.now()
        print(f"Fecha y hora actual: {ahora.strftime('%Y-%m-%d %H:%M:%S')}")
    elif opcion == "3":
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")