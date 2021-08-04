from datetime import datetime

def trabalhando_com_datetime():
    data_atual = datetime.now()
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%H:%M:%S'))
    print(data_atual.strftime('%d/%m/%y %H:%M:%S'))
    print(data_atual.strftime('%c'))
    print(data_atual.day)
    print(data_atual.year)
    print(type(data_atual))
if __name__ == '__main__':
    trabalhando_com_datetime()
