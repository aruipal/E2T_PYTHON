'''Crea una clase Estudiante con atributos para nombre, edad y calificación.
Implementa métodos getter y setter, y un método que determine si el estudiante 
aprobó (calificación mayor o igual a 6).'''

class Estudiante():
    def __init__(self, nombre, edad, calificacion):
        self.name = nombre
        self.age = edad
        self.score = calificacion
        
    def get_name(self):
        return self.name
        
    def set_name(self, nombre):
        self.name = nombre
    def get_name(self):
        return self.name
        
    def set_name(self, nombre):
        self.name = nombre      
