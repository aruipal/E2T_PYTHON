import random



aleatorio = random.randint(1,100)
numero = int(input("Introduce numero: "))

      
while numero != aleatorio:
           
    if numero > aleatorio:
        print("Más bajo")
        
    else:
        print("Más alto")
    
    numero = int(input("Introduce otro numero: "))

print(f"Acertaste {aleatorio}")