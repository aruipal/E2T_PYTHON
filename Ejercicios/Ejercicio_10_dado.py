'''Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
Incluye un método para tirar el dado y otro para mostrar el resultado.
EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)'''

import random

class Dado:
    def __init__(self):
        self.tirada = None

    def tirar(self):
        while True:
            global tipo
            tipo = input("\nElige las caras del dado (2,4,6,8,10,12 o 20), o pulse 1 para salir: ")
            if tipo == "1":
                break
            else:
                if tipo == "2":
                    self.tirada = random.randint(1, 2)
                    return self.mostrar_resultado() 
                elif tipo == "4":
                    self.tirada = random.randint(1, 4)
                    return self.mostrar_resultado() 
                elif tipo == "6":
                    self.tirada = random.randint(1, 6)
                    return self.mostrar_resultado() 
                elif tipo == "8":
                    self.tirada = random.randint(1, 8)
                    return self.mostrar_resultado() 
                elif tipo == "10":
                    self.tirada = random.randint(1, 10)
                    return self.mostrar_resultado() 
                elif tipo == "12":
                    self.tirada = random.randint(1, 12)
                    return self.mostrar_resultado() 
                elif tipo == "20":
                    self.tirada = random.randint(1, 20)
                    return self.mostrar_resultado() 
                else:
                    print(f"Error, introduce un número válido.")        
           
    def mostrar_resultado(self):
        print(f"Elegiste el dado de {tipo} caras.\nEl resultado es: {self.tirada}")
        self.tirar()

dado1 = Dado()
dado1.tirar()
