def tabla_multiplicar():
    # Pedimos al usuario un número entero
    numero = int(input("Introduce un número entero para generar su tabla de multiplicar: "))

    # Imprimimos la tabla de multiplicar del número
    print(f"\nTabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

tabla_multiplicar()