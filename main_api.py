import requests
from acesso_cep import BuscaEndereco

print("\nValidando o CEP e aplicando máscara\n")
cep = "01001000"
obj_cep = BuscaEndereco(cep)
print(obj_cep)

print("\nTestando a API via CEP\n")
req = requests.get("https://viacep.com.br/ws/01001000/json/")
print(type(req.text))
print(req)
print(req.text)

# print("\nFazendo busca no via CEP\n")
# cep = "01001000"
# obj_cep = BuscaEndereco(cep)
# req = obj_cep.acessa_via_cep()
# #print(dir(req)) #retorna todos os atributos e métodos que o objeto possui
# print(type(req.text)) #str
# print(req.text) #atributo
# print(type(req.json())) #dict - dicionário
# print(req.json()) #método
# print(req.json()['cep']) #retorna somente o cep

print("\nFormatando busca no via CEP\n")
cep = "01001000"
obj_cep = BuscaEndereco(cep)
bairro, cidade, uf = obj_cep.acessa_via_cep()
print(bairro, cidade, uf)
