loop = int(input())

while loop>0:
    entrada = input()
    vet = entrada.split()
    
    if int(vet[2])%2==0:
        print((int(vet[0])*int(vet[2]) -int(vet[1])*int(vet[2]))//2)#par ok
    else:
        num = ((int(vet[2])//2)+1)
        print(int(vet[0])*num -int(vet[1])*(int(vet[2])-num))
    
    
    loop-=1