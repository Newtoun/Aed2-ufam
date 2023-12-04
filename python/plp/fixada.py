import sys
operadores = {"*", "/", "+", "-"}

def resolve(lista):
    operacao = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
            '*': lambda x, y: x * y, '/': lambda x, y: x / y}
    pilha = []
    for elemento in reversed(lista):

        if isinstance(elemento, float):
            pilha.append(elemento)
        elif elemento in operacao and lista!=[]:
            num1 = pilha.pop()
            num2 = pilha.pop()
            resu = operacao[elemento](num1, num2)
            pilha.append(resu)
    return pilha[0]


#def expressao_valida(operador, num1, num2):
#    if operador in operadores and isinstance(num1, float) and isinstance(num2, float):
#        return True
#    return False

#entrada = ['-', 5.0, 2.0, '.']
for line in sys.stdin:
    entrada = eval(line.strip())
    #print(type(entrada))
    if entrada !=[]:
        print("{:.2f}".format(resolve(entrada[:-1])))
    

