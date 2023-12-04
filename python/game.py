def espiralMat(linha,coluna,resultado_x,resultado_y,nivel,num):#num comeca no valor maximo
   
    if linha == resultado_x and coluna == resultado_y:
        return num
    
    if nivel%2==0:#o valor maior comeca embaixo
        if coluna<nivel+1:
            return espiralMat(linha,coluna+1,resultado_x,resultado_y,nivel,num-1)
        
        if coluna ==nivel+1:
            return espiralMat(linha-1,coluna,resultado_x,resultado_y,nivel,num-1)
            

    else:#linha ou coluna precisa comecar com 0 depedendo da situaçao
        if linha<nivel+1:#linha comeca em 0
            return espiralMat(linha+1,coluna,resultado_x,resultado_y,nivel,num-1)        
        if linha == nivel+1:
            return espiralMat(linha,coluna-1,resultado_x,resultado_y,nivel,num-1)


#########################################################################################################
def espiral(linha,coluna,resultado_x,resultado_y,nivel,num):#num comeca no valor maximo
    
    if nivel%2==0:#o valor maior comeca embaixo

        for i in range(1,nivel+1,1):
            coluna +=1
            num-=1
            if linha == resultado_x and coluna == resultado_y:
                print(num)

        for i in range(1,nivel+1,1):
            linha -=1
            num-=1
            if linha == resultado_x and coluna == resultado_y:
                print(num)
        
    else:#linha ou coluna precisa comecar com 0 depedendo da situaçao
        for i in range(1,nivel+1,1):
            coluna +=1
            num-=1
            if linha == resultado_x and coluna == resultado_y:
                print(num)

        for i in range(1,nivel+1,1):
            linha -=1
            num-=1
            if linha == resultado_x and coluna == resultado_y:
                print(num)



repticao = int(input())
linha = coluna = 0

while repticao>0:
    entrada = input()
    linha, coluna = (int(numero) for numero in entrada.split(' '))

    if linha>coluna:
       espiral(linha,1,linha,coluna,linha,linha**2)
    else:
       espiral(1,coluna,linha,coluna,coluna,coluna**2)

 

    repticao-=1