from datetime import datetime, timedelta

def trabalhando_com_datetime():
    data_string = '01/01/2022 12:30:01'
    data_convertida = datetime.strptime(data_string, '%d/%m/%Y %H:%M:%S')
    print(data_convertida)
    nova_data_subtracao = data_convertida - timedelta(days=100, hours=2, minutes=30)
    nova_data_adicao = data_convertida + timedelta(days=40, hours=10, minutes=40)
    print('Nova data com adição de tempo: {}'.format(nova_data_subtracao))
    print('Nova data com subtraçao de tempo: {}'.format(nova_data_adicao))

if __name__ == '__main__':
    trabalhando_com_datetime()