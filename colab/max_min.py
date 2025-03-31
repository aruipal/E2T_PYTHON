number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
number3 = int(input("Ingresa el tercer número: "))

# Verifica cuál de los números es el mayor y pásalo a la variable
largest_number = max(number1, number2, number3)
min_number = min(number1, number2, number3)

print("El número más grande es:", largest_number)
print("El número más pequeño es:", min_number)