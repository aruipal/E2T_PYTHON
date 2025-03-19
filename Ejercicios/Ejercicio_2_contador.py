class Texto:
    
    def __init__(self, cadena):
        self.cadena = cadena

    def contador(self):
        print(f"La cadena de texto tiene {len(self.cadena.split())} palabras.")

texto1 = Texto(input("Introduce un texto: "))
texto1.contador()
