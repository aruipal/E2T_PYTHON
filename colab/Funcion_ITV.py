def message(marca, number):
  print("La marca de su coche es", marca+", " "y esta matriculado en el año", number)
  año = 2025 - number
  print("Su coche tiene:", año, "años")
  if año >= 0 and año <= 4:
    print("La primera ITV es en:", number + 4)
  elif año > 4 and año < 10:
    print("Tiene que pasar la ITV cada dos años")
  else:
    print("Tiene que pasar la ITV cada año")

message("Fiat", 2016)