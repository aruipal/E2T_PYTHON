'''Diseña una clase ConversorTemperatura con métodos para convertir de Celsius a Fahrenheit y viceversa.
Usa un constructor para inicializar una temperatura base.'''

class ConversorTemperatura:
    
    def __init__(self,temp):
        self.temp = temp
        
    def cf(self):
        far = (self.temp * 9/5) + 32
        return f"{self.temp} grados C son {round(far,2)} grados Fahrenheit."
        
    def fc(self):
        cel = (self.temp - 32) * 5/9
        return f"{self.temp} grados F son {round(cel,2)} grados celcius."
    
def menu():
    try:   
        opcion = float(input("\nSelecciona conversión a realizar:\n - 1. De Celsius a Fahrenheit.\n - 2. De Fahrenheit a Celsius. \nOpcion:"))
        if opcion == 1:
            temp = float(input("Introduce grados Celsius a convertir: "))
            conversor1 = ConversorTemperatura(temp)
            print(conversor1.cf())
        elif opcion == 2:
            temp = float(input("Introduce grados Fahrenheit a convertir: "))
            conversor1 = ConversorTemperatura(temp)
            print(conversor1.fc())
        else:
            print("ERROR, seleccione 1 o 2.")
            return menu()
    except ValueError:
        print("Error, inténtelo de nuevo.")
        return menu()
        
menu()