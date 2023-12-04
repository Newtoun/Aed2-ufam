class Pessoa:
    def __init__(self,nome,nota1,nota2,nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        lista = [nota1,nota2,nota3]
        lista.sort()
        self.pontos = lista[1]+lista[2]
    
    def __lt__(self,outro):
        return outro.pontos<self.pontos

    def __repr__(self):
        return str(self.nome) +": "+str(self.pontos)
    

loop = int(input())
tam = loop
lista = []
while loop>0:
    entrada = eval(input())

    lista.append(Pessoa(entrada[0],entrada[1],entrada[2],entrada[3]))

    loop-=1

lista.sort()
for i in range(0,tam,1):
    print(lista[i])
