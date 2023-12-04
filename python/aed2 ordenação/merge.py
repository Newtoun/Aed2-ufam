def merge_sort(lista,inicio,fim,d=0):

    if inicio>=fim:
        return
    
    meio = (inicio+fim)//2
    merge_sort(lista,inicio,meio,d+1)
    merge_sort(lista,meio + 1,fim,d+1)

    tamanho = fim - inicio+1
    res = [0] * tamanho

    i = inicio
    j = meio+1

    for k in range(tamanho):# intercala
        if (j <= fim) and (i> meio or lista[j] <lista[i]):
            res[k] = lista[j]
            j+=1
        else:
            res[k] = lista[i]
            i+=1


    for i in range(tamanho):
        lista[inicio+i] = res[i]


lista = eval(input())

merge_sort(lista,0,len(lista)-1)
print(lista)