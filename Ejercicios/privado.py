
class Alumno:
    def __init__(self, nom, anos):
        self.__nombre = nom
        self.edad = anos
        
    def set_nombre(self,nombre):
        self.__nombre = nombre
        
    def get_nombre(self):
        return self.__nombre
                        
fulano = Alumno("fulano", 16)
print(fulano.edad)

fulano.edad = 17
print(fulano.edad)

# print(fulano.__nombre) #error, atributo privado

print(fulano.get_nombre())

