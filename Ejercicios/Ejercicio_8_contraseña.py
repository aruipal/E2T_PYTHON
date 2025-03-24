'''Diseña una clase Validador con un atributo para una contraseña.
Incluye un método que verifique si la contraseña tiene al menos 8 caracteres, una mayúscula y un número.'''

class Validador:

    def __init__(self, password):
        self.password = password

    def comprobar(self):
        mayuscula = False
        numero = False

        for i in self.password:
            if i.isupper():
                mayuscula = True
            if i.isdigit():
                numero = True

        if len(self.password) < 8:
            return "La contraseña tiene que tener 8 o más caracteres."
        if mayuscula == False:
            return "La contraseña tiene que tener al menos una letra mayúscula."
        if numero == False:
            return "La contraseña tiene que tener al menos un número."
    
        return "La contraseña es válida."

contraseña = input("Verificador de contraseñas.\n  - Introduce una contraseña: ")
comprobar1 = Validador(contraseña)
print(comprobar1.comprobar())