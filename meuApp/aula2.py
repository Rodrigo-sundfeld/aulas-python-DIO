a = int(input('Entre com o primeiro valor: '))
b = int(input('Entre com o segundo valor:'))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b
resultados = ('soma: {soma}. '
      '\nsubtração: {sub}. '
      '\nmultiplicacao: {mult}. '
      '\ndivisao: {div}. '
      '\nresto: {res}'
      .format(soma=soma, sub=subtracao, mult=multiplicacao, div=divisao, res=resto))

print(resultados)