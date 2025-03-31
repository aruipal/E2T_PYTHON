class Calculadora2:
    
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
        
    def sumar(self):
        return self.num1 + self.num2
    
    def restar(self):
        return self.num1 - self.num2
    
    def multiplicar(self):
        return self.num1 * self.num2
    
    def dividir(self):
        return self.num1 / self.num2


    
def menu():
    print("\tCALCULADORA:\n1.Sumar\n2.Restar\n3.Multiplicar\n4.Dividir")
    opcion = int(input("Selecciona operación: "))
    if opcion > 4:
        print("¡¡¡Operación no permitida.!!!")
        menu()
    numero1 = float(input("Introduce un número: "))
    numero2 = float(input("Introduce otro número: "))

    if opcion == 1:
        calculo1 = Calculadora2(numero1,numero2)
        print(f"El resultado es: {calculo1.sumar()}")
    elif opcion == 2:
        calculo1 = Calculadora2(numero1,numero2)
        print(f"El resultado es: {calculo1.restar()}")
    elif opcion == 3:
        calculo1 = Calculadora2(numero1,numero2)
        print(f"El resultado es: {calculo1.multiplicar()}")
    elif opcion == 4:
        calculo1 = Calculadora2(numero1,numero2)
        print(f"El resultado es: {calculo1.dividir()}")
        
menu()