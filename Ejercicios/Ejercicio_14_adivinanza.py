'''Crea una clase Adivinanza que genere un número aleatorio entre 1 y 100 (usa random).
Incluye un método que permita al usuario adivinar y devuelva pistas ("más alto" o "más bajo") hasta que acierte.'''

import random

class Adivinanza:

    def __init__(self, numero):
        self.number = numero
        self.aleatorio = random.randint(1,100)
        self.contador = 0

    def adivina(self):
        while True:
            self.contador += 1
            if self.number > self.aleatorio:
                print("Más bajo")   
            elif self.number < self.aleatorio:
                print("Más alto")   
            elif self.number == self.aleatorio:
                return f"¡¡¡Acertaste!!!, en {self.contador} intentos."
            self.number = int(input("Adivina el número: "))


adivina1 = Adivinanza(int(input("Adivina el número: ")))
print(adivina1.adivina())
