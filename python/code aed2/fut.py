class Time:

    def __init__(self,nome,numVitorias,numEmpate,numDerrota,golsPositivo,golsNegativo):
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


    def __lt__(self, outro):#>
        flagself = 0
        flagoutro = 0

        criterio1 = outro.pontosTime < self.pontosTime#200 pontos
        criterio2 = outro.numVitorias < self.numVitorias#100 pontos
        criterio3 = outro.diferencaGols < self.diferencaGols# 50pontos
        criterio4 = outro.golsPositivo < self.golsPositivo # 25 pontos
        criterio5 = outro.partidasJogadas < self.partidasJogadas # 12 ponto
        criterio6 = outro.OrdemNome < self.OrdemNome # 6 ponto

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


lista = []
loop = int(input())

for i in range(0,loop,1):
    entrada = eval(input())
    lista.append(Time(entrada[0],entrada[1],entrada[2],entrada[3],entrada[4],entrada[5]))

lista.sort()

for i in range(0,loop,1):
    print("{}{}".format(i+1,lista[i]))
        
