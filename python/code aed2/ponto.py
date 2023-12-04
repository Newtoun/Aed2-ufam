import math
class Ponto:
    def __init__(self, x, y):
        self.norma = (x**2 + y**2)**.5
        self.x=x
        self.y=y
        # Construtor.
        # Guarde os atributos self.x e self.y

    def __lt__(self, outro):
        if self.norma == outro.norma and self.x==outro.x:
           return self.y<outro.y
        elif self.norma==outro.norma:
           return self.x<outro.x
        else:
            return self.norma < outro.norma

     #########################################       
    def __repr__(self):
        return  str(self.x) +" "+ str(self.y)

# Leitura da entrada
entrada = eval(input())

#print(entrada)
# Crie uma lista vazia e insira os objetos da classe ponto nela
#ponto = [len.(entrada)]
ponto = []



for item in entrada:
    
    ponto.append(Ponto(item[0],item[1]))
	# processe...

ponto.sort()
for i in range(0,len(entrada)):
    print(ponto[i])
    print()
    
# Ordene e imprima de acordo com o enunciado