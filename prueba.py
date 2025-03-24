def validar_contraseña(contraseña):
    tiene_mayuscula = False
    tiene_numero = False

    for caracter in contraseña:
        if caracter.isupper():
            tiene_mayuscula = True
        if caracter.isdigit():
            tiene_numero = True

    if len(contraseña) < 8:
        return "La contraseña debe tener al menos 8 caracteres."
    if not tiene_mayuscula:
        return "La contraseña debe tener al menos una letra mayúscula."
    if not tiene_numero:
        return "La contraseña debe tener al menos un número."
    
    return "La contraseña es válida."

contraseña = input("Ingresa una contraseña: ")
resultado = validar_contraseña(contraseña)
print(resultado)
