import time as t
#t.sleep(1)
registrados = []

def aumentar_chave(heap, pos, novo):
	tam = len(heap)
	if pos == tam:
		heap.append(novo)
	else:
		heap[pos] = novo
	pai = (pos-1)//2
	while (pos>0) and (heap[pos]<(heap[pai])):
		heap[pai], heap[pos]= heap[pos], heap[pai]
		pos=pai
		pai=(pos-1)//2
	return heap

def valorRoda(config, roda):
	return (config // 10 ** (4 - roda)) % 10

def gira(config, roda, sentido):
	peso = 10 ** (4 - roda)
	
	digitoAtual = (config // peso) % 10

	if sentido == 'a':
		proximoDigito = (digitoAtual + 9) % 10
	else:
		proximoDigito = (digitoAtual + 1) % 10

	subtrair = digitoAtual * peso
	somar = proximoDigito * peso

	return config - subtrair + somar

class Estado:
	def __init__(self, numero, proibidos, passos):
		# Guarda a configuração atual e a coleção de
		# estados proibidos
		self.numero = numero
		self.proibidos = proibidos

		# Calcule f, g e h
		self.g = passos
		self.h = heuristica(self.numero) # Deve calcular a heurística aqui
		self.f = self.g + self.h

	def transicoes(self):
		# Complete-me
		transicoes = []
		for roda in range(1,5):
			prox_num=gira(self.numero, roda, "a")
			if (prox_num not in self.proibidos) and (prox_num not in registrados):
				transicoes.append(Estado(prox_num, self.proibidos,self.g+1 ))
		for roda in range(1,5):
			prox_num=gira(self.numero, roda, "h")
			if (prox_num not in self.proibidos) and (prox_num not in registrados):
				transicoes.append(Estado(prox_num, self.proibidos,self.g+1 ))
		return transicoes
		#saida = []  # Deve retornar os estados alcançáveis 

	def __lt__(self, other):
		# Complete-me
		return self.f<other.f # Deve comparar aqui

	def __repr__(self):
		return "{:04d}".format(self.numero)
	
def heuristica(numero):
	a, b, c, d= valorRoda(numero, 1), valorRoda(numero, 2), valorRoda(numero, 3), valorRoda(numero, 4)
	lista=[a,b,c,d]
	helristica=0
	for i in lista:
		if i >=5:
			i = 10 - i
		helristica+=i
	return helristica

def minpassos(estado):
	if estado.numero == 0:
		return estado.g
	else:
		registrados.append(estado.numero)
		lista = estado.transicoes()
		print(lista)
		heap = []
		for i in lista:
			tam = len(heap)
			heap = aumentar_chave(heap, tam, i)
		print(heap)
		novo_estado = heap[0]
		return minpassos(novo_estado)

config_inicial = eval(input())
proibidos= eval(input())
while config_inicial != -1:
	registrados = []
	estado_inicial=Estado(config_inicial, proibidos, 0)
	passos=minpassos(estado_inicial)
	print(passos)
	config_inicial = eval(input())
	proibidos= eval(input())