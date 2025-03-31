# Adivina el número secreto

secret_number = 1234
user_number = int(input("Adivina el número secreto: "))

while user_number != secret_number:
  print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
  user_number = int(input("Adivina el número secreto: "))

print("¡Bien hecho!, Eres libre ahora.")