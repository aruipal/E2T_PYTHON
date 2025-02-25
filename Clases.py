''' Una clase es un objeto. Las funciones de una clase son metodos (lo que hace)
class Animal:
    patas = 2
    entorno = "terrestre"
    comidas = 0
    def comer():
        comidas += 1
Cada clase creada de un objeto es una instacia de esa clase
Una clase es un modelo de algo y dentro funciones
'''

class Militar:
    empleo = ""
    nombre = ""
    edad = int()

    def __init__(self): # init inicializa la clase, las funciones no pueden estar vacias. Self accede a todo lo de la clase militar
        pass #indicarle que es vacia para que no de error
        # self.nombre = nombre # self para acceder a las variables de la clase
    def saludo(self):
        print("A sus ordenes, buenos dias!")

    def dalenombre(self, name): # Metodo para modificar el nombre
        self.nombre = name
    def dimenombre(self): # Metodo para consultar el nombre
        print(f"El militar se llama: {self.nombre}")
    
    def daleempleo(self, rank):
        self.empleo = rank
    def dimeempleo(self):
        print(f"Su militar es: {self.empleo}")

    def daleedad(self, age):
        self.edad = age

    def dimeedad(self):
        print(f"El militar tiene: {self.edad} años.")

    def cumple(self):
        self.edad += 1  # Cada vez que llame al método le sume un año.

militar1 = Militar()
militar1.dalenombre("Antonio")
militar1.daleempleo("Sgto1")
militar1.daleedad(21)

militar1.dimenombre()
militar1.dimeempleo()
militar1.dimeedad()

militar1.cumple()
militar1.dimeedad()

#Fulanito = Militar() # Un objeto (clase) metido en una variable
#Menganito = Militar()
#print(type(Fulanito)) # Nos dice que es una clase

#Fulanito.saludo()
#Menganito.saludo()
