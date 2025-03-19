'''sueldos=[]
for x in range(5):
    valor=int(input("Ingrese sueldo:"))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for k in range(4):
    for x in range(4):
        if sueldos[x]>sueldos[x+1]:
            aux=sueldos[x]
            sueldos[x]=sueldos[x+1]
            sueldos[x+1]=aux

print("Lista con el último elemento ordenado")
print(sueldos)'''

lista = [10,5,6,3,12]
print(lista)
for i in range(len(lista)-1):
    for j in range(len(lista)-1):
        if lista[j] > lista[j+1]:
            num = lista[j]
            lista[j] = lista[j+1]
            lista[j+1] = num
print(lista)
         

