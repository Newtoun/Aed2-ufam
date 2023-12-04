class Gatos:
	
	def __init__(self,nome,energia,defesa,forca):
		self.nome = nome
		self.energia = energia
		self.defesa = defesa
		self.forca = forca
	
	def dano(self,num):
		if num < 0 :
			return
		self.energia -= num
		if self.energia < 0 :
			self.energia = 0
		

def insere(entrada):
	return Gatos(entrada["nome"],entrada['energia'],entrada['defesa'],entrada['forca'])

def simula (ataq , defe):
	print("{} esta atacando!".format(ataq.nome))
	for i in range(len(defe)):
		defesa = int(defe[i].defesa)
		defe[i].dano(int(ataq.forca) - defesa)
		print("Energia de {}: {}".format(defe[i].nome, defe[i].energia))
		if defe[i].energia == 0:
			print("{} fugiu!".format(defe[i].nome))
	
	    
	

Atacante = insere(eval(input()))

#print(type(Atacante.dano))
num = int(input())
defesa = []

for i in range(num):
	entrada = eval(input())
	defesa.append(insere(entrada))

simula(Atacante,defesa)
