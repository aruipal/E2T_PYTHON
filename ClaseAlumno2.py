class Alumno:

    def __init__(self, age):
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.edad = age
    
    def set_nombre(self, name):
        self.nombre = name

    def get_nombre(self):
        return self.nombre