def leComando():
	caso = input()
	return caso[0], int(caso[1:])

def espalhamento_h(k, m, A):
	return int(m*((k*A)-int(k*A)))

def espalhamento_hLinha(h, m, i):
	return int((h + (i*i))%m)
	

def inserir(k, m, A, vetor):
	h =  espalhamento_h(k, m, A)
	index = h
	volta = 0
	i = 1
	while (vetor[index][0] != None):
		index = espalhamento_hLinha(h, m, i)
		i += 1
		volta += 1
	
	vetor[index] = (k, True)
	print("Chave {} inserida no indice {}".format(k, index))

def remover(k, m, A, vetor):
	index = procurar(k, m, A, vetor)
	if index >= 0:
		vetor[index] = (None, True)
		print("Chave {} removida".format(k))
	return vetor

def procurar(k, m, A, vetor):
	h =  espalhamento_h(k, m, A)
	index = h
	volta = 0
	i = 1
	while  volta < m and vetor[index][1] != False:
		if vetor[index][0] == k:
			return index 
		index = espalhamento_hLinha(h, m, i)
		i += 1
		volta += 1
	return -1
	
tam = int(input())
vetor = [(None, False)]*tam
A = float(input())
comando, numero = leComando()
while comando != 'x':
	if comando == 'i': #inserir
		inserir(numero, tam, A, vetor)
	elif comando == 'r': #remover
		remover(numero, tam, A, vetor)
	elif comando == 'p': #procurar
		resposta = procurar(numero, tam, A, vetor)
		if resposta >= 0:
			print("Chave {} encontrada no indice {}".format(numero, resposta))
		else:
			print("Chave {} nao esta na tabela".format(numero))
	comando, numero = leComando()