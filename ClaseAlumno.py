'''
Crea una clase Alumno en la que todos tengan:
    - Nombre
    - Apellidos
    - Edad
Crea los setter y getter de esos atributos.
Crea un método que me diga si el alumno es mayor de edad.
'''

class Alumno:
        
    def __init__(self,nombre,apellidos,edad):
        self.años = edad
        self.nomb = nombre
        self.apel = apellidos

    def setedad(self,edad):
        self.años = edad

    def getedad(self):
        return self.años
    
    def setnombre(self,nombre):
        self.nomb = nombre

    def getnombre(self):
        return self.nomb
    
    def setapellidos(self,apellidos):
        self.apel = apellidos

    def getapellidos(self):
        return self.apel

    def adulto(self):
        if self.años >= 18:
            print(f"El alumno {self.nomb} es mayor de edad.")
        else:
            print(f"El alumno {self.nomb} NO es mayor de edad.")

alumno1 = Alumno("Antonio", "Ruiz", 25)
alumno1.adulto()

print(alumno1.getnombre())


alumno2 = Alumno("Benito", "Carmela", 17)
alumno2.setedad(20)
alumno2.adulto()
