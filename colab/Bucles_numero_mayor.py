# Almacena el actual
mayor_number = 0

# Ingresa el primer valor
number = int(input("Introduce un número o escribe -1 para detener: "))

while number != -1:
    if number > mayor_number: # Si es mayor actualiza la variable
        mayor_number = number
    # Ingresa el siguiente número
    number = int(input("Introduce un número o escribe -1 para detener: "))
# Imprime el número más grande
print("El número más grande es:", mayor_number)