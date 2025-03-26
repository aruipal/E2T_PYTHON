'''Crea una clase Estudiante con atributos para nombre, edad y calificación.
Implementa métodos getter y setter, y un método que determine si el estudiante 
aprobó (calificación mayor o igual a 6).'''

class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def set_nombre(self, nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self, edad):
        self.edad = edad
        
    def get_edad(self):
        return self.edad
   
    def set_calificacion(self,calificacion):
        self.calificacion = calificacion

    def get_calificacion(self):
        return self.calificacion
    
    def notas(self):
        try:
            self.calificacion = float(input("Introduzca la nota: "))
            if self.calificacion >= 6:
                return "está aprobado."
            else:
                return "está suspenso."
        except ValueError:
            return "Introduzca un valor numérico."          
 
estudiante1 = Estudiante("Antonio Ruiz",23)
print(f"Nombre: {estudiante1.get_nombre()}, edad: {estudiante1.get_edad()}")
print(estudiante1.notas())
