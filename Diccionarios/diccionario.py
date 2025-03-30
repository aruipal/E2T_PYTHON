
diccionario = {}

diccionario["clave"] = { # un diccionario dentro de un diccionario
    "valor_key":"valor",
    "valor_k2":"valor2"
}

print(diccionario)
# Diccionarios anidados
paises = {
    "Perú": {
        "nombre": "República del Perú",
        "código": "PE",
        "is_mercosur": True
    },
    "Argentina": {
        "nombre": "República Argentina",
        "código": "AR",
        "is_mercosur": True
    },
    "Colombia": {
        "nombre": "República de Colombia",
        "código": "CO",
        "is_mercosur": True
    }
}

print(paises.get("Perú"))
print(paises.get("Perú").get("código"))

print(paises["Perú"])
# Crear otra clave y añadirla a paises
ecuador = {
    "name": "República del Ecuador",
    "código": "EC",
    "is_mercosur": True
}
paises["Ecuador"] = ecuador

print(paises)
print(paises.get("Ecuador"))