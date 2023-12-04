tamanho = int(input())

lista = [] * tamanho

for i in range(0,tamanho):
    lista[i]=int(input())


lista.sort()

flag = 0

for i in range(1,tamanho):
    if lista[i-1]!=lista[i]:
        flag +=1

print(flag)
