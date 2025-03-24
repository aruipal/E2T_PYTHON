'''Crea una clase Notas con una lista de calificaciones como atributo.
Implementa un método que calcule el promedio y otro que devuelva la nota más alta. 
Añade manejo de excepciones para evitar notas inferiores a 0 o superiores a 10.'''

class Notas:

    def __init__(self, calificaciones):
        self.calificaciones = calificaciones

    def promedio(self):
        media = sum(self.calificaciones) / len(self.calificaciones)
        return round(media,2)

    def maxima(self):
        alta = max(self.calificaciones)
        return alta

lista = []

while True:
    try:
        notas = float(input("Introduce las notas y pulse 99 para salir: "))
        if notas == 99:
            break
        
        if notas < 0 or notas > 10:
            raise ValueError("Las notas deben estar entre 0 y 10.")
        lista.append(notas)

    except ValueError as e:
        print(e)
            
notas1 = Notas(lista)
print(f"La media es de: {notas1.promedio()}")
print(f"La nota más alta es de: {notas1.maxima()}")
