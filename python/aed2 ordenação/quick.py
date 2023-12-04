def hoare(lista,ini,fim):
    meio  = (ini+fim)//2
    pivo = lista[meio]

    i = ini
    j = fim

    while True:
        while lista[i]<pivo:
            i = i+1
        while lista[j]>pivo:
            j = j-1
        if i<j:
            lista[i],lista[j] = lista[j],lista[i]
        else:
            return j



def quick(lista,ini,fim):
    
    if ini<fim:
        pivo = hoare(lista,ini,fim)
        quick(lista,ini,pivo)
        quick(lista,pivo+1,fim)
    
     

lista = eval(input())

quick(lista,0,len(lista)-1)
print(lista)
