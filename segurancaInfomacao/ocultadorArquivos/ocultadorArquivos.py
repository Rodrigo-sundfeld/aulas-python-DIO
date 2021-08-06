import ctypes

atributos_ocultar = 0x02
retorno_erro = ctypes.windll.kernel32.SetFileAttributesW('ocultar.txt', atributos_ocultar)
retorno_sucesso = ctypes.windll.kernel32.SetFileAttributesW('arquivoTesteOcultar.txt', atributos_ocultar)

if retorno_erro:
    print('Arquivo foi ocultado com sucesso.')
else:
    print('Arquivo não foi ocultado.')

if retorno_sucesso:
    print('Arquivo foi ocultado com sucesso.')
else:
    print('Arquivo não foi ocultado.')
