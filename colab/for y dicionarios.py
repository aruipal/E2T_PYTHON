# Forma básica de acceso a diccionarios:
valores = {'j': 1, 'a': 3, 'm': 7, 'e': 9, 's': 40}
for x in valores:
    print("clave", x, end=" | ") # accede a la clave
    print("valor:", valores[x])

# Accediendo directamente a los valores
for y in valores.values():
    print(y)

# El equivalente a values, es keys para las claves
for z in valores.keys():
    print(z)

# Ahora veamos, como podría obtener ambos, mediante el uso de items:
w = valores.items()
print(type(w), w)

# Tenemos un objeto del tipo dict_items, que nos permite hacer esto:
for a, b in w: # recordemos que w es valores.items
    print("clave:", a, " | valor: ", b)