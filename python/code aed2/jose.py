import time as t 
lista_registrados = []

def min_heapify(lista, i, tam):
 
 min = i
 
 filho_esquerdo = 2 * i + 1
 if filho_esquerdo < tam and lista[filho_esquerdo] < lista[min]:
  min = filho_esquerdo
  
 filho_direito = 2 * i + 2
 if filho_direito < tam and lista[filho_direito] < lista[min]:
  min = filho_direito
 
 if min != i:
  lista[i], lista[min] = lista[min], lista[i]
  min_heapify(lista, min, tam)

 return lista

def insere_chave(heap, tam, chave):
 
 heap.append(None)
 
 heap[tam] = chave
 
 heap = aumentar_chave(heap, tam, chave)
 
 return heap

def aumentar_chave(heap, pos, novo):
 
 heap[pos] = novo
 pai = (pos - 1) // 2
 
 while pos > 0 and heap[pai] > novo:
  
  heap[pai], heap[pos] = heap[pos], heap[pai]
  pos = pai
  pai = (pos - 1) // 2

 return heap

def calcula_heuristica(config):
 
 passo = 0
 
 for j in range(1,5):
  
  numero = valorRoda(config, j)
  
  if numero > 5: 
   passo += (10 - numero)
  else:
   passo += numero
   
 return passo

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
 def init(self, numero, proibidos, passos):
  
  self.numero = numero
  self.proibidos = proibidos
  self.g = passos
  self.h = calcula_heuristica(self.numero)
  self.f = self.g + self.h

 def transicoes(self):
  
  valor_h = None
  valor_a = None
  saida = []
  
  for j in range(1,5):
   
   valor_h = gira(self.numero, j, 'a')
   
   if valor_h not in self.proibidos and valor_h not in lista_registrados:
    saida.append(Estado(valor_h, self.proibidos, self.g + 1))
    
  for j in range(1, 5):
   
   valor_a = gira(self.numero, j, 'h')
   
   if valor_a not in self.proibidos and valor_a not in lista_registrados:
    saida.append(Estado(valor_h, self.proibidos, self.g + 1))
   
   
  return saida

 def lt(self, other):
  # Complete-me
  return self.f < other.f # Deve comparar aqui

 def repr(self):
  return "{:04d}".format(self.numero)

 
def menor_passo(classe):
 
 print(lista_registrados)
 
 if classe.numero == 0:
  return classe.g
 else:
  lista_aprovados = classe.transicoes()
  lista_registrados.append(classe.numero)
  heap = []
  for i in lista_aprovados:
   heap = insere_chave(heap, len(heap), i)
  elemento = heap[0]
  return menor_passo(elemento)
 
numero = int(input())

while numero != -1:
 
 lista_proibidos = eval(input())
 primeiro_elemento = Estado(numero, lista_proibidos, 0)
 
 print(menor_passo(primeiro_elemento))
 t.sleep(1)
 
 numero = int(input())