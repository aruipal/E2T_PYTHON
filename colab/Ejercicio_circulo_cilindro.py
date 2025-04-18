"""Función que calcula el area de un círculo.
Parámetros
radius: Es el radio del círculo.
Devuelve el área del círculo de radio radius. 
"""

def circle_area(radius):

    pi = 3.1415
    return pi*radius**2

"""Función que calcula el volumen de un cilindro.
Parámetros
radius: Es el radio de la base del cilindro.
high: Es la altura del cilindro.
Devuelve el volumen del clindro de radio radius y altura high.
"""

def cilinder_volume(radius, high):

    return circle_area(radius)*high

print(cilinder_volume(3,5))