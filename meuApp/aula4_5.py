a = int(input('Digite a nota do primeiro bimestre: '))
while a > 10:
    a = int(input('Atenção você digitou uma nota inválida. Por favor verifique e digite novamente: '))
b = int(input('Digite a nota do segundo bimestre: '))
while b > 10:
    b = int(input('Atenção você digitou uma nota errada. Por favor verifique e digite novamente: '))
c = int(input('Digite a nota do terceiro bimestre: '))
while c > 10:
    c = int(input('Atenção você digitou uma nota errada. Por favor verifique e digite novamente: '))
d = int(input('Digite a nota do quarto bimestre: '))
while d > 10:
    d = int(input('Atenção você digitou uma nota errada. Por favor verifique e digite novamente: '))
media = (a + b + c + d) / 4
print('A média do aluno é: {}' .format(media))