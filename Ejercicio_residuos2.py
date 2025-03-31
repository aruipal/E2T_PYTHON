# Tarifas por tipo de residuo (€ por m³)
tarifas = {
    1: ("Madera", 10),
    2: ("Plástico", 20),
    3: ("Hospitalarios", 40),
    4: ("Otros", 30)
}

def calcular_presupuesto(tipo, cantidad, km):
    """Calcula el presupuesto basado en tipo de residuo, cantidad y distancia."""
    nombre, precio_m3 = tarifas[tipo]
    costo_ida = km * 1  # 1€ por kilómetro recorrido al ir
    costo_residuos = cantidad * precio_m3  # Precio de los residuos
    costo_vuelta = km * cantidad * 1  # 1€ por m³ y km a la vuelta
    total = costo_ida + costo_residuos + costo_vuelta
    return nombre, total

def empresa():
    """Ejecuta la aplicación de presupuestos."""
    while True:
        print("\n-- Empresa Recicla S.L. --\nSeleccione el tipo de residuo:")
        for key, value in tarifas.items():
            print(f"{key}. {value[0]}")
        print("5. Salir")

        try:
            tipo = int(input("--> "))
            if tipo == 5:
                print("Saliendo del programa...")
                break
            if tipo not in tarifas:
                print("Opción no válida, intente de nuevo.")
                continue
            
            cantidad = int(input("Introduzca la cantidad de desechos a recoger (m³): "))
            km = int(input("Introduzca los kilómetros de distancia: "))

            nombre_residuo, presupuesto = calcular_presupuesto(tipo, cantidad, km)
            print(f"\nPresupuesto para {cantidad} m³ de {nombre_residuo}: {presupuesto}€.")
        
        except ValueError:
            print("Error: Introduzca un número válido.")

# Ejecutar la aplicación
empresa()