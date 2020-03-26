from datetime import datetime
from datas_br import DatasBr

print("\nTestando a classe DatasBr \n")
cadastro = DatasBr()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())

print("\nDatetime formatado \n")
hoje = datetime.today()
hoje_formatado = hoje.strftime("%d/%m/%Y %H:%M")
print(hoje)
print(hoje_formatado)

print("\nTestando a classe DatasBr - data_formatada \n")
cadastro = DatasBr()
print(cadastro)

print("\nTestando a classe DatasBr - timedelta \n")
hoje = DatasBr()
print(hoje.tempo_cadastro())