class Funcionario:
    def __init__(self, nome, sobrenome, titulo):
        self.nome = nome
        self.sobrenome = sobrenome
        self.titulo = titulo

class Celetista(Funcionario):
    def __init__(self, nome, sobrenome, titulo, horas_por_semana, salario_semanal):
        super().__init__(nome, sobrenome, titulo)
        self.horas_contrato = horas_por_semana
        self.salario_semanal = salario_semanal
        self.horas_trabalhadas = 0

    def registrar(self, horas):
        self.horas_trabalhadas += horas

    def calcular_salario(self):
        if self.horas_trabalhadas <= self.horas_contrato:
            return self.salario_semanal * (self.horas_trabalhadas/ self.horas_contrato  )
        else:
            horas_extras = self.horas_trabalhadas - self.horas_contrato
            dinheiro_hora = self.salario_semanal/self.horas_contrato
            #print(dinheiro_hora)
            
            salario = self.salario_semanal + (2 *(horas_extras*dinheiro_hora))
            
            return salario


class Comissionado(Funcionario):
    def __init__(self, nome, sobrenome, titulo, comissao):
        super().__init__(nome, sobrenome, titulo)
        self.comissao = comissao
        self.total_vendas = 0

    def registrar(self, vendas):
        self.total_vendas += vendas

    def calcular_salario(self):
        salario = self.total_vendas * self.comissao
        return salario


class FreeLancer(Funcionario):
    def __init__(self, nome, sobrenome, titulo):
        super().__init__(nome, sobrenome, titulo)
        self.total_projetos = 0

    def registrar(self, valor_projeto):
        self.total_projetos += valor_projeto

    def calcular_salario(self):
        return self.total_projetos


num = int(input())

dic = {}

for _ in range(num):
    funcionario_data = eval(input())
    sobrenome = funcionario_data['sobrenome']
    regime = funcionario_data['regime']
    nome = funcionario_data['nome']
    titulo = funcionario_data['titulo']

    if regime == 'celetista':
        horas_por_semana = funcionario_data['horas_por_semana']
        salario_semanal = funcionario_data['salario_semanal']
        dic[sobrenome] = Celetista(nome, sobrenome, titulo, horas_por_semana, salario_semanal)
    elif regime == 'comissionado':
        comissao = funcionario_data['comissao']
        dic[sobrenome] = Comissionado(nome, sobrenome, titulo, comissao)
    elif regime == 'freelancer':
        dic[sobrenome] = FreeLancer(nome, sobrenome, titulo)


registro = int(input())


for _ in range(registro):
    sobrenome, parametro = eval(input())

    if sobrenome in dic:
        funcionario = dic[sobrenome]
        funcionario.registrar(parametro)
salarios = []
for funcionario in dic.values():
    salario = funcionario.calcular_salario()
    salarios.append((funcionario.nome, funcionario.sobrenome, salario))

salarios.sort(key=lambda x: x[1])
for nome, sobrenome, salario in salarios:
    funcionario = dic[sobrenome]
    money = round(salario, 2)
    print("{} {} {} recebeu R$ {:.2f}".format(funcionario.titulo,funcionario.nome,funcionario.sobrenome,money))
#2
#{'regime':'celetista','nome':'Durel','sobrenome':'Xenoficles','titulo':'Sra.','horas_por_semana':40,'salario_semanal':3600}
#{'regime':'celetista','nome':'Tariel','sobrenome':'Martelo','titulo':'Sr.','horas_por_semana':40,'salario_semanal':3600}
# 2
#('Xenoficles',56)
#('Martelo',36)