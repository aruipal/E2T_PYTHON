class par:
    
    def __init__(self,lista):
        self.lista = lista

    def pares(self):
        long = len(self.lista)
        print(f"\nEn la lista hay {long} números en total\nY son pares:")
        for i in self.lista:
            if i % 2 == 0:
                print(i, end=", ")
            else:
                continue
            
par1 = par(lista = [1,2,3,4,5,6,7,8])
par1.pares()