user_word = input("Ingrese una palabra: ")
user_word= user_word.upper()
vocales = "aeiouAEIOU"
word_without_vowels = ""

for letra in user_word:
  if letra in vocales:
    continue
  else:
    word_without_vowels += letra
print(word_without_vowels)