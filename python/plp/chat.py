import sys

operadores = {"*", "/", "+", "-"}

def resolve(lista):
    operacao = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
                '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    pilha = []
    for elemento in reversed(lista):
        if isinstance(elemento, float):
            pilha.append(elemento)
        elif elemento in operadores and lista != []:
            num1 = pilha.pop()
            num2 = pilha.pop()
            resu = operacao[elemento](num1, num2)
            pilha.append(resu)
    return pilha[0]


for line in sys.stdin:
    entrada = line.strip().split()
    if entrada != []:
        expressao = [float(elemento) if elemento.isdigit() or '.' in elemento else elemento for elemento in entrada]
        print(resolve(expressao[:-1]))
