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
    
conversor1 = ConversorTemperatura(80)        
print(conversor1.cf())
print(conversor1.fc())
            
