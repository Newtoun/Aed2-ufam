def troca(num1,num2):
    temp = num1
    num1 =num2
    num2 = temp



lista = [8,7,6,5,4,3,2,1]#8
n=8

for i in range(n-1,0,-1): # n

    for j in range(n-1,0,-1): # n
        if lista[j]<lista[j-1]:# 1
            temp = lista[j]  #O(1)
            lista[j] = lista[j-1] #O(1)
            lista[j-1] = temp #O(1)

    

print(lista)

