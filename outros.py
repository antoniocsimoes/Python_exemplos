from operator import attrgetter
from functools import total_ordering

class Conta:
    
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return "[>> Código {} Saldo {} <<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

print(Conta(88))

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print('Conta16 - {}'.format(conta16))

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print('Conta17 - {}'.format(conta17))

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes() #duck typing
    print('Conta - {}'.format(conta))

@total_ordering
class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self):
        return "[>> Código {} Saldo {} <<]".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
conta1.deposita(1000)
conta2 = ContaSalario(37)
conta2.deposita(500)
conta3 = ContaSalario(37)
conta3.deposita(50)

print(f'Conta1 é igual a Conta2 ? {conta1 == conta2} \n')

print(f'Conta1 é menor que Conta2 ? {conta1 < conta2} \n')

conta = [conta1, conta2, conta3]

def extrai_saldo(conta):
    return conta._saldo

print("Ordenação 1:")
for c in sorted(conta, key=extrai_saldo):    
    print(c)
print("\n")

print("Ordenação 2:")
for c in sorted(conta, key=attrgetter("_saldo")):   
    print(c)
print("\n")

print("Ordenação 3:")
for c in sorted(conta):    
    print(c)
print("\n")

conta1 = ContaSalario(3)
conta1.deposita(500)
conta2 = ContaSalario(37)
conta2.deposita(500)
conta3 = ContaSalario(377)
conta3.deposita(500)

conta = [conta1, conta2, conta3]
print("Ordenação 4:")
for c in sorted(conta, key=attrgetter("_saldo", "_codigo")):   
    print(c)
print("\n")

idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
    print(i, idades[i])

l = list(enumerate(idades))
print(l)

for valor in enumerate(idades): #gera uma tupla
    print(valor)

for indice, idade in enumerate(idades): #unpacking da nossa tupla
    print(indice, "x", idade)

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniela", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, idade, nascimento in usuarios: # já desempacotando
    print(nome)

for nome, _, _ in usuarios: # já desempacotando e ignorando o resto
    print(nome)

print(sorted(idades)) # ordenou minha lista original e devolve como uma lista

print(list(reversed(idades))) # inverteu o sentido da lista, de trás para frente, preciso colocar o list para ver o valor

print(sorted(idades, reverse=True)) # ordena de trás para frente