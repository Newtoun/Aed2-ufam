def inunda(mapa, x, y, lar, comp, alturaMax):  
  #parado
  
  for i in range(len(mapa)):
    for j in range(len(mapa[0])):
      print(mapa[i][j], end = " ")
    print()
  print()
  
  if(mapa[x][y]<=alturaMax):
    mapa[x][y] = 10
  if(y+1 <= comp - 1 and y+1 >=0):  
    if(mapa[x][y+1]<=alturaMax):
      mapa[x][y+1]=10
      inunda(mapa, x, y+1, lar, comp, alturaMax)
  if(y-1 >= 0 and y-1 <=comp-1):
    if(mapa[x][y-1]<=alturaMax):
      mapa[x][y-1]=10  
      inunda(mapa, x, y-1, lar, comp, alturaMax)
  #x+1 e possibilidades com x+1  
    
  if(x+1 <= lar-1 and x+1>=0):
    if(mapa[x+1][y]<=alturaMax):
      mapa[x+1][y]=10
      inunda(mapa, x+1, y, lar, comp, alturaMax)
    
  #x-1 e possibilidades com x-1
  if(x-1 >=0 and x-1 <=lar-1):  
      if(mapa[x-1][y]<=alturaMax):
        mapa[x-1][y]=10
        inunda(mapa, x-1, y, lar, comp, alturaMax)
      

  

# Lê os parâmetros do mapa
alturaMax = int(input())
casaX, casaY = eval(input())
mapa = eval(input())

encontrou = False
for i in range (len(mapa)):
  for j in range (len(mapa[0])):
    if(mapa[i][j]==0):
      inicioX = i
      inicioY = j
      encontrou = True
      break
  if(encontrou == True or i==len(mapa)-1):
    break

comp = len(mapa)
lar = len(mapa[0]) 

inunda(mapa, inicioX, inicioY, comp, lar, alturaMax)

if(mapa[casaX][casaY]== 10):
  print('Deu ruim!')
else:
  print(':)')