import time

def es_primo():
    num=int(input("Introduzca el número final: "))
    inicio=time.time()
    primos=[]
    for i in range(2,num+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primos.append(i)
    fin=time.time()
    print(primos)
    print(f"Ha tardado {round(fin-inicio,2)} segundos.")

es_primo()

