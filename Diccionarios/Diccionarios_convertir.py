''' 
- Convertir un diccionario en dos listas.
- Convertir dos listas en un diccionario.
'''

pares = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5}

letras = []
numeros = []

for clave, valor in pares.items():
    letras.append(clave)
    numeros.append(valor)
print(letras)
print(numeros)

# Otra manera usando metodos

letters = list(pares.keys())
numbers = list(pares.values())
print(letters)
print(numbers)

# Hacer un diccionario a partir de dos listas
let = ["A", "B", "C", "D", "E"]
num = [1, 2, 3, 4, 5]

par = {}

for i in range(len(let)):
    par[let[i]] = num[i]

print(par)

# Otra manera mediante zip
lista1 = ["A", "B", "C", "D", "E"]
lista2 = [1, 2, 3, 4, 5]

dicc = dict(zip(lista1, lista2))
print(dicc)

# Otra manera de crear un diccionario
d = dict([(1,1), (2,2), (3,3)])
print(d)