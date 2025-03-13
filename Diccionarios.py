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
import json

class Agenda():
    
    def __init__(self, archivo = "agenda.json"):
        self.archivo = archivo
        self.diccionario = self.cargar_agenda()
                    
    def guardar_agenda(self):
        with open(self.archivo, "w") as f:
            json.dump(self.diccionario, f, indent=4)
            print("Agenda guardada correctamente.")
    
    def cargar_agenda(self):
        with open(self.archivo, "r") as f:
            return json.load(f)
        
    def introducir(self):
        
        nom_contacto = input("Introduzca el nombre: ")
        nom_contacto = nom_contacto.upper()
        num_contacto = input("Introduzca el número: ")
        self.diccionario[nom_contacto] = num_contacto
        self.guardar_agenda()
        print(f"El contacto {nom_contacto} con el teléfono {num_contacto} se ha añadido.")
        
    def borrar(self):
        
        nom_contacto = input("Introduzca el nombre que quiere eliminar: ")
        nom_contacto = nom_contacto.upper()
        if nom_contacto in self.diccionario:
            self.diccionario.pop(nom_contacto)
            self.guardar_agenda()
            print(f"El contacto {nom_contacto} se ha borrado.")
        else:
            print(f"El contacto {nom_contacto} no existe.")      
        
    def buscar(self):
        nom_contacto = input("Introduzca el nombre que quiera buscar: ")
        nom_contacto = nom_contacto.upper()
        if nom_contacto in self.diccionario:
            print(f"El teléfono de {nom_contacto} es {self.diccionario[nom_contacto]}.")
        else:
            print(f"El contacto {nom_contacto} no existe.")
           
    def mostrar(self):
        print(f"Hay {len(self.diccionario)} contactos en la agenda:\n {self.diccionario}")
               
    def menu(self):
        while True:
            print(f"\n-- MI AGENDA TELEFONICA --\n  1. Introducir un contacto. \n  2. Eliminar un contacto. \n  3. Buscar un contacto.\n  4. Mostrar agenda.\n  5. Salir.")
            opcion=int(input(f"Elija una opción: "))
            if opcion == 1:
                agenda1.introducir()
            elif opcion == 2:
                agenda1.borrar()
            elif opcion == 3:
                agenda1.buscar()
            elif opcion == 4:
                agenda1.mostrar()
            elif opcion == 5:
                break
            else:
                print("Opción no válida.")
    
agenda1 = Agenda()
agenda1.menu()



    
        
                   


