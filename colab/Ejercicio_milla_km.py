def convertidor():
    milla = float(input("Introduce las millas a convertir: "))
    km = round(milla * 1.61, 2)
    print (f"{milla} millas son: {km} kilometros")
    
convertidor()