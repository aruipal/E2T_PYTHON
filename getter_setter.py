class Cuenta:
    def __init__(self,nom, sal, mon):
        self.__nombre = nom
        self.__saldo = sal
        self.__moneda = mon

    def get_saldo(self):
        return self.__saldo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_moneda(self):
        return self.__moneda
    
    def set_moneda(self, moneda):
        self.__moneda = moneda  

cuenta1 = Cuenta("Antonio", 1500, "Euros")
print(cuenta1.get_saldo())
print(cuenta1.get_moneda())
cuenta1.set_moneda("Dolares")
print(cuenta1.get_moneda())