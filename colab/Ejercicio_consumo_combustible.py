# La tarea es escribir un par de funciones que conviertan l/100km a mpg, y viceversa.
# 1 milla americana = 1609.344 metros
# 1 galón americano = 3.785411784 litros

def liters_100km_to_miles_gallon(liters_100km):
  miles_per_kilometer = 1 / 1.609344  # Convertimos la distancia de kilómetros a millas
  gallons_per_liter = 1 / 3.785411784 # Convertimos el volumen de litros a galones
  miles_per_100km = 100 * miles_per_kilometer # Calculamos las millas recorridas en 100 kilómetros
  gallons_per_100km = liters_100km * gallons_per_liter  # Calculamos los galones consumidos en 100 kilómetros

  return miles_per_100km / gallons_per_100km # Calculamos el número de millas por galón dividiendo las millas por los galone


def miles_gallon_to_liters_100km(miles_gallon):
  kilometers_per_mile = 1.609344  # Convertimos la distancia de millas a kilómetros
  liters_per_gallon = 3.785411784  # Convertimos el volumen de galones a litros
  kilometers_per_gallon = miles_gallon * kilometers_per_mile #Calculamos los kilómetros recorridos por galón
  liters_per_100km = 100 / kilometers_per_gallon * liters_per_gallon  # Calculamos los litros consumidos en 100 kilómetros dividiendo 100 kilómetros por los kilómetros por galón y multiplicando por los litros por galón

  return liters_per_100km # Retornamos el valor calculado

print("Conversión del consumo de combustible.\n---------------------------------------")
print("Opcion 1: de l/100km a mpg")
print("Opcion 2: de mpg a l/100km")
opcion = int(input("Introduce una opción: "))
if opcion == 1:
  liters = float(input("Introduce el numero de litros a convertir: "))
  print(round(liters_100km_to_miles_gallon(liters),2))
if opcion == 2:
  gallon = float(input("Introduce el número de galones a convertir: "))
  print(miles_gallon_to_liters_100km(gallon))


