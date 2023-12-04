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


def imprime_arvore(arvore, indent=0):
    #"""Imprime a árvore na forma de um dicionário indentado."""
    prefixo = ' ' * indent

    print("{ 'valor': ", arvore['valor'], ",", sep='')

    if arvore['esq'] is None:
        print(prefixo, "  'esq': None,", sep='')
    else:
        print(prefixo, "  'esq': ", sep='', end='')
        imprime_arvore(arvore['esq'], indent + 9)

    if arvore['dir'] is None:
        print(prefixo, "  'dir': None,", sep='')
    else:
        print(prefixo, "  'dir': ", sep='', end='')
        imprime_arvore(arvore['dir'], indent + 9)

    print(prefixo, "},", sep='')



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
    
    imprime_arvore(arvore)
    caso = eval(input())
