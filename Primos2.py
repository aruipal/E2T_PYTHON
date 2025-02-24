def es_primo(num):
    primos=[]
    for i in range(2,num):
        for j in range(2,i-1):
            if i % j == 0:
                break
        else:
            primos.append(i)
    print(primos)

num=int(input("Introduzca el número final: "))

es_primo(num)