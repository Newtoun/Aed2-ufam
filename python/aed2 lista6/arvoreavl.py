def insere(arvore, valor):
    # complete o código
    if arvore is None:
        return cria_no(valor)
    elif arvore['valor']<valor and arvore['valor'] is not None:
        arvore['dir'] = insere(arvore['dir'],valor)
        return arvore
    else:
        arvore['esq'] = insere(arvore['esq'],valor)
        return arvore

def cria_arvore():
   
    return None


def cria_no(valor):
    arvore = dict()
    arvore = {'valor': valor, 'esq': None, 'dir': None}
    return arvore

def rotacaoRR(T):
    aux = T
    res = T['dir']['esq']

    T = T['dir']

    T['esq'] = aux

    T['esq']['dir'] = res
    return T

def rotacaoLL(T):
    aux = T
    res = T['esq']['dir']
    T = T['esq']
    T['dir'] = aux
    T['dir']['esq'] = res

    return T

def preOrdem(arvore):
   
    print(arvore['valor'], end=' ')
    
    if arvore['esq'] is not None:
        preOrdem(arvore['esq'])
    

    if arvore['dir'] is not None:
        preOrdem(arvore['dir'])
    
    
def emOrdem(arvore,lista):

    if arvore['esq'] is not None:
        emOrdem(arvore['esq'],lista)

    lista.append(arvore['valor'])

    if arvore['dir'] is not None:
        emOrdem(arvore['dir'],lista)

def posOrdem(arvore):   
    if arvore['esq'] is not None:
        posOrdem(arvore['esq'])
    

    if arvore['dir'] is not None:
        posOrdem(arvore['dir'])
    
    print(arvore['valor'], end=' ')




lista = eval(input())
cont = 1
while lista!=[]:
    arvore = cria_arvore()

    for i in range(len(lista)):
        arvore = insere(arvore,lista[i])

    arvore = rotacaoLL(arvore)
    print("arvore {}".format(cont))
    print("pre:",end=" ")
    preOrdem(arvore)
    print()
    print("pos:",end=" ")
    posOrdem(arvore)
    print(end="\n\n")
    cont+=1
    lista = eval(input())



	