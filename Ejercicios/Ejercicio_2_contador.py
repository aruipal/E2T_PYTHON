'''Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.'''

class Texto:
    
    def __init__(self, cadena):
        self.cadena = cadena

    def contador(self):
        print(f"La cadena de texto tiene {len(self.cadena.split())} palabras.")

texto1 = Texto(input("\n-Contador de palabras- \n\tIntroduce un texto: "))
texto1.contador()
