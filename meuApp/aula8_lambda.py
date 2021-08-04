#lambda é uma função anonima para simplificar algo que utilizaremos mais de uma vez no codigo

contador_letras = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'hiena']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
subtracao = lambda a, b: a - b
print(soma(88, 18))
print(subtracao(19, 11.87))


