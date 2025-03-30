agenda = {
    "Jorge": {
        "Telefono": 111111,
        "Pais": "España",
        "Personal": {
            "Aficion": "Futbol",
            "Estudios": "E2T",
            "Musica": "Pop"
        },
    },

    "Maria": {
        "Telefono": 222222,
        "Pais": "Italia",
        "Personal": {
            "Aficion": "Videojuegos",
            "Estudios": "Informatica",
            "Musica": "Rock"
        },
    },
    
    "Tomás": {
        "Telefono": 333333,
        "Pais": "Portugal",
        "Personal": {
            "Aficion": "Baloncesto",
            "Estudios": "Administrativo",
            "Musica": "Clasica"
        },
    },
}

# Comprobar si hay miembros de Italia y si le gusta la musica rock
for nombre, datos in agenda.items():
    if datos["Pais"] == "Italia" and datos["Personal"]["Musica"] == "Rock":
        print(nombre)

# Mostrar todos los miembros con su aficion
for nombre, datos in agenda.items():
    print("{}: {}".format(nombre, datos["Personal"]["Aficion"]))

# Mostrar todos los datos personales de cada miembro
for nombre, datos in agenda.items():
    print("Datos personales de {}".format(nombre))
    for categoria, informacion in datos["Personal"].items():
        print(" - {}: {}".format(categoria, informacion))

