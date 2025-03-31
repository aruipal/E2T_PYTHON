class Calculadora:
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2   
      
    def sumar(self):
        suma = self.num1 + self.num2
        print(f"La suma de {self.num1} + {self.num2} es: {suma}")
              
    def restar(self):
        resta = self.num1 - self.num2
        print(f"La resta de {self.num1} - {self.num2} es: {resta}")
        
    def multiplicar(self):
        multiplica = self.num1 * self.num2
        print(f"La multiplicación de {self.num1} X {self.num2} es: {multiplica}")
        
    def dividir(self):
        divide = self.num1 / self.num2
        print(f"La división de {self.num1} / {self.num2} es: {divide}")
        
def menu():
    while True:
        try:
            print("\n>>> Calculadora <<<\n 1.Sumar\n 2.Restar\n 3.Multiplicar\n 4.Dividir\n 5.Salir")
            
            opcion = int(input("Elige la opción: "))
            if opcion > 5:
                print("Operación no válida introduce un núm del 1 al 5.")
            elif opcion == 5:
                break

            num1 = float(input("Introduce un número: "))
            num2 = float(input("Introduce otro número: "))
        
            calculadora1 = Calculadora(num1,num2)

            if opcion == 1:
                calculadora1.sumar()
            elif opcion == 2:
                calculadora1.restar()
            elif opcion == 3:
                calculadora1.multiplicar()
            elif opcion == 4:
                calculadora1.dividir()

        except ValueError:
            print("Opción incorrecta, introduce un NUMERO!!!")
        
menu()
  