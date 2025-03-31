'''Tenemos una empresa de gestión de residuos, que cobra por metro cúbico de basura.
Los precios cobrados son los siguientes:
Madera: 10€ m3
Plástico: 20€ m3
Hospitalarios: 40€ m3
Otros: 30€ m3
Además, el transporte cobrará a razón de 1€ por kilómetro recorrido al ir a buscar los desechos, 
y 1€ por m3 y kilómetro recorrido a la vuelta.
Realice una aplicación, que pregunte la cantidad de desechos de cada tipo a recoger, además de los Kilómetros y genere un presupuesto.
'''

madera = 10
plastico = 20
hospitalarios = 40
otros = 30

def empresa():
    while True:
        try:
            print("\n-- Empresa Recicla S.L. --\nIntroduzca el tipo de residuo: ")
            tipo = int(input("1. Madera\n2. Plástico\n3. Hospitalarios\n4. Otros\n5. Salir\n--> "))
            if tipo == 5:
                break

            cantidad = int(input("Introduzca cantidad de desechos a recoger en m3: "))
            km = int(input("Introduzca los kilometros: "))

            if tipo == 1 :
                presupuesto = (km) + (cantidad * madera) + (km * madera)
                print(f"El presupuesto es de: {presupuesto}€.")
    
            elif tipo == 2:
                presupuesto = (km) + (cantidad * plastico) + (km * plastico)
                print(f"El presupuesto es de: {presupuesto}€.")

            elif tipo == 3:
                presupuesto = (km) + (cantidad * hospitalarios) + (km * hospitalarios)
                print(f"El presupuesto es de: {presupuesto}€.")

            elif tipo == 4:
                presupuesto = (km) + (cantidad * otros) + (km * otros)
                print(f"El presupuesto es de: {presupuesto}€.")
                       
        except ValueError:
            print("ERROR: Introduzca un número válido.")

empresa()