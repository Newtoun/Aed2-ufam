tabela = (['61','Brasilia'],
			 ['71','Salvador'],
			 ['11','Sao Paulo'],
			 ['21','Rio de Janeiro'],
			 ['32','Juiz de Fora'],
			 ['19','Campinas'],
			 ['27','Vitoria'],
			 ['31','Belo Horizonte']
			)

num = int(input())
veri = dict(tabela)

if str(num) in veri:
    print(veri[str(num)])
else:
    print('DDD nao cadastrado')
	
