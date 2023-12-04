import math
def leComando(entrada):
	return entrada[0], int(entrada[1:])

def insere(tabela,k,num):
    N = len(tabela)#tamanho
    i = 0
    pos = int(N * (num*k  - (int(num*k) ) ) )

    posicao = pos
    while tabela[posicao][1] != "apagada"  and tabela[posicao][1] != "livre":
        i+=1    
        posicao = (pos + (i*i))%N

    tabela[posicao] = (num,"ocupado")
    print("Chave {} inserida no indice {}".format(num,posicao))

def apaga(tabela,k,num):
    N = len(tabela)#tamanho
    i = 0
    pos = int(N * (num*k  - (int(num*k) ) ) )
    posicao = pos
    while (tabela[posicao][1] == "ocupado" or tabela[posicao][1] == "apagada") and tabela[posicao][0]!=num:
        i+=1
        posicao = (pos + i*i)%N
    if tabela[posicao][1] == "livre" or tabela[posicao][0]!=num:
        print("Chave {} nao esta na tabela".format(num))
    else:
         print("Chave {} removida".format(num))
         tabela[posicao] = (None,"apagada")

def procura(tabela,k,num):
    N = len(tabela)#tamanho
    i = 0
    pos = int(N * (num*k  - (int(num*k) ) ) )

    posicao = pos
    while (tabela[posicao][1] == "ocupado" or tabela[posicao][1] == "apagada") and tabela[posicao][0]!=num:
        i+=1
        posicao = (pos + i*i)%N
    if tabela[posicao][0]==num:
         print("Chave {} encontrada no indice {}".format(num,posicao))
    else:
         print("Chave {} nao esta na tabela".format(num))
     

tamanhoT = int(input())
k = float(input())
vet = [(None,"livre")] * tamanhoT

entrada = input()

while entrada[0] != "x":
    comando,chave = leComando(entrada)
    if comando=="i":
         insere(vet,k,chave)
    elif comando=="r":
         apaga(vet,k,chave)
    else:
         procura(vet,k,chave)

    entrada = input()
