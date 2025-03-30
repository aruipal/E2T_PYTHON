telefonos = {"Jose": 1234,
             "Maria": 4567,
             "Lucia": 9876,
             "Andres": 1912
             }

consultando = True

while consultando:
    print("\nMIS TELEFONOS\n------------\n1. Consultar\n2. Añadir\n3. Modificar\n4. Borrar\n5. Salir")

    opcion = ""
    while opcion not in ("1","2","3","4","5"):
        opcion = input("-->")
        if opcion == "1": # consultar
            nombre = input("Nombre: ")
            if nombre not in telefonos:
                print("No existe.")
            else:
                telf = telefonos[nombre]
                print(f"{nombre}:{telf}")
        if opcion == "2": # añadir
            nombre = input("Nombre: ")
            if nombre in telefonos:
                print("Ese nombre ya está en la agenda.")
            else:
                telf = int(input("Telefono: "))
                telefonos[nombre] = telf
                print("Añadido correctamente.")
        if opcion == "3": # Modificar
            nombre = input("Nombre: ")
            if nombre not in telefonos:
                print("Ese nombre no esta en la agenda.")
            else:
                telf = int(input("Telefono: "))
                telefonos[nombre] = telf
                print("El telefono se ha modificado.")
        if opcion == "4": # Borrar
            nombre = input("Nombre: ")
            if nombre not in telefonos:
                print("Ese nombre no está en la agenda.")
            else:
                del telefonos[nombre]
                print("El telefono se ha borrado.")
        elif opcion == "5": # Salir
            consultando = False
