'''Realice un programa que reciba como parámetros 2 números enteros.
La función sumará todos los números entre esos dos números, ambos incluidos.
Finalmente imprimirá en pantalla el número obtenido.'''



def calculo(num1, num2):
    lista = []
    
    
    for i in range(num1, num2+1):
        lista.append(i)
    
    return sum(lista)
        
       
print(calculo(2,10))

print(calculo(10,2))