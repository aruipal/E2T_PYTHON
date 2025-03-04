'''
Crea la clase "Cuenta".
Cada cuenta tendrá un número (diferente a las demás) y un saldo (float).
El número de cuenta se puede consultar y modificar (getter y setter).
PERO el saldo sólo puede consultarse (getter).
Para modificar el saldo tenemos que hacer un ingreso o una retirada
'''
class Cuenta:

    def __init__(self,numero,saldo):
        self.numero = numero
        self.saldo = saldo

    def set_numero(self,account):
        self.numero = account

    def get_numero(self):
        return self.numero
    
    def get_saldo(self):
        return self.saldo

    def ingreso(self):
        cantidad = float(input("Cantidad a ingresar: "))
        self.saldo = cantidad + self.saldo
        print(f"El saldo es {self.saldo}")
        
    def retirada(self):
        cantidad = float(input("Cantidad a retirar: "))
        self.saldo = self.saldo - cantidad
        print(f"El saldo es {self.saldo}")

cuenta1 = Cuenta(145688723, 1200)
cuenta1.ingreso()
cuenta1.retirada()