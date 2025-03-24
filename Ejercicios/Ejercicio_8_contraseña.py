'''Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un 
número.'''


def comprobar(contraseña):
    caracter = ""
    if len(contraseña) >= 8:
        for i in contraseña:
            caracter += i
            
            if caracter == caracter.upper():
                print("Tiene mayuscula")
    else:
        print("Longitud invalida.")
    

print(comprobar("nfanAteria1537"))

#print(comprobar("infanteria1537"))

#print(comprobar("Infanteria"))