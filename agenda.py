import json 
import os
import datetime

class Agenda:

    def __init__(self, archivo="contactos.json"):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def cargar_contactos(self):
        if os.path.exists(self.archivo): # Si el archivo existe
            with open(self.archivo, "r") as f: # Abrelo como lectura y alias f
                return json.load(f) # Carga f que es self.archivo, archivo contactos.json
        else:
            return {} # si no existe el archivo json, crea un diccionario en self.contactos
    
    def mostrar_agenda(self):
        if self.contactos: # Si hay contactos
            for nombre, info in self.contactos.items(): #recorre el diccionario nombre y el diccionario info
                print(f"Nombre: {nombre}\nTelefono: {info['telefono']}\nEmail: {info['email']}\n") # Dentro de info está telefono y email.
        else:
            print("La agenda está vacia.")

    def buscar_contactos(self):
        nombre = input("Introduzca el nombre que quiera buscar: ")
        nombre = nombre.upper()
        if nombre in self.contactos:
            info = self.contactos[nombre]
            print(f"Nombre: {nombre}\nTelefono: {info['telefono']}\nEmail: {info['email']}")
        else:
            print(f"El contacto {nombre} no existe.")

    def borrar_contactos(self):
        nombre = input("Introduzca el nombre que quiere eliminar: ")
        nombre = nombre.upper()
        if nombre in self.contactos:
            self.contactos.pop(nombre) # del self.contactos[nombre]
            # self.guardar_agenda()
            print(f"El contacto {nombre} se ha borrado.")
        else:
            print(f"El contacto {nombre} no existe.")

    def meter_contacto(self):
        nombre = input("Introduzca el nombre: ")
        nombre = nombre.upper()
        telefono = input("Introduzca el teléfono: ")
        mail = input("Introduzca el mail: ")
        self.contactos[nombre] = {"telefono": telefono, "email": mail}
        # tambien con: self.contactos.update({nombre: {"telefono": telefono, "email": mail}})

    def guardar_agenda(self):
        with open(self.archivo, "w") as f:
            json.dump(self.contactos, f, indent=4)
            now = datetime.datetime.now()
            formato_hora = now.strftime('%d %b %Y a las %H:%M')
            print(f"Agenda guardada correctamente el: {formato_hora}.")

agenda1 = Agenda()

def menu():
        while True:
            print(f"\n-- MI AGENDA TELEFONICA --\n  1. Introducir un contacto. \n  2. Eliminar un contacto. \n  3. Buscar un contacto.\n  4. Mostrar agenda.\n  5. Guardar agenda.\n  6. Salir.")
            opcion=int(input(f"Elija una opción: "))
            if opcion == 1:
                agenda1.meter_contacto()
            elif opcion == 2:
                agenda1.borrar_contactos()
            elif opcion == 3:
                agenda1.buscar_contactos()
            elif opcion == 4:
                agenda1.mostrar_agenda()
            elif opcion == 5:
                agenda1.guardar_agenda()
            elif opcion == 6:
                break
            else:
                print("Opción no válida.")

if __name__ == "__main__": # el archivo main es en el que estoy agenda.py
    menu()
