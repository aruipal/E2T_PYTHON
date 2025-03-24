'''Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
Incluye un método para tirar el dado y otro para mostrar el resultado.
EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)'''

import random

class Dado:
    def __init__(self):
        self.tirada = None

    def tirar(self):
        self.tirada = random.randint(1, 6)

    def mostrar_resultado(self):
        print(f"El resultado es: {self.tirada}")

dado1 = Dado()
dado1.tirar()
dado1.mostrar_resultado()