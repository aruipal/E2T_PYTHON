mi_agenda = {
    "Alicia": 2222,
    "Roberto": 1111,
    "Lucía": 3333,
    "Andrés": 5555
}

for clave in mi_agenda:
    print(clave, ":", mi_agenda[clave])

# Metodo keys
vista_claves = list(mi_agenda.keys()) # convertir claves a lista
print(vista_claves)

vista_claves = mi_agenda.keys()
for clave in vista_claves:
    print(clave)

# Metodo values
print(mi_agenda.values()) # ver los valores del diccionario

print(list(mi_agenda.values())) # Convertirlo en lista

if 1111 in mi_agenda.values():
    print("Ese valor esta en el diccionario")

for valor in mi_agenda.values():
    print(valor)

# Metodo items
print(mi_agenda.items()) # vista clave valor

for clave, valor in mi_agenda.items():
    print(clave, valor)