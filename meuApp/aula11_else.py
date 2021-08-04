
try:
    arquivo = open('Teste primeiro arquivo.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 1

except ZeroDivisionError:
    print('Não é possivel realizar divisao por zero.')
except ArithmeticError:
    print('Houve um erro na expressão aritimética')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('Executa quando não ocorre exceção')
finally:
    print('Sempre executa')
    print('Fechando arquivo')
    arquivo.close()