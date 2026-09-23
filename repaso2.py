
while True:

    print("==TIQUETE BUS==\n")

    try:


        menu =int(input("""
        Seleccione ruta a comprar:
        
        1.Medellin-Bogota
        2.Medellin-Cali
        3.Medellin-Barranquilla
        4.Medellin-Cartagena
        5.Salir

        """))


        if menu ==1:

            print("Ha seleccionado la ruta Medellin-Bogota.")
            print("=="*35)
            pasajeros = int(input("Ingrese el número de pasajeros: "))
            nombre = input("Ingrese el nombre del pasajero: ")
            precio = 120000
            total = pasajeros * precio
            print(f"El total a pagar es: ${total}")

        elif menu == 2:

                print("Ha seleccionado la ruta Medellin-Cali.")
                print("=="*35)
                pasajeros = int(input("Ingrese el número de pasajeros: "))
                precio = 100000
                total = pasajeros * precio
                print(f"El total a pagar es: ${total}")

        elif menu == 3:

                print("Ha seleccionado la ruta Medellin-Barranquilla.")
                pasajeros = int(input("Ingrese el número de pasajeros: "))
                precio = 150000
                total = pasajeros * precio
                print(f"El total a pagar es: ${total}")

        elif menu == 4:

                print("Ha seleccionado la ruta Medellin-Cartagena.")
                pasajeros = int(input("Ingrese el número de pasajeros: "))
                precio = 200000
                total = pasajeros * precio
                print(f"El total a pagar es: ${total}")

        elif menu == 5:
                print("Sliendo del sistema")
                break
        else:
                print("Opción inválida.")



    except ValueError:
        print("Error: Debe ingresar una opcion valida.")
        continue





