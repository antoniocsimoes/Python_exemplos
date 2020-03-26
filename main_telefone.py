from telefonesbr import  TelefonesBr
import re

padrao = "[0-9][a-z][0-9]"
texto = "123 1a2 1cc aa1"
resposta = re.search(padrao, texto)
print(resposta) #traz a informação do posicionamento
print(resposta.group()) #traz somente a informação que ele achou

padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
texto = "aaabbbccc rodrigo123@gmail.com.br"
resposta = re.search(padrao, texto)
print(resposta)
print(resposta.group())

padrao = "\w{5,50}@[a-z]{3,10}.com.br"
texto = "aaabbbccc rodrigo123@gmail.com.br"
resposta = re.search(padrao, texto)
print(resposta)
print(resposta.group())

padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "eu gosto do número 2126451234 e gosto também do 2136431234"
resposta = re.findall(padrao, texto) #traz uma lista com todas as ocorrências
print(resposta)

telefone = "552126481234"
padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
resposta = re.search(padrao, telefone)
print(resposta)
print(resposta.group())

print("\n Testando classe TelefonesBr \n")

telefone = "552126481234"
telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)
