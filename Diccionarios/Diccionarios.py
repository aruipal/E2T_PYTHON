telefonos = {"José": 1234,
             "María": 3456,
             "Paco": 6789,
             "Ana": 9876          
}

print(telefonos["María"])

print(len(telefonos))

print("José" in telefonos)

if "Julia" in telefonos:
    print(telefonos["Julia"])
else:
    print("No exite.")    

try:
    buscar = input("Introduce nombre a buscar: ")
    busqueda = telefonos[buscar]
    print(busqueda)
except:
    print("No existe.")

# Añadir elementos nuevos
telefonos["Jorge"] = 6543

nuevo = input("Introduce el nombre a añadir: ")
telefono = int(input("Introduce el número de telefono: "))

telefonos.update({nuevo: telefono})

print(telefonos)

# Modificar valores
telefonos["María"] = 1010

telefonos.update({"Ana": 2020})

# Eliminar clave valor: # del telefonos borra el diccionario
del telefonos["Ana"]

telefonos.pop("Paco")

# Metodo get
print(telefonos.get("Paco"))

print(telefonos.get("Antonio")) #Si no existe devuelve None
print(telefonos.get("Antonio", "Esa clave no existe."))

inventario = {
        "Tornillos": 100,
        "Tuercas": 150,
        "Arandelas": 250
}

articulo = input("Articulo: ")
numero = inventario.get(articulo, 0)
print("{}:{}".format(articulo, numero))