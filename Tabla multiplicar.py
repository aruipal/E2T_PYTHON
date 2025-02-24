#Tabla de multiplicar del 1 al 10 de un número dado.

def tabla(num):
    print(f"Tabla del {num}:")
    for i in range(1,11):
        print(f"{num}x{i}={num*i}") #print(num + "x" + i + "=" + (num*i))

numero_usuario=int(input("Introduzca un número: "))

tabla(numero_usuario)

    
