def llenado(litros):
    capacidad_total = 1800
    velocidad_bomba = 1.5  # litros por segundo

    # Calculamos cuántos litros faltan para llenar el tanque (sin exceder por más de 1.5 litros)
    litros_faltantes = min(capacidad_total - litros, capacidad_total - 1.5 - litros)

    # Calculamos el tiempo en segundos que debe estar encendida la bomba
    tiempo_segundos = int(litros_faltantes / velocidad_bomba)

    return tiempo_segundos

# Pruebas con los valores solicitados
print(llenado(1648))  # Debe devolver el tiempo para llenar desde 1648 litros
print(llenado(1696))  # Debe devolver el tiempo para llenar desde 1696 litros
print(llenado(1780))  # Debe devolver el tiempo para llenar desde 1780 litros