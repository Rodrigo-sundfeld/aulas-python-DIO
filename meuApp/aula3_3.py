a = int(input('Digite a nota do primeiro bimestre: '))
if a > 10:
    a = int(input('Atenção você digitou uma nota inválida. Por favor verifique e digite novamente: '))
b = int(input('Digite a nota do segundo bimestre: '))
if b > 10:
    b = int(input('Atenção você digitou uma nota errada. Por favor verifique e digite novamente: '))
c = int(input('Digite a nota do terceiro bimestre: '))
if c > 10:
    c = int(input('Atenção você digitou uma nota errada. Por favor verifique e digite novamente: '))
d = int(input('Digite a nota do quarto bimestre: '))
if d > 10:
    d = int(input('Atenção você digitou uma nota errada. Por favor verifique e digite novamente: '))

media = (a + b + c + d) / 4
print('A média do aluno é: {}' .format(media))