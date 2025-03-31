from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from bson.objectid import ObjectId # Id hash

app = Flask(__name__)

# Conectar con MongoDB
client = MongoClient("mongodb://admin:admin123@localhost:27017/?authSource=admin")
"""El usuario y password están en claro, deberían cifrarse. Se debería también crear
un usuario con permisos de escritura y lectura pero no de admin"""
# Crear base de datsos
db = client["Practica_flask"]

# Colección dentro de la base de datos
collection = db["personas"]

# Ruta principal: mostrar lista de paersonas y agregar nuevas
@app.route("/", methods=["GET","POST"]) # @ decorador en python con la ruta del index.html /. metodos: recibir y enviar datos
def index():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        #apellidos = request.form.get("apellidos")
        if nombre: #and apellidos:
            collection.insert_one({"nombre":nombre}), #"apellidos":apellidos})
    personas = list(collection.find()) # Obtenemos la lista de personas desde mongo
    return render_template("index.html", personas=personas)

# Ruta para eliminar una persona de la BD
@app.route("/delete/<id>")
def delete(id):
    collection.delete_one({"_id":ObjectId(id)})
    return redirect(url_for("index"))

# Ruta para editar una persona existente
@app.route("/edit/<id>", methods=["GET","POST"])
def edit(id):
    persona = collection.find_one({"_id":ObjectId(id)}) # Buscamos persona por ID
    if request.method == "POST":
        nuevo_nombre = request.form.get("nombre")
        # nuevos_apellidos = request.form.get("apellidos")
        collection.update_one({"_id":ObjectId(id)}, {"$set":{"nombre":nuevo_nombre}})
        return redirect(url_for("index"))
    return render_template("edit.html", persona=persona)

if __name__=="__main__":
    app.run(debug=True) # Iniciamos el servidor Flask