calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a -b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
subtracao = calculadora['subtracao']
multiplicacao = calculadora['multiplicacao']
divisao = calculadora['divisao']
print('Total da soma {}'.format(soma(10, 9)))
print('Total da subtracao {}'. format(subtracao(19, 9)))
print('Total da multiplicacao {}'.format(multiplicacao(10, 10)))
print('Total da divisao {}'.format(divisao(19, 7)))