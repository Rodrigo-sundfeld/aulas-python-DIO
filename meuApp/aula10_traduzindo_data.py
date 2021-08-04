from datetime import datetime

def trabalhando_com_datetime():
    data_atual = datetime.now()
    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sabado', 'Domingo')
    print(tupla[data_atual.weekday()])
    data_criada = datetime(2021, 8, 2, 20, 2, 10)
    print(data_criada)
    print(data_criada.strftime('%c'))
    data_string = '01/01/2022 12:30:01'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)

if __name__ == '__main__':
    trabalhando_com_datetime()