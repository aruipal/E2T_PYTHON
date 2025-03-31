user_word = input("Ingrese una palabra: ")
user_word= user_word.upper()

consonantes = ""

for letra in user_word:
  if letra == "A":
    continue
  elif letra == "E":
    continue
  elif letra == "I":
    continue
  elif letra == "O":
    continue
  elif letra == "U":
    continue
  else:
    consonantes += letra

print(", ".join(consonantes))
