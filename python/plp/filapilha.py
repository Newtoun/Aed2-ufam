import sys
class Lista:
    def __init__(self):
        self._lista = []

    def _inserir_inicio(self, num):
        return self._lista.insert(0 ,num)
    
    def _inserir_fim(self, num):
        return self._lista.append(num)
    
    def _remover_ini(self):
        return self._lista.pop(0)
    
    def _remover_fim(self):
        return self._lista.pop()
    
    def vazia(self):
        return self._lista == []
    
    def valor_pilha(self):
        return self._lista[-1]
    
    def valor_fila(self):
        return self._lista[0]
    
class Pilha(Lista):

    def insere(self , num):
        self._inserir_fim(num)

    def retira(self):
        self._remover_fim()

    def valor(self):
        return self.valor_pilha()

class Fila(Lista):
    def insere(self , num):

        self._inserir_fim(num)

    def retira(self):
        self._remover_ini()

    def valor(self):
        return self.valor_fila()

pi = Pilha()
fi = Fila()

entrada = []
for line in sys.stdin:
    entrada.append(line.strip())

for i in range(len(entrada)):
    if int(entrada[i])%2==0:
        pi.insere(int(entrada[i]))
    else:
         fi.insere(int(entrada[i]))

while not pi.vazia():
    print(pi.valor())
    pi.retira()

while not fi.vazia():
    print(fi.valor())
    fi.retira()
