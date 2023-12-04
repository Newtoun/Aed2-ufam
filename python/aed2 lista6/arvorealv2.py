#calcula a altura recursivamente iniciando as folhas com 1 e somando um com o filho maior para o pai
#altura recursiva incrementa e volta calculando a altura do maior filho atualiza +1
#depois atualiza altura dos filhos primeiro e dps do pai
# rotacao simples raiz+2 e filho direito +1 ou 0
# raiz -2,filho esquerdo -1 ou 0 simples
#raiz +2 e filho direito -1 rota dupla

def insere_com_altura(arvore,valor):
    if arvore is None: #recusao que insere elementos
        arvore = cria_no(valor)
    elif arvore['valor']<valor and arvore['valor'] is not None:
        arvore['dir'] = insere_com_altura(arvore['dir'],valor)
    else:
        arvore['esq'] = insere_com_altura(arvore['esq'],valor)

    if arvore['esq'] is None and arvore['dir'] is None:#caso de parada caso seja folha
        return arvore

    if arvore['esq'] is None or arvore['dir'] is None:#volta a recursao atualizando a altura
        if arvore['esq'] is None: # caso a arvore só tenha um filho
            arvore['alt'] = arvore['dir']['alt']+1
            arvore['fb'] = arvore['dir']['alt']
        elif arvore['dir'] is None:
            arvore['alt'] = arvore['esq']['alt'] + 1
            arvore['fb'] =  - arvore['esq']['alt']
    elif arvore['esq']['alt']>arvore['dir']['alt']:#caso que o filho esq é maior que o dir 9 + 13 + 8
        arvore['alt'] = arvore['esq']['alt'] + 1
        arvore['fb'] = arvore['dir']['alt']  - arvore['esq']['alt']
    else:
        arvore['alt'] = arvore['dir']['alt'] + 1# caso que o filho dir é maior que o esq
        arvore['fb'] = arvore['dir']['alt']  - arvore['esq']['alt']

    return arvore

def atualizaAltura(T):
    if T['esq'] is None and T['dir'] is None:#caso de parada caso seja folha
        T['alt'] = 1
        T['fb'] = 0
        return T
    
    if T['esq'] is None or T['dir'] is None:
        if T['esq'] is None:
            T['alt'] = T['dir']['alt'] + 1
            T['fb'] = T['dir']['alt']
        elif T['dir'] is None:
            T['alt'] =  T['esq']['alt'] + 1
            T['fb'] = -T['esq']['alt']

    elif T['esq']['alt']>T['dir']['alt']:#caso que o filho esq é maior que o dir
        T['alt'] = T['esq']['alt'] + 1
        T['fb'] = T['dir']['alt']  - T['esq']['alt']
    else:
        T['alt'] = T['dir']['alt'] + 1# caso que o filho dir é maior que o esq
        T['fb'] = T['dir']['alt']  - T['esq']['alt']
    
    return T



    
    

def cria_arvore():
   
    return None


def cria_no(valor):
    arvore = dict()
    arvore = {'valor': valor, 'esq': None, 'dir': None,'alt': 1,'fb':0}
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

    aux  =T['dir']
    T['dir'] = atualizaAltura(T['dir'])
    T = atualizaAltura(T)

    
    
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
	
#atualizar as alturas em arvores separadas enquanto fco as modificaçoes de conexao de arvore 
#ao fazer a recursao que calcula o cofador de sub arvore eu preciso desconectar as subarvores para depois juntalar com suas informaçoes
def altura(T):
	if T['dir'] is not None:
		T['dir'] = altura(T['dir'])#recu para dir
		
	if T['esq'] is not None: # terceiro caso em caso seja none pode dar erro
		T['esq'] = altura(T['esq'])#recu para esq
		
	if T['esq'] is None and T['dir'] is None: #caso de parada
		return T
	
	
	if T['esq'] is None or T['dir'] is None:
		if T['esq'] is None:#caso tenha filho para esq
			T['alt'] = T['dir']['alt'] + 1
		elif T['dir'] is None:#caso que so tem filho para dir
			T['alt'] = T['esq']['alt'] + 1
			
	elif T['esq']['alt']>T['dir']['alt']:#caso de comparacao
		T['alt'] = T['esq']['alt'] + 1
	else:#pode dar erro aqui
		T['alt'] = T['dir']['alt'] + 1
	 
	return T
	
lista = eval(input())
cont = 1
while lista!=[]:

    arvore = cria_arvore()

    for i in range(len(lista)):
        arvore = insere_com_altura(arvore,lista[i])
    
    #arvore = altura(arvore)
    
    
    arvore = rotacaoLL(arvore)
   
    print("Arvore {}".format(cont))
    print("h: {}".format(arvore['alt']))
    print("fb: {}".format(arvore['fb']))
    print("pre:",end=" ")
    preOrdem(arvore)
    print()
    print("pos:",end=" ")
    posOrdem(arvore)
    print(end="\n\n")
    cont+=1
    lista = eval(input())



	