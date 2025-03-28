x = 1
try:
    print(str(x))
  
except NameError:
    print("No existe el nombre")
  
except SyntaxError:
    print("Error de sintaxis")
    
except ValueError:
    print("Algo no fue bien")
    
# finally: se ejecutará Independientemente de si el bloque try genera un error o no. 
finally:
  print("Terminaron las excepciones")
  
# raise: define el tipo de error que se va a generar y el texto que se va a imprimir para el usuario.
a = "cadena"
if not type(a) is int:
  raise TypeError("Solo números enteros están permitidos.")

x = -1
if x < 0:
  raise Exception("Solo números positivos")