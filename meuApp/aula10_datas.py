from datetime import date

def trabalhando_com_datas():
    data_atual = date.today()
    data_atual_str = data_atual.strftime('%A - %B - %Y')
    print(data_atual)
    print(data_atual.strftime('%d/%m/%y'))
    print(data_atual.strftime('%A %B %Y'))
    print(data_atual_str)
    print(type(data_atual))
    print(type(data_atual_str))

if __name__ == '__main__':
    trabalhando_com_datas()

