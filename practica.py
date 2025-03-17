import pymongo

# Nos devuelve la version de pymongo instalada con pip install pymongo:
# print(pymongo.__version__) 

# Conectar a la BD local:
cliente = pymongo.MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")

# Para que la conexión se cierre:
# cliente.close()

# Listar bases de datos
dbs = cliente.list_database_names()
print("Bases de datos disponibles: ", dbs)

# Crear una base de datos, si no la hay, la crea
db = cliente["practica_7"]
# Crear colección, si no la hay, la crea
productos = db["productos"]

'''numero_productos = int(input("Introduzca el número de productos a meter: "))
numero_productos_metidos = 0
while numero_productos_metidos < numero_productos:
    nombre = input("nombre: ")
    precio = input("precio: ")
    stock = input("stock: ")
    
    producto = {"nombre": nombre, "precio": precio, "stock": stock}
    productos.insert_one(producto)
    numero_productos_metidos += 1'''
    
# Insertar un documento
# producto1 = {"nombre": "Laptop", "precio": 1200, "stock": 5}
# productos.insert_one(producto1)

# Consultar
productos2 = productos.find()

for producto in productos2:
    print(producto)

for i in productos2:
    print(i)
# Consultar por clave:valor    
productos3 = productos.find_one({"nombre":"ratón"})
print(productos3)

# Actualizar documento
productos.update_one({"nombre":"ratón"},{"$set":{"precio":15}})    

# Eliminar un documento    
productos.delete_one({"nombre": "Tablet"})