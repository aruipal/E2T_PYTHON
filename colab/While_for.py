# WHILE, la rama else del bucle siempre se ejecuta una vez, independientemente de si
# el bucle ha entrado o no en su cuerpo.
i = 1
while i < 5:
  print(i)
  i += 1
else:
  print("else:", i)

# Modifica el fragmento para que el bucle no tenga oportunidad de ejecutar el cuerpo ni una sola vez:
i = 6
while i < 5:
  print(i)
  i += 1
else:
  print("else:", i)

# FOR, se comporta un poco diferente
for i in range(5):
  print(i)
else:
  print("else:", i) # El resultado puede ser un poco sorprendente, la variable i conserva su último valor.

# Aqui el cuerpo del bucle no se ejecutará. Hemos asignado la variable i antes del bucle.
i = 111
for i in range(5):
  print(i)
else:
  print("else:", i)