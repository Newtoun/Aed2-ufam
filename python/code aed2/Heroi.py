from math import ceil
from math import floor

class monstro:

    def __init__(self,vida,ataque):
        self.vida = vida
        self.ataque = ataque
        self.QuantidadeDeAtaqueParaMatar = floor(vida/40) ## arredonda o valor de ataque para baixo, menor ataques necessario mais facil mata
        #self.QuantidadeDeAtaqueParaMorrer = ceil(100/self.ataque)##arredonda o valor de defesa para cima, maior defesa dificil matar
        self.Comparacao = self.QuantidadeDeAtaqueParaMatar*self.ataque#quanto menor o valor melhor

        #self.proporcaoSeXigual = self.QuantidadeDeAtaqueParaMorrer/self.QuantidadeDeAtaqueParaMatar ##quanto maior o valor melhor a escolha
        #self.ProbabMatar = self.ataque/self.vida # Quanto menor a probabilidade mais chance de matar o inimigo

    

    def __lt__(self,outro):       
        return self.Comparacao<outro.Comparacao


    
    def __repr__(self) -> str:
        return str(self.vida)+" "+str(self.ataque)



entrada = eval(input())
ponto = []

vidaHeroi = 100
AtaqueHeroi = 40
QuantMonstroAbatido = 0

for item in entrada:
    
    ponto.append(monstro(item[0],item[1]))
	# processe...

ponto.sort()

for i in range(0,len(entrada)):
    MonstroAtaque = ponto[i].ataque
    MonstroDefesa = ponto[i].vida
    while vidaHeroi>0:

        MonstroDefesa = MonstroDefesa-AtaqueHeroi
        if MonstroDefesa<=0:
            QuantMonstroAbatido+=1
            break
        
        vidaHeroi = vidaHeroi - MonstroAtaque

if vidaHeroi<0: 
    vidaHeroi=0

print("{} {}".format(QuantMonstroAbatido,vidaHeroi))
print(ponto)






