class Time:

    def __init__(self,nome,numVitorias=0,numEmpate=0,numDerrota=0,golsPositivo=0,golsNegativo=0):
        self.nome = nome
        self.numVitorias = numVitorias
        self.numEmpate = numEmpate
        self.numDerrota=numDerrota
        self.golsPositivo = golsPositivo
        self.golsNegativo = golsNegativo
        self.pontosTime = (self.numVitorias*3) + self.numEmpate
        self.partidasJogadas = self.numVitorias+self.numDerrota+self.numEmpate
        self.diferencaGols = self.golsPositivo-self.golsNegativo
        self.OrdemNome = self.nome.lower()

    def set_numVitorias(self,num):
        self.numVitorias += num
    def set_numEmpate(self,num):
        self.numEmpate += num
    def set_numDerrota(self,num):
        self.numDerrota += num
    def set_golPositivo(self,num):
        self.golsPositivo += num
    def set_golNegativo(self,num):
        self.golsNegativo += num
    def set_pontosTime(self,num):
        self.pontosTime+=num
    def set_partidasJogadas(self):
        self.partidasJogadas+=1
    def set_diferencaGol(self,golAliado,golInimigo):
        self.diferencaGols+= (golAliado-golInimigo)
    
    def __lt__(self, outro):#>
        flagself = 0
        flagoutro = 0

        if outro.pontosTime < self.pontosTime:
            flagself+=200
        elif outro.pontosTime == self.pontosTime:
            flagself+=200
            flagoutro+=200
        else:
            flagoutro+=200

        if outro.numVitorias < self.numVitorias:
            flagself+=100
        elif outro.numVitorias == self.numVitorias:
            flagself+=100
            flagoutro+=100
        else:
            flagoutro+=100
        
        if outro.diferencaGols < self.diferencaGols:
            flagself+=50
        elif outro.diferencaGols == self.diferencaGols:
            flagself+=50
            flagoutro+=50
        else:
            flagoutro+=50
            
        
        if outro.golsPositivo < self.golsPositivo:
            flagself+=25
        elif outro.golsPositivo == self.golsPositivo:
            flagself+=25
            flagoutro+=25
        else:
            flagoutro+=25

        if outro.partidasJogadas < self.partidasJogadas:
            flagoutro+=12
        elif outro.partidasJogadas == self.partidasJogadas:
            flagself+=12
            flagoutro+=12
        else:
            flagself+=12
        
        if outro.OrdemNome < self.OrdemNome:
            flagoutro+=6
        else:
            flagself+=6

        if flagoutro<flagself:
            return True
        else:
            return False

            
    def __repr__(self):
        return " - "+str(self.nome)+": "+ str(self.pontosTime)+" pontos, "+str(self.partidasJogadas)+" jogos ("+str(self.numVitorias)+"-"+str(self.numEmpate)+"-"+str(self.numDerrota)+"), d.g. "+str(self.diferencaGols)+" ("+str(self.golsPositivo)+"-"+str(self.golsNegativo)+")"

def separaTime(palavra,lista_de_Times):
    lista  = palavra.split('#')#lista que divide na '#'
    time_one = lista[0].split(':')#informacoes do time 1 em um vetor
    time_two = lista[1].split(':')#informacoes do time 2 em um vetor
    pontoPrimeiro = int(time_one[1])
    pontoSegundo = int(time_two[1])
    calculaPonto(lista_de_Times,time_one[0],time_two[0],pontoPrimeiro,pontoSegundo)


def calculaPonto(lista,time1,time2,ponto1,ponto2):# a lista orientada a objeto
    if ponto1==ponto2:##se foi empate
        for i in range(len(lista)):
            if str(time1) == lista[i].nome:
                lista[i].set_numEmpate(1)
                lista[i].set_pontosTime(1)
                lista[i].set_diferencaGol(ponto1,ponto2)
                lista[i].set_partidasJogadas()
                lista[i].set_golPositivo(ponto1)
                lista[i].set_golNegativo(ponto2)
            if str(time2)==lista[i].nome:
                lista[i].set_numEmpate(1)
                lista[i].set_pontosTime(1)
                lista[i].set_partidasJogadas()
                lista[i].set_diferencaGol(ponto2,ponto1)
                lista[i].set_golPositivo(ponto2)
                lista[i].set_golNegativo(ponto1)
    elif ponto1>ponto2:#time 1 ganha
        for i in range(len(lista)):
            if str(time1) == lista[i].nome:
                lista[i].set_numVitorias(1)
                lista[i].set_pontosTime(3)
                lista[i].set_diferencaGol(ponto1,ponto2)
                lista[i].set_partidasJogadas()
                lista[i].set_golPositivo(ponto1)
                lista[i].set_golNegativo(ponto2)
            if str(time2)==lista[i].nome:
                lista[i].set_numDerrota(1)
                lista[i].set_partidasJogadas()
                lista[i].set_diferencaGol(ponto2,ponto1)
                lista[i].set_golPositivo(ponto2)
                lista[i].set_golNegativo(ponto1)
    else:##time 2 ganhou
        for i in range(len(lista)):
            if str(time1) == lista[i].nome:
                lista[i].set_numDerrota(1)
                lista[i].set_partidasJogadas()
                lista[i].set_diferencaGol(ponto1,ponto2)
                lista[i].set_golPositivo(ponto1)
                lista[i].set_golNegativo(ponto2)
            if str(time2)==lista[i].nome:
                lista[i].set_numVitorias(1)
                lista[i].set_partidasJogadas()
                lista[i].set_pontosTime(3)
                lista[i].set_diferencaGol(ponto2,ponto1)
                lista[i].set_golPositivo(ponto2)
                lista[i].set_golNegativo(ponto1)

def merge_sort(lista,inicio,fim,d=0):

    if inicio>=fim:
        return
    
    meio = (inicio+fim)//2
    merge_sort(lista,inicio,meio,d+1)
    merge_sort(lista,meio + 1,fim,d+1)

    tamanho = fim - inicio+1
    res = [0] * tamanho

    i = inicio
    j = meio+1

    for k in range(tamanho):# intercala
        if (j <= fim) and (i> meio or lista[j] <lista[i]):
            res[k] = lista[j]
            j+=1
        else:
            res[k] = lista[i]
            i+=1


    for i in range(tamanho):
        lista[inicio+i] = res[i]


num_de_Torneio = int(input())
while num_de_Torneio>0:
    nome_do_Torneio = input()
    quantidade_de_times = int(input())

    lista_de_Times = []
    for i in range(quantidade_de_times):
        nome_Time = input()
        lista_de_Times.append(Time(nome_Time))#cria um vet com os nomes

    quantidade_de_jogos = int(input())
    for i in range(quantidade_de_jogos):#ler a partida e insere os pontos
        ler_partida = input()
        separaTime(ler_partida,lista_de_Times)

    merge_sort(lista_de_Times,0,len(lista_de_Times)-1)#usando o algoritmo de ordenação?????

    print(nome_do_Torneio)
    for i in range(len(lista_de_Times)):#imprime a lista
        print("{}{}".format(i+1,lista_de_Times[i]))
    
    print(end='\n\n')
    num_de_Torneio-=1






        
