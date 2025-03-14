def calculadora():

    try:
        x = int(input("Introduzca un número: "))
        y = int(input("Introduzca otro: "))
        print(x/y)
        # print(10/2)

    except ZeroDivisionError:
        print("No se puede dividir entre cero.")

    except Exception as e: # excepcion generica, le puedo poner un alias
        print(f"Ha ocurrido un error {e}")

    finally: # Se ejecuta siempre haya o no errores, puedo no ponerlo
        calculadora()


calculadora()