
lista = [8,7,6,5,4,3,2,1]#8
n=8

for i in range(1,n):
    pivo = lista[i]
    j = i-1

    while j>=0 and pivo<lista[j]:
        lista[j+1] = lista[j]
        j -=1

    lista [j+1] = pivo


print (lista)