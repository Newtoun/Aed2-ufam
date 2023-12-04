import numpy as np
import random

class Processo(object):
    def __init__(self, pnome, pio, ptam, prioridade, tempoChegada):
        self.nome = pnome
        self.io = pio # Probabilidade de fazer E/S, inicialmente zero
        self.tam = ptam # Quantos Timeslices são necessários para terminar
        self.prio = prioridade # Prioridade, agora usada para definir o número de bilhetes
        self.chegada = tempoChegada
        self.bilhetes = self.prio # Número de bilhetes atribuído à prioridade do processo
        
    def roda(self, quantum=None):
        if(random.randint(1,100) < self.io):
            self.tam -= 1
            print(self.nome, "fez E/S, faltam", self.tam)
            return 1, True # Retorna True se o processo fez E/S
            
        if quantum is None or self.tam < quantum:
            quantum = self.tam
        self.tam -= quantum
        print(self.nome, "rodou por", quantum, "timeslice, faltam", self.tam)
        return quantum, False # Retorna False se o processo não fez E/S
    
class EscalonadorLoteria(object):
    def __init__(self, vprontos=[]):
        self.prontos = vprontos
        
    def pronto(self, processo):
        self.prontos.append(processo)
        
    def proximo(self):
        bilhetes_totais = sum([p.bilhetes for p in self.prontos])
        if bilhetes_totais == 0:
            return None # Se não há processos prontos, retorna None
        
        bilhete_sorteado = random.randint(1, bilhetes_totais)
        for processo in self.prontos:
            if bilhete_sorteado <= processo.bilhetes:
                return processo # Retorna o processo que teve seu bilhete sorteado
            bilhete_sorteado -= processo.bilhetes
            
        return None # Isso nunca deveria acontecer, mas se chegar aqui, retorna None

nprocs = 4
nomes = ['A', 'B', 'C', 'D']
chanceio = [0, 0, 0, 0]
tamanho = np.array([3, 3, 3, 3])
prioridades = [1, 2, 3, 4] # Prioridades dos processos

total = tamanho.sum()

procs = []
for i in range(nprocs):
    procs.append(Processo(nomes[i], chanceio[i], tamanho[i], prioridades[i], 0))

quantum = 2
tempoBloq = 1

escalonador = EscalonadorLoteria(procs)
bloqueados = []

tempo = 0
random.seed(0)

while total > 0:
    p = escalonador.proximo()
    if p is not None:
        rodou, _ = p.roda(quantum)
        
        if p.tam > 0:
            escalonador.pronto(p)
        total -= rodou
        tempo += rodou
    else:
        tempo += 1
