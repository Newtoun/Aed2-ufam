vetA=['a','c','d','r']
vetB=['a','a','a']
vetC = [0]*7
tamA=4
tamB=3
total = tamA+tamB
indcA=0
indcB=0
indC=0

while indcA+indcB!=total:
    if(indcA!=tamA and vetA[indcA]<vetB[indcB]):
        vetC[indC]=vetA[indcA]
        indcA+=1
    else:
        vetC[indC]=vetB[indcB]      
        indcB+=1
    indC+=1


print(vetC)