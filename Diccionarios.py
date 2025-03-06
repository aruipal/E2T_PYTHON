'''
diccionario = {clave:valor,clave2:valor} Las claves son unicas y no se pueden modificar (inmutable).

Hacer una aplicación para tener una agenda de teléfonos.
Crear la clase Agenda.
Los teléfonos se guardarán en un diccionario con clave: nombre de contacto y
valor: teléfono.
Necesitamos los siguientes métodos:
    -__init__ (por supuesto que siempre hace falta)
    - Método para introducir nuevo contacto
    - Método para borrar nuevo contacto (por nombre)
    - Método para buscar un contacto (por nombre)
    - Método para mostrar TODA la agnda
'''
class Agenda:

    diccionario = {}

    def __init__(self):
        pass
        
    def set_nombre(self,nombre):
        self.nombre = nombre

    def get_nombre(self):
        return self.nombre
    
    def set_numero(self,numero):
        self.numero = numero
    
    def get_numero(self):
        return self.numero
    
    def introducir(self):
        nom_contacto = input("Introduce el nombre del contacto: ")
        num_contacto = int(input("Introduce el número del contacto: "))
        self.diccionario[nom_contacto] = num_contacto

    def borrar(self):
        nom_contacto = input("Introduce el contacto a borrar: ")
        self.diccionario.pop(nom_contacto)

    def buscar(self):
        nom_contacto = input("Introduce el contacto a buscar: ")
        print(self.diccionario[nom_contacto])

    def mostrar(self):
        print(self.diccionario)


    
        
                   


