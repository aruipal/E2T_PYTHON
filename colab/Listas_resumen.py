# 1. la lista es un tipo de dato en Python que se utiliza para almacenar multiples objetos.
# Es un acolección ordenada y mutable de elementos separados por comas entre corchetes:

my_list = [1, None, True, "Soy una cadena", 256, 0]

# 2. Las listas se pueden indexar y actualizar:

print(my_list[3])
print(my_list[-1])

my_list[1] = "?"
print(my_list)

my_list.insert(0, "primero")
my_list.append("ultimo")
print(my_list)

# 3. Las listas pueden estar anidadas:

my_list2 = [1, "a", ["lista", 64, [0, 1], False]]
print(my_list2)

# 4. Los elementos de la lista y la lista se pueden eliminar:

my_list = [1, 2, 3, 4]
del my_list[2]
print(my_list)

del my_list

# 5. Las listas pueden ser iteradas mediante el uso del bucle for:

my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
for color in my_list:
  print(color)

# 6. La función len() se puede usar para verificar la longitud de la lista:

my_list = ["blanco", "purpura", "azul", "amarillo", "verde"]
print(len(my_list))

del my_list[2]
print(len(my_list))