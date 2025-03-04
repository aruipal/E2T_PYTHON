'''
Crea una clase Profesor que tenga los siguientes atributos:
- Nombre (getter)
- Asignatura (setter y getter)
- Salario (nº horas x €)
El salario de los profesores es un valor fijo tipo float.
Crear getter y setter para cada atributo.

Crea la calse ProfesorAsociado, que hereda de profesor, psero cuyo salario es el resultado de sus
horas de clase multiplicado por el precio hora (se puede "hardcodear" el precio hora).
'''

class Profesor:
    salario = float()

    def __init__(self,nombre, asignatura):
        self.nombre = nombre
        self.asignatura = asignatura
        
    def set_asignatura(self,asig):
        self.asignatura = asig

    def get_asignatura(self):
        return self.asignatura