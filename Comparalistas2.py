lista1= [1,2,3,4,5,6]
lista2= [1,2,3,4,5,6,7]

def comparador(l1, l2):
    if len(l1) != len(l2):
        return "Son diferentes en longitud."
    else:
        for indice in range(len(l1)):
            if l1[indice] != l2[indice]:
                return "Son diferentes en elementos."
        return "Son iguales"
    
print(comparador(lista1,lista2))