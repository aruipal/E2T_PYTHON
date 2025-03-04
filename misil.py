''' realizar un programa que permita obtener los alcances y las alturas máximas del 
lanzamiento de un proyectil disparado con diferentes angulos y velocidades
'''
import math

class tiro:
    ang = 0
    vel = 0
    def __init__(self):
        pass

    def proyectil(self,vel,ang):
        self.vel = vel
        self.ang = ang
        velocidad = float(input("Introduce la velocidad: "))
        angulo = int(input("Introduce el angulo: "))
        g = 9.81

        angulo_rad= math.radians(angulo)
        alcance = (velocidad**2) * math.sin(2*angulo_rad) / g
        altura_max = (velocidad**2)*(math.sin(angulo_rad)**2)/(2*g)
        print(f"El alcance máx es: {round(alcance,2)}")
        print(f"La altura máx es: {round(altura_max,2)}")    

tiro1 = tiro()
tiro1.proyectil(100,45)