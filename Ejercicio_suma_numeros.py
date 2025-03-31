'''Realice un programa que reciba como parámetros 2 números enteros.
La función sumará todos los números entre esos dos números, ambos incluidos.
Finalmente imprimirá en pantalla el número obtenido.'''

def calculo(num1, num2):
    lista = []
    if num1 < num2:
        for i in range(num1, num2+1):
            lista.append(i) 
        return f"- La suma de todos los números es: {sum(lista)}."
    else:
        for i in range(num2, num1+1):
            lista.append(i)
        return f"- La suma de todos los números es: {sum(lista)}."
             
print(calculo(num1 = int(input("Introduzca un número entero: ")), num2 = int(input("Introduzca otro número entero: "))))

print(calculo(10,2))