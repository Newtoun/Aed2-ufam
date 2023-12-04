def mdc(a,b):
    if a%b==0:
        return b
    else:
       return mdc(b,(a%b))

input()

entrada = input()
vet = entrada.split()
flag = 0
cont = 0

for j in range(0,len(vet)):
    for i in range(0,len(vet)):
        if i!=j :
            flag = mdc(int(vet[j]),int(vet[i]))
            if flag==1:
                cont+=1

print(cont//2)
