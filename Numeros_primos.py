# Imprimir lista de primos del 1 al 100.

def es_primo(num):
    if num < 2:
        return False
    else:
        for i in range(2, int(num-1)):
            if num % i == 0:
                return False
        return True
            
def lista_primos():
    primos=[]
    for i in range(2,101):
        if es_primo(i):
            primos.append(i)
    return primos

print(lista_primos())