class Pilha:
    def __init__(self):
        self.pilha=[]

    def insere(self,num):
        self.pilha +=[num]
    
    def tira(self):
        if self.vazia() == False :
            self.pilha.pop()
    
    def vazia(self):
        return self.pilha == []


    def topo(self):
        if  not self.vazia():
            return self.pilha[-1]
        return None


def Verifica(pilha, lista):
    
    for i in range( len(lista)):
        if lista[i] == ')' and pilha.topo()== '(' :
            pilha.tira()
        elif lista[i] == ']' and pilha.topo()== '[':
            pilha.tira()          
        elif lista[i] == '}' and pilha.topo()== '{':
            pilha.tira()
        else:
            pilha.insere(lista[i])
        


pilha = Pilha()

ler  = str(input())
Verifica(pilha,ler)

if pilha.vazia():
    print('sim')
else:
    print('nao')


