'''Crea una clase CuentaBancaria con atributos para titular y saldo.
Añade métodos para depositar, retirar y consultar el saldo. 
Usa el manejo de excepciones para evitar saldos negativos.
'''

class CuentaBancaria:
    
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self,ingreso):
        self.saldo = self.saldo + ingreso
        return self.consultar()
    
    def retirar(self,retirada):
        try:
            if self.saldo - retirada < 0:
                raise ValueError("No se puede retirar más cantidad del saldo disponible.")
            else:
                self.saldo = self.saldo - retirada
                return self.consultar()
        except ValueError as e:
            print(e)
    
    def consultar(self):
        print(f"\nEl titular {self.titular} tiene un saldo de {self.saldo}€.")

cuenta1 = CuentaBancaria("Antonio Ruiz", 1200)

def menu():
    while True:
        opcion = int(input("Elija la opción deseada:\n\t1.Consultar saldo\n\t2.Retirada\n\t3.Ingreso\n\t4.Salir\n--->"))
        if opcion == 4:
            break
        elif opcion == 1:
            cuenta1.consultar()
        elif opcion == 2:
            retirar = int(input("Indique la cantidad a retirar: "))
            cuenta1.retirar(retirar)
        elif opcion == 3:
            ingresar = int(input("Indique la cantidad a ingresar: "))
            cuenta1.depositar(ingresar)
        else:
            print("Opción incorrecta.")
menu()     


