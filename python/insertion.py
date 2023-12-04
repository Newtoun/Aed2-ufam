lista = [8,7,6,5,4,3,2,1]#8
n=8

for i in range(1,n):
    pivor = lista[i]#8
    j = i-1#0

    while j>=0 and pivor<lista[j]:#
        lista[j+1] = lista[j]#
        j=j-1#
        print(lista)#


    print(lista)#
    lista[j+1] = pivor#


print(lista)