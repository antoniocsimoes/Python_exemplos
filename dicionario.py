#dicionário - chave e valor

from collections import defaultdict, Counter

aparicoes = {
    "Guilherme" : 1,
    "cachorro" : 2,
    "nome" : 2,
    "vindo": 1
}

print(type(aparicoes))

print(aparicoes["Guilherme"])

print(aparicoes.get("xpto", 0)) #procura o xpto senão achar coloca zero

print(aparicoes.get("cachorro",0))

aparicoes2 = dict(Guilherme = 2, cachorro = 1) #outra forma de criar um dicionário
print(aparicoes2)

aparicoes["Carlos"] = 1 #adicionando elemento no dicionário
print(aparicoes)

aparicoes["Carlos"]=2
print(aparicoes)

del aparicoes["Carlos"] #deleta o elemento "Carlos" do dicionário
print(aparicoes)

print("cachorro" in aparicoes) #busca "cachorro" nas chaves
print("Carlos" in aparicoes)

for elmento in aparicoes:
    print(elmento)

for elmento in aparicoes.keys():
    print(elmento)

for elmento in aparicoes.values():
    print(elmento)

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=", valor)

print(["palavra {}".format(chave) for chave in aparicoes.keys()])

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(meu_texto.split())
meu_texto = meu_texto.lower()
print(meu_texto.split())

aparicoes_ = {}

for palavra in meu_texto.split():
    ate_agora = aparicoes_.get(palavra, 0)
    aparicoes_[palavra] = ate_agora + 1

print(aparicoes_)

aparicoes = defaultdict(int)

# for palavra in meu_texto.split():
#     ate_agora = aparicoes_[palavra]
#     aparicoes_[palavra] = ate_agora + 1

for palavra in meu_texto.split():
    aparicoes_[palavra] += 1

print(aparicoes_)

dicionario = defaultdict(int) #defini zero como padrão
print(dicionario['guilherme'])


dicionario['guilherme'] = 15
print(dicionario['guilherme'])

class Conta:
    def __init__(self):
        print("Criando uma conta")

contas = defaultdict(Conta)
contas[15]
contas[17]

aparicoes_ = Counter(meu_texto.split())
print(aparicoes_)