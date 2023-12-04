dena= input()
tamanho=len(dena)
#lista=[0]* tamanho
i=0
repetidos=0
j=0
maisRepetido=0
OmaisRepetido=0
Dena = dena+"\n"
#print(Dena)

while j<tamanho:
	repetidos=0
	for n in range (0,tamanho):
		if Dena[n]==Dena[j] and (Dena[n-1]==Dena[j] or Dena[n+1]==Dena[j]):
			repetidos+=1
		#if dena[tamanho-1]==dena[j] and  (dena[n-1]==dena[j] or dena[n+1]==dena[j]):
		#	repetidos+=1
	
	if maisRepetido<repetidos:
		#print("repetidos",repetidos)
		maisRepetido=repetidos
		#print("rmaisRepetidos",maisRepetido)
	j+=1
print(maisRepetido)
