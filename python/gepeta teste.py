def intercala(l1, l2):
	if len(l1) == 0:
		return l2
	elif len(l2) == 0:
		return l1
	sentinela = l1[-1] + l2[-1]
	tam = len(l1)+len(l2)
	# lis3 = [0]*(len(l1)+len(l2))
	l3 = []

	l1 += [sentinela]
	l2 += [sentinela]
	
	i = 0
	j = 0
	
	for a in range(tam):
		if l1[i] < l2[j]:
			l3 += [l1[i]]
			i = i + 1
		else:
			l3 += [l2[j]]
			j = j + 1

	return l3
	
lista1 = eval(input())
lista2 = eval(input())

while len(lista1) != 0 or len(lista2) != 0:
	print(intercala(lista1, lista2))
	input()
	lista1 = eval(input())
	lista2 = eval(input())
	
	



