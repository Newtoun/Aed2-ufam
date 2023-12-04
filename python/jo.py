def primo(n):
    NUM=0
    if n==1: 
        return False
        
    for i in range(2,n-1,1):
        if(n%i)==0: 
            return False
    
    return True 
    

repeticao = int(input())

while repeticao>0:
    
    num = int(input())
    print(primo(num))
    repeticao-=1