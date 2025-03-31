largest_number = -9999999999
counter = 0

number = int(input("Ingrese un numero o escribe -1 para detener: "))

while number != -1:
  if number == -1:
    continue
  counter += 1
  if number > largest_number:
    largest_number = number
  number = int(input("Ingrese un numero o escribe -1 para detener: "))

if counter:
  print("El numero mas grande es:", largest_number)
else:
  print("No has ingresado ningun numero.")