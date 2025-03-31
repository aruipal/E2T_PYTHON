"""
Habia una vez un sombrero. El sombrero no contenía conejo,
si no una lista de cinco números: 1, 2, 3, 4, 5.
- Escribe una linea de código que solicite al usuario qque reemplace
el número central con un número entero ingresado por el usuario.
- Escribe una linea de código que elimine el último elemento de la lista
- Escribe una linea de código que imprima la longitud de la lista
"""
hat_list = [1, 2, 3, 4, 5]
hat_list[2] = int(input("Introduzca un número: "))
del hat_list[4]
print(hat_list)
print(len(hat_list))