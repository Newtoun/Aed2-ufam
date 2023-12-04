def valorString(string):
	n = len(string)
	soma = 0
	for i in range(n):
		if string[i]!='-':
			soma+=ord(string[i])-96
	
	return soma

tamanhoT = int(input())
num = int(input())
vet = [(None,"livre")] * tamanhoT 
while num>0:
    string = input()
    valor  = valorString(string)
    pos = valor % tamanhoT
    while vet[pos][1]=="ocupado" :
        pos += 1
        pos = pos % tamanhoT
    
    vet[pos]= (string,"ocupado")
    i=n=0
    num-=1
		
for i in range(len(vet)):
	if vet[i][0] is not None :
		print("{}: {}".format(i,vet[i][0]))
		