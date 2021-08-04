a = int(input('Digite a nota do primeiro bimestre: '))
b = int(input('Digite a nota do segundo bimestre: '))
c = int(input('Digite a nota do terceiro bimestre: '))
d = int(input('Digite a nota do quarto bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('A média do aluno é: {}' .format(media))
else:
    print('Ocorreu um erro! Alguma das notas digitadas foi maior que 10. Verifique e digite novamente.')
