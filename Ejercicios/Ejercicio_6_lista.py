'''Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
Luego, intégrala como método en una clase Ordenador.'''

class Ordenador:
    
    def __init__(self, lista):
        self.lista = lista

    def ordena(self):
        for i in range(len(lista)-1):
            for j in range(len(lista)-1):
                if lista[j] > lista[j+1]:
                    num = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = num
        return self.lista
         
lista = [10,5,6,3,12]
ordena1 = Ordenador(lista)
print(f"Lista ordenada: {ordena1.ordena()}")