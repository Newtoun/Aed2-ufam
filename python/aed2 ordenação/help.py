def max_helpify(lista,raiz,tam):#aqui ta certo
    maior = raiz

    esquerda = 2*raiz+1
    if esquerda < tam and lista[esquerda] > lista[maior]:
        maior = esquerda
    
    direita = 2*raiz+2

    if direita < tam and lista[direita] > lista[maior]:
        maior = direita
    
    if maior != raiz:
        lista[maior] , lista[raiz] = lista[raiz] , lista[maior]
        lista = max_helpify(lista,maior,tam)
    

def montar_max_help(lista):
    N = len(lista)
    for i in range((N//2)-1,-1,-1):
        max_helpify(lista,i,N)

def helpsort(lista):
    tam_help = len(lista)-1
    montar_max_help(lista)

    for i in range(tam_help,0,-1):#ah
        lista[i],lista[0] = lista[0],lista[i]
        max_helpify(lista,0,i)


lista = eval(input())
while lista!=[]:

    helpsort(lista)
    print(lista)
    lista = eval(input())

