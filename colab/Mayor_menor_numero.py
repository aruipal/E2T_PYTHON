# Usando uno de los operadores de comparacion en Python, escribe un programa simple de dos lineas que tome el
# parametro n como entrada, que es un entero, e imprime False si n es menor que 100, y True si n es mayor o igual que 100.

n = int(input("Introduce un numero: "))
n >= 100

# Identificar el mayor de dos numeros introducidos
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
if number1 > number2:
  large_number = number1
else:
  large_number = number2
print("El número más grande es: ", large_number)