from datetime import time

def trabalhando_com_time():
    horario = time(hour=15, minute=18, second=30)
    horario_str = horario.strftime('%H:%M:%S')
    print(horario.strftime('%H:%M:%S'))
    print(type(horario_str))
    print(type(horario))

if __name__ == '__main__':
    trabalhando_com_time()