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

asignaturas=["BD","HTML","PYTHON"]
class profesor():
    def __init__(self, nombre):
        self.nombre = nombre
        self.salario = float()

    def get_nombre(self):
        return self.nombre
    
    def get_asignatura(self):
        return self.asignatura
    
    def get_salario(self):
        return self.salario
    
    def set_asignatura(self, asignatura):
        self.asignatura = asignatura
        
    def set_salario(self, salario):
        self.salario = salario
        
    def asignar_asignatura(self):
        clase=int(input(f"Elija una opción de las siguientes para asignar una asignatura:\n1 BD\n2 HTML\n3 PYTHON\n"))
        while True:
            if clase >=1:
                self.asignatura = asignaturas[clase]
                break
            else:
                print("Elija un número válido.")
    
    def asignar_sueldo(self):
        horas=float(input("Introduzca el número de horas impartidas: "))
        if self.asignatura == asignaturas[0]:
            self.salario= horas*60
        elif self.asignatura == asignaturas[1]:
            self.salario= horas*70
        elif self.asignatura == asignaturas[2]:
            self.salario= horas*80
   
    def mostrar_datos(self):
        print(f"El profesor {self.nombre} imparte la asignatura {self.asignatura} y tiene un salario de {self.salario}€.")
         
profesor1 = profesor("Manolo")
profesor1.asignar_asignatura()
profesor1.asignar_sueldo()
profesor1.mostrar_datos()