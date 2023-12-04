tamanhoT = int(input())
num = int(input())
vet = [(None,"livre")] * tamanhoT 
while num>0:
    valor = int(input())
    pos = valor % tamanhoT
    while vet[pos][1]=="ocupado" and pos<tamanhoT:
        pos += 1
        pos = pos % tamanhoT
    
    vet[pos]= (valor,"ocupado")
    i=n=0
    num-=1
		
for i in range(len(vet)):
	if vet[i][0] is not None :
		print("{}: {}".format(i,vet[i][0]))
		