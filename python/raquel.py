def inserirArvore(arvore, valor):
  if arvore is None:
    return {'valor': valor, 'esq': None, 'dir': None}
  if valor < arvore['valor']:
    arvore['esq'] = inserirArvore(arvore['esq'], valor)
  else:
    arvore['dir'] = inserirArvore(arvore['dir'], valor)
  return arvore

def rotacaoRR(arvore):
  if arvore is None or ['dir'] is None:
    return arvore
  nova_raiz = arvore['dir']
  arvore['dir'] = nova_raiz['esq']
  nova_raiz['esq'] = arvore
  return nova_raiz
def pre_ordem(arvore):
  if arvore is not None:
    print(arvore['valor'], end=' ')
    pre_ordem(arvore['esq'])
    pre_ordem(arvore['dir'])
def pos_ordem(arvore):
  if arvore is not None:
    pos_ordem(arvore['esq'])
    pos_ordem(arvore['dir'])
    print(arvore['valor'], end=' ')
def construir(chaves):
  raiz = None
  for chave in chaves:
    raiz = inserirArvore(raiz, chave)
  return raiz

caso = 1
while True:
  entrada = input().strip()
  if entrada == "[]":
    break
  chaves = list(map(int, entrada[1:-1].split(', '))if entrada != "[]" else[])
  arvore = construir(chaves)
  print("Arvore", caso)
  caso += 1
  arvore = rotacaoRR(arvore)
  print("pre:", end=' ')
  pre_ordem(arvore)
  print()
  print("pos:", end=' ')
  pos_ordem(arvore)
  print()
