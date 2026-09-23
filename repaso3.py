while True:
    print("\n== TIQUETE BUS ==")

    try:
        menu = int(
            input("""
        Seleccione ruta a comprar:
        
        1. Medellin - Bogota ($120.000)
        2. Medellin - Cali ($100.000)
        3. Medellin - Barranquilla ($150.000)
        4. Medellin - Cartagena ($200.000)
        5. Salir

        Opción: """
            )
        )

        # Asignación de precios según la opción elegida
        if menu == 1:
            precio = 120000
            ruta = "Medellin - Bogota"
        elif menu == 2:
            precio = 100000
            ruta = "Medellin - Cali"
        elif menu == 3:
            precio = 150000
            ruta = "Medellin - Barranquilla"
        elif menu == 4:
            precio = 200000
            ruta = "Medellin - Cartagena"
        elif menu == 5:
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida. Por favor seleccione un número del 1 al 5.")
            continue

        # Registro de pasajeros para la compra actual
        try:
            pasajeros = int(input("Ingrese el número de pasajeros: "))

            if pasajeros <= 0:
                print("El número de pasajeros debe ser mayor a 0.")
                continue

            # Reiniciamos la lista para almacenar únicamente los pasajeros de esta nueva compra
            lista_pasajeros = []

            for i in range(pasajeros):
                nombre = input(f"Ingrese el nombre del pasajero {i+1}: ")
                lista_pasajeros.append(nombre)

            # Resumen de la compra
            print(
                f"""
            === RESUMEN COMPRA ===
            Ruta: {ruta}
            Precio por tiquete: ${precio:,}
            Número de pasajeros: {pasajeros}
            Pasajeros registrados: {', '.join(lista_pasajeros)}
            Total a pagar: ${precio * pasajeros:,}
            """
            )

        except ValueError:
            print("Error: Debe ingresar un número válido de pasajeros.")

    except ValueError:
        print("Error: Debe ingresar una opción válida del menú.")