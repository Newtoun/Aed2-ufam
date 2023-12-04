def solve(x, y, mapa, alturaMax, largura, altura, casaX, casaY):
    if x == casaX and y == casaY:
        return True
    
    if x + 1 < altura and mapa[x + 1][y] <= alturaMax and (x + 1, y) != (x, y):
        if solve(x + 1, y, mapa, alturaMax, largura, altura, casaX, casaY):
            return True
    if x - 1 >= 0 and mapa[x - 1][y] <= alturaMax and (x - 1, y) != (x, y):
        if solve(x - 1, y, mapa, alturaMax, largura, altura, casaX, casaY):
            return True
    if y + 1 < largura and mapa[x][y + 1] <= alturaMax and (x, y + 1) != (x, y):
        if solve(x, y + 1, mapa, alturaMax, largura, altura, casaX, casaY):
            return True
    if y - 1 >= 0 and mapa[x][y - 1] <= alturaMax and (x, y - 1) != (x, y):
        if solve(x, y - 1, mapa, alturaMax, largura, altura, casaX, casaY):
            return True
    
    return False

# Lê os parâmetros do mapa
alturaMax = int(input())
casaX, casaY = eval(input())  # corrected the order of casaX and casaY
mapa = eval(input())
flag = 0
for i in range(len(mapa)):
    for j in range(len(mapa[0])):
        if mapa[i][j] == 0 and flag == 0:
            resultado = solve(i, j, mapa, alturaMax, len(mapa[0]), len(mapa), casaX, casaY)
            if resultado:
                flag = 1

if flag == 0:
    print(":)")
else:
    print("Deu ruim!")
