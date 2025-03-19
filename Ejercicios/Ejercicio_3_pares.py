class par:
    
    def __init__(self,lista):
        self.lista = lista

    def pares(self):
        long = len(self.lista)
        print(f"\nEn la lista hay {long} números en total\nY son pares:")
        for i in self.lista:
            if i % 2 == 0:
                print(i,end=" ")

lista = []            
while True:
    num = input("Introduce numeros y pulsa 0 para terminar: ")
    if num == str(0):
        break
    else:
        lista.append(int(num))

par1 = par(lista)
par1.pares()