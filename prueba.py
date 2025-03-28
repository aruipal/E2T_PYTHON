'''Ejercicio 16: Programa de gestión de tareas.
Define una clase Tarea con atributos titulo, descripcion y completada.
Implementa métodos para añadir, eliminar, marcar como completada y listar todas las tareas.
Guarda la lista de tareas en un archivo JSON y permite cargarla al iniciar el programa.
Usa la librería os para gestionar los archivos y directorios necesarios.'''

import os
import json

class Tarea:
    
    def __init__(self, title = "recursos/tareas.json"):
        self.archivo = title
        self.tareas = self.cargar_tareas()
        
    def cargar_tareas(self):
        if os.path.exists(self.archivo): # si el archivo existe
            with open(self.archivo,"r") as f: # lectura, necesario alias
                return json.loads(f)
        else:
            return {} # si el archivo no existe me devuelve un diccionario vacio
        
    def anadir_tarea(self):
        self.titulo = input("Introduzca el nombre de la tarea: ")
        self.descripcion = input("Introduzca la descripción de la tarea: ")
        self.completada = "No completada"
        self.tareas[self.titulo] = {
            "Descripción" : self.descripcion,
            "Estado" : self.completada
        }
    
    def eliminar_tarea(self):
        self.delete = input("Introduzca la tarea que quiere borrar: ")
        self.tareas.pop(self.delete)
        
    def marcar_completa(self):
        self.completar = 