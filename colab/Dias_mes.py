def bisiesto(año):
    if año % 4 != 0:
        return False
    elif año % 4 == 0 and año % 100 != 0:
        return True
    elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
        return False
    elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
        return True


def obtener_dias_del_mes(mes, año):
    # Abril, junio, septiembre y noviembre tienen 30
    if mes in [4, 6, 9, 11]:
        return 30
    # Febrero depende de si es o no bisiesto
    if mes == 2:
        if bisiesto(año):
            return 29
        else:
            return 28
    else:
        # En caso contrario, tiene 31 días
        return 31
# Probamos
año = int(input("Ingrese un año: "))
mes = int(input("Ingrese el número del mes: "))
dia = int(input("Ingrese un día: "))
total_dias = obtener_dias_del_mes(mes, año)
print("El mes tiene", total_dias, "días.")

def obtener_dia_del_año(año, mes, dia):
  
    if año < 1582 or mes > 12 or dia < 1:
        return None
    if dia > obtener_dias_del_mes(año, mes) or dia < 1:
        return None
    Dias_totales = dia
    mes = mes -1
    while mes > 0:
        Dias_totales += obtener_dias_del_mes(mes, año)
        mes -= 1
    # return Dias_totales
    print("Es el día", Dias_totales, "del año.")

obtener_dia_del_año(año, mes, dia)