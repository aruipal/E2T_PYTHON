'''Crea una clase Numeros con un atributo que sea una lista de enteros.
Incluye un método que devuelva solo los números pares de esa lista.'''

class Numeros:
    
    def __init__(self, enteros):
        self.enteros = enteros
        self.pares()
        
    def pares(self):
        for i in self.enteros:
            if i % 2 == 0:
                print(f"Par: {i}")
            
lista1 = [1,2,3,4,5,6,7,8]
numero1 = Numeros(lista1)        
print()
lista2 = [9,8,7,4,3]
numero2 = Numeros(lista2)