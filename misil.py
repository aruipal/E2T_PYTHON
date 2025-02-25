''' realizar un programa que permita obtener los alcances y las alturas máximas del 
lanzamiento de un proyectil disparado con diferentes angulos y velocidades
'''

import math

a = float(input("Introduce la velocidad: "))
b = int(input("Introduce el angulo min: "))
c = int(input("Introduce el angulo max: "))
g = input("¿La gravedad es 9.81? escriba si o no: ")
gravedad = 9.81

if g == "no":
    g = float(input("Introduce el valor de la gravedad: "))
else:
    g = gravedad

def proyectil(velocidad,angulo,g):
    angulo_rad= math.radians(angulo)
    alcance = (velocidad**2) * math.sin(2*angulo_rad) / g
    altura_max = (velocidad**2)*(math.sin(angulo_rad)**2)/(2*g)
    print(f"El alcance máx es: {round(alcance,2)}")
    print(f"La altura máx es: {round(altura_max,2)}")    

proyectil(a,b,g)