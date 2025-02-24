# Realiza una función que compare dos listas y nos diga si son iguales
# Misma longitud y mismos elementos

# lista1=[[1,2,3,4,5,6],[1,2,3,4,5,6]] El indice 0 sería una lista y el 1 otra lista.

lista1= [1,2,3,4,5,6]
lista2= [1,2,3,4,5,6,7]

def longlista():
    if len(lista1)==len(lista2):
        print("Misma longitud.")
    else:
        print(f"La lista1 tiene {len(lista1)} elementos y la lista2 tiene {len(lista2)}.")


def elemlista():
    longlista()
    for i in range(len(lista1)):
        if lista1[i]==lista2[i]:
            continue
        else:
            return "No tienen mismos elementos."
    print(f"Coinciden en {i} elementos.")

elemlista()
        

