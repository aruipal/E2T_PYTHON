# CASO DE USO BREAK:
# Quiero hacer un for, que cuando consiga un elemento realice una acción y se detenga:

grupo = [1, 2, 3, 4, 5, 6, 9]
for e in grupo:
    if e == 4:
        print("elemento inválido") #Esta es mi acción
        break
    print(e)

# CASO DE USO CONTINUE:
# Quiero hacer un bucle for, pero que no imprima los números pares

for x in range(20):
    if x % 2 == 0:
      continue
    print(x)