
lista = [1, 10]
try:
    divisao = 10 / 0
    #numero = lista[5]

except ZeroDivisionError:
    print('Não é possivel realizar divisao por zero.')
except ArithmeticError:
    print('Houve um erro na expressão aritimética')
except IndexError:
    print('Erro ao acessar um index invalido na lista.')
except BaseException as ex:
    print('erro desconhecido. Erro: {}'.format(ex))

