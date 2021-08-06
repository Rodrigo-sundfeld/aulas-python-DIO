import ctypes

pasta = input('Digite o caminho da pasta a ser ocultada exemplo (C:/pasta): ')

atributos_ocultar = 0x02
retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributos_ocultar)

if pasta:
    print('A pasta {} foi ocultada com sucesso.'.format(pasta))
else:
    print('A pasta {} não foi ocultada.'.format(pasta))
