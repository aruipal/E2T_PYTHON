'''Escribe una función que reciba una cadena de texto y devuelva cuántas palabras contiene.
Luego, crea una clase Texto que use esa función como método y almacene el texto como atributo.'''

class Texto:
    def __init__(self, cadena):
        self.cadena = cadena
        print(self.contador())

    def contador(self):
        palabras = len(self.cadena.split())
        return f"La cadena de texto tiene {palabras} palabras."
    
texto1 = Texto(input("Introduce un texto: "))