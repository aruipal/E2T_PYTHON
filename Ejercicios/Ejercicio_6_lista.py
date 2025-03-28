'''Escribe una función que reciba una lista de números y la ordene de menor a mayor sin usar sort().
Luego, intégrala como método en una clase Ordenador.'''

class Ordenador:
    
    def __init__(self, lista):
        self.lista = lista

    def ordena(self):
        for i in range(len(self.lista)-1):
            for j in range(len(self.lista)-1):
                if self.lista[j] > self.lista[j+1]:
                    num = self.lista[j]
                    self.lista[j] = self.lista[j+1]
                    self.lista[j+1] = num
        return self.lista

def ordena_numeros():    
    try:
        lista_num = []
        while True:
            numero = int(input("Introduce un número, o pulse 0 para salir: "))
            if numero == 0:
                ordena1 = Ordenador(lista_num)
                print(f"Lista ordenada: {ordena1.ordena()}")
                break
            lista_num.append(numero)
        
    except ValueError:
        print("Introduce solo números.")
        ordena_numeros()
           
ordena_numeros()