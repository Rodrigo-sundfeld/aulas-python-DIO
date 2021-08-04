a = int(input('Entre com um numero: '))

div = 0
for x in range(1, a+1):
    resto = a % x
    print(x, resto)
    if resto == 0:
        div += 1

if div == 2:
    print('O numero {} é um numero primo.' .format(a))
else:
    print('O numero {} não é um numero primo.'.format(a))
