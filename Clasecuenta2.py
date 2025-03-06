import random

class Cuenta:
 
    def __init__(self, saldo_inicial):
        self.numero = random.randint(100000000, 999999999) # numero cuenta aleatorio desde hasta.
        # self.numero = num_cuenta
        self.saldo = saldo_inicial     

    def setnumero(self, num):
        self.numero = num
    
    def getnumero(self):
        return self.numero
    
    def getsaldo(self):
        return self.saldo
    
    def ingreso(self):
        cantidad = float(input("Cantidad a ingresar: "))
        self.saldo += cantidad #El valor de saldo mas la cantidad self.saldo + cantidad
        print(f"El saldo es {self.saldo}€.")

    def retirada(self):
        cantidad = float(input("Cantidad a retirar: "))
        if cantidad > self.saldo:
            print(f"No tienes suficiente saldo en tu cuenta.\nEl saldo actual es: {self.saldo}€.")
        else:
            self.saldo -= cantidad
            print(f"El saldo es {self.saldo}€.")

cuenta1 = Cuenta(1000)
cuenta2 = Cuenta(1500)
cuenta3 = Cuenta(2000)
print(cuenta1.getnumero())
print(cuenta2.getnumero())
print(cuenta3.getnumero())
cuenta1.ingreso()
cuenta1.retirada()