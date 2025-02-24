lista1= [1,2,3,4,5,6]
lista2= [1,2,3,4,5,6]
lista3= ["patata",2,3,4,5,6]
lista_a=[]

while True:
    x = int(input("Introduzca dato (para salir escriba -12345): "))
    if x != -12345:
        lista_a.append(x)
    else:
        break

def comparador(l1, l2, l3):
    if len(l1) != len(l2) or len(l2) != len(l3):
        return "Son diferentes en longitud."
    else:
        for indice in range(len(l1)):
            if l1[indice] != l2[indice] or l2[indice] != l3[indice]:
                return "Son diferentes en elementos."
        return "Son iguales"
    
print(comparador(lista1,lista2,lista_a))