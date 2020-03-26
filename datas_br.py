# https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior

from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()
    
    def mes_cadastro(self):
        meses_do_ano = [
            "Janeiro", "Fevereiro", "Março",
            "Abril", "Maio", "Junho", "Julho",
            "Agosto", "Setembro", "Outubro",
            "Novembro", "Dezembro"
        ]
        mes = self.momento_cadastro.month - 1
        return meses_do_ano[mes]

    def dia_semana(self):
        dia_semana = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sábado",
            "domingo"
        ]
        dia_da_semana = self.momento_cadastro.weekday()
        return dia_semana[dia_da_semana]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro