import math

class tiro:
    
    def __init__(self):
        self.vel = 0
        self.ang = 0

    def setvel(self):
        vel_proyectil=int(input("Introduce la velocidad: "))
        self.vel = vel_proyectil

    def getvel(self):
        print(f"La velocidad seleccionada es: {self.vel}.")
       

    def setang(self):
        ang_proyectil=int(input("Introduce el angulo: "))
        self.ang = ang_proyectil

    def getang(self):
        print(f"El angulo seleccionado es: {self.ang}.")

    def proyectil(self):
        g = 9.81
        angulo_rad= math.radians(self.ang)
        alcance = (self.vel**2) * math.sin(2*angulo_rad) / g
        altura_max = (self.vel**2)*(math.sin(angulo_rad)**2)/(2*g)
        print(f"El alcance máx es: {round(alcance,2)}.")
        print(f"La altura máx es: {round(altura_max,2)}.")
 

while True:
    tiro1 = tiro()
    tiro1.setvel()
    tiro1.setang()
    tiro1.proyectil()
    continuar = input("¿Deseas realizar otro cálculo? Escriba si o no: ")
    if continuar.lower() != 'si':
        break
    
