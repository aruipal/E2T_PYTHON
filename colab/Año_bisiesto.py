# Tu tarea es escribir y probar una función que toma un argumento (año) y devuelve True
# si es un año bisiesto o False si no lo es.

def bisiesto(año):
  if año % 4 != 0:
    return False
  elif año % 4 == 0 and año % 100 != 0:
    return True
  elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    return False
  elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    return True

print(bisiesto(1999))
print(bisiesto(2000))