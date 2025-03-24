'''Escribe una clase Dado que simule tirar un dado de 6 caras (usando random).
Incluye un método para tirar el dado y otro para mostrar el resultado.
EXTRA: Añade un selector de tipos de dados (d2, d4, d6, d8, d10, d12, d20)'''

import random

class Dado:
    def __init__(self):
        self.tirada = None

    def tirar(self, tipo):
        if tipo == "d6":
            self.tirada = random.randint(1, 6)
        elif tipo == "d2":
            self.tirada = random.randint(1, 2)

    def mostrar_resultado(self):
        print(f"El resultado es: {self.tirada}")


tipo = input("Elige el tipo de dado (d2, d4, d6, d8, d10, d12, d20): ")

dado1 = Dado()
dado1.tirar(tipo)
dado1.mostrar_resultado()