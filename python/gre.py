word = input()


size=len(word)

flag = maior = 0

for i in range(0,size,1):
    
    if word[i]!=word[i-1] and i!=0:
        flag=0


    if word[i] == 'A' or word[i] == 'C' or word[i] == 'G' or word[i] == 'T':
        flag+=1
    
    if maior < flag:
        maior = flag




print(maior)