'''Crea una clase Rectangulo con atributos para ancho y alto.
Incluye métodos para calcular el área y el perímetro, usando un constructor para inicializar los valores.'''

class Rectangulo:

    def __init__(self, anchura, altura):
        self.ancho = anchura
        self.alto = altura

    def area(self):
        calculo_area = self.ancho * self.alto
        return calculo_area
    
    def perimetro(self):
        calculo_perimetro = self.ancho * 2 + self.alto * 2
        return calculo_perimetro

while True:
    try:
        a = float(input("Introduce un lado del rectángulo: "))
        b = float(input("Introduce el otro lado:"))

        rectangulo1 = Rectangulo(a,b)

        print(f"El area del rectángulo es: {rectangulo1.area()}")
        print(f"El perímetro del rectángulo es: {rectangulo1.perimetro()}")
        break
    
    except ValueError:
        print("Introduce un número válido.")
