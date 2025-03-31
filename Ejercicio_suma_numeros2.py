def calculo(num1, num2):
    suma = sum(range(min(num1, num2), max(num1, num2) + 1))
    return f"- La suma de todos los números es: {suma}."

# Solicitar entrada al usuario
num1 = int(input("Introduzca un número entero: "))
num2 = int(input("Introduzca otro número entero: "))

# Imprimir resultados
print(calculo(num1, num2))

# Prueba con valores fijos
print(calculo(10, 2))
