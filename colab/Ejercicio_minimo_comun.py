def MinimoComunMultiplo(numero1, numero2):
  if numero1 > 0 and numero2 > 0:
    if numero1 >= numero2:
      mcm = numero1 * 2
      numero = numero1
    else:
      mcm = numero2 * 2
      numero = numero2
    while mcm % numero1 != 0 or mcm % numero2 != 0:
      mcm += numero
    print(f"\n El mcm de {numero1} y {numero2} es = {mcm}")
  else:
    print("Numero introducido incorrecto, debe ser positivo.")

MinimoComunMultiplo(8, 12)