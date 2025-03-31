# 1. Crea una lista vacia
beatles = []

# 2. Usa append() para agregar los siguientes miembros:
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

print("Paso 2:", beatles)

# 3. Emplea el bucle for y append() para pedirle al usuario que agregue los siguientes miembros:

for miembros in range(2):
  beatles.append(input("Nuevo miembro de la banda: "))

print("Paso 3:", beatles)

# 4. Usa la instrucción del para eliminar a los dos últimos miembros
del beatles[-1] # Esto es el último, tambien se puede por indice [4]
del beatles[-1]

print("Paso 4:", beatles)

# 5. usa el método insert() para agregar Ringo Starr al principio de la lista
beatles.insert(0, "Ringo Starr")

print("Paso 5:", beatles)