import numpy as np
import random

import numpy as np
import random

class Processo(object):
    def __init__(self, pnome, pio, ptam, prioridade, tempoChegada, bilhetes=100):
        self.nome = pnome
        self.io = pio # Probabilidade de fazer E/S, inicialmente zero
        self.tam = ptam # Quantos Timeslices sao necessarios para terminar
        self.prio = prioridade # Prioridade, eh desnecessaria agora 
        self.chegada = 0
        self.bilhetes  = bilhetes
        
    def roda(self, quantum=None): # se rodar sem quantum, o processor roda ate o fim
        if(random.randint(1, 100) < self.io): #Verifica se fez E/S
            self.tam -= 1
            print(self.nome, "fez e/s, falta", self.tam)
            return 1, True #True que fez E/S
            
            
        if(quantum is None or self.tam < quantum):
            quantum = self.tam
        self.tam -= quantum
        print(self.nome, "rodou por", quantum, "timeslice, faltam", self.tam)
        return quantum, False # False se nao fez E/S


class Stride(object):
    def __init__(self, vprontos=[], quantum=2):
        self.prontos = vprontos #processos que cheam ao tempo zero
        self.quantum = quantum
        self.tempo = 0
        self.passos = {p.nome: 0 for p in self.prontos}
        self.bilhetes = {p.nome: self.calcular_bilhetes(p) for p in self.prontos}
        
    def calcular_bilhetes(self, processo):
        return int((1 / processo.tam) * 10000)
    
    def pronto(self, processo):
        self.prontos.append(processo)
        self.passos[processo.nome] = 0
        self.bilhetes[processo.nome] = self.calcular_bilhetes(processo)
        
    def sortear(self):
        sorteado = None
        maior_passo = -1
        
        for processo in self.prontos:
            passo_atual = self.passos[processo.nome]
            if passo_atual > maior_passo:
                maior_passo = passo_atual
                sorteado = processo
                
        return sorteado
    
    def proximo(self):
        if len(self.prontos) == 0:
            return None
        
        sorteado = self.sortear()
        if sorteado is None:
            return None
        
        self.passos[sorteado.nome] += sorteado.tam
        sorteado.bilhetes += self.calcular_bilhetes(sorteado)
        return sorteado
    
    def rodar(self, processo):
        rodou, _ = processo.roda(self.quantum)
        self.tempo += rodou
        
        if processo.tam == 0:
            self.prontos.remove(processo)
            del self.passos[processo.nome]
            del self.bilhetes[processo.nome]
        
        if rodou < self.quantum and processo.tam > 0:
            return True
        
        return False


nprocs = 4
nomes = ['A','B','C','D']
chanceio = [0,0,0,0] #Valor de zero a cem, chance de ser entrada e saida por enquanto deixem em zero
tamanho = np.array([10,20,30,40])


total = tamanho.sum()

procs = []
for i in range(nprocs):
    procs.append(Processo(nomes[i],chanceio[i],tamanho[i],0,0,100)) #cria uma lista procs de Processos

quantum = 2
tempoBloq = 1

escalonador = Stride(procs) #troque escalonador pelo seu escalonador
bloqueados = []

tempo = 0

random.seed(0)

while total>0:
    p = escalonador.proximo()
    if(p is not None):
        rodou, _ = p.roda() #adicione quantum como parâmetro, por enquanto nao temos E/S
        
        if(p.tam>0):
            escalonador.pronto(p)
        total-=rodou
        tempo+=rodou
    else:
        #Reduz o tempo de todos os bloqueados em uma unidade se nao havia ninguem pronto
        tempo+=1


    