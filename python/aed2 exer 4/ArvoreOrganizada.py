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



def bala(lista,inicio,fim,arvore):
    meio  = (fim+inicio)//2

    if(inicio<=fim):
        valor = lista[meio]
        arvore = insere(arvore,valor)
        bala(lista,inicio,meio-1,arvore)
        bala(lista,meio+1,fim,arvore)
        return arvore
        #arvore['esq']=bala(lista,inicio,meio-1,arvore['esq'])
        #arvore['dir']=bala(lista,meio+1,fim,arvore['dir'])
 
    #arvore = cria_no(lista[fim+inicio//2])
    
    return arvore
    


# Lê o primeiro caso de teste
caso = eval(input())


 #Itera até o último caso


lista=[]
listaNova=[]
arvore = cria_arvore()
for i in range(0,len(caso)):
    arvore = insere(arvore,caso[i])
    
emOrdem(arvore,lista)
tam = len(lista)

arvore_nova = cria_arvore()
arvore_nova= bala(lista,0,tam-1,arvore_nova)

#print(lista)
print("pre: ",end='')
preOrdem(arvore_nova)
print()
print("pos: ",end='')
posOrdem(arvore_nova)

