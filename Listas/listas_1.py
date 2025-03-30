'''
1. Crea una lista vacia llamada letras (usando una función)
2. Añade la letra "a" a esa lista (usando un método)
3. Haz una copia de la lista (creando una lista distinta)
4. Añade la letra "b" a la copia de la lista
5. Comprueba los elementos de las dos listas
'''

letras = []
letras.append("a")

copia_letras = list(letras)

copia_letras.append("b")

print(letras)
print(copia_letras)

# Reverso de una lista
numeros = [1, 5, 8, 4, 7, 2, 9]
print(numeros)
reverso = []

for n in range(len(numeros)):
    reverso.append(numeros[len(numeros)-1-n])

print(reverso)

# Otra forma
numeros = [1, 5, 8, 4, 7, 2, 9]
print(numeros)
reverso = []

for n in numeros:
    reverso = [n] + reverso
    # print(reverso)

print(reverso)

print(numeros[0:3])

reverso = numeros[0:6:2] # del indice 0 al 6 con salto 2
print(reverso)

numeros = [1, 5, 8, 4, 7, 2, 9]
reverso = numeros[2:6:-2]
print(reverso)