from abc import ABC, abstractmethod

# Classe abstrata Funcionario
class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @abstractmethod
    def calcular_salario(self):
        pass

# Subclasse para funcionários horistas
class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self._horas_trabalhadas = horas_trabalhadas
        self._valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self._horas_trabalhadas

    @horas_trabalhadas.setter
    def horas_trabalhadas(self, horas_trabalhadas):
        self._horas_trabalhadas = horas_trabalhadas

    @property
    def valor_hora(self):
        return self._valor_hora

    @valor_hora.setter
    def valor_hora(self, valor_hora):
        self._valor_hora = valor_hora

    def calcular_salario(self):
        return self._horas_trabalhadas * self._valor_hora

# Subclasse para funcionários mensalistas
class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self._salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self._salario_mensal

    @salario_mensal.setter
    def salario_mensal(self, salario_mensal):
        self._salario_mensal = salario_mensal

    def calcular_salario(self):
        return self._salario_mensal

# Subclasse para funcionários comissionados
class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self._salario_base = salario_base
        self._vendas = vendas
        self._taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, salario_base):
        self._salario_base = salario_base

    @property
    def vendas(self):
        return self._vendas

    @vendas.setter
    def vendas(self, vendas):
        self._vendas = vendas

    @property
    def taxa_comissao(self):
        return self._taxa_comissao

    @taxa_comissao.setter
    def taxa_comissao(self, taxa_comissao):
        self._taxa_comissao = taxa_comissao

    def calcular_salario(self):
        return self._salario_base + (self._vendas * self._taxa_comissao)

# Função para processar pagamento de um funcionário
def processar_pagamento(funcionario):
    print(f"Nome: {funcionario.nome}, Salário: R${funcionario.calcular_salario():.2f}")

# Criação de instâncias de funcionários
funcionarios = [
    FuncionarioHorista(nome="Alice", matricula=101, horas_trabalhadas=160, valor_hora=20),
    FuncionarioMensalista(nome="Bob", matricula=102, salario_mensal=3000),
    FuncionarioComissionado(nome="Carlos", matricula=103, salario_base=2000, vendas=5000, taxa_comissao=0.1)
]

# Processar pagamento para cada funcionário
for funcionario in funcionarios:
    processar_pagamento(funcionario)
