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

def preOrdem(arvore):
   
    print(arvore['valor'], end=' ')
    
    if arvore['esq'] is not None:
        preOrdem(arvore['esq'])
    

    if arvore['dir'] is not None:
        preOrdem(arvore['dir'])
    
    
def emOrdem(arvore):
   
    
    
    if arvore['esq'] is not None:
        emOrdem(arvore['esq'])  
    print(arvore['valor'], end=' ')

    if arvore['dir'] is not None:
        emOrdem(arvore['dir'])

def posOrdem(arvore):   
    if arvore['esq'] is not None:
        posOrdem(arvore['esq'])
    

    if arvore['dir'] is not None:
        posOrdem(arvore['dir'])
    
    print(arvore['valor'], end=' ')






# Lê o primeiro caso de teste
caso = eval(input())


 #Itera até o último caso
num=0
while caso != []:
    num+=1
    print("arvore {}".format(num))
    arvore = cria_arvore()
    for i in range(0,len(caso)):
        arvore = insere(arvore,caso[i])

    print("Pre-ordem:",end=' ')
    preOrdem(arvore)
    print()
    print("In-ordem:",end=' ')
    emOrdem(arvore)
    print()
    print("Pos-ordem:",end=' ')
    posOrdem(arvore)
    print()
    print()

    caso = eval(input())
