def concatena(A, B):
    indcA = 0
    indcB = 0
    indcC = 0
    tam = len(A) + len(B)  # Calcular o tamanho correto da lista final
    lista = [0] * tam
    while indcA + indcB != tam:
        if indcA < len(A) and (indcB >= len(B) or A[indcA] <= B[indcB]):
            lista[indcC] = A[indcA]
            indcA += 1
        else:
            lista[indcC] = B[indcB]
            indcB += 1
        indcC += 1

    return lista


a = [2,3,4,5]
b = [1,6]
print(concatena(a,b))