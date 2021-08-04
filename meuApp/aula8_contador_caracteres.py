def contador_caracteres(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade_caracteres = len(x)
        contador.append(quantidade_caracteres)
    return contador

if __name__ == '__main__':
    lista = ['cachorro', 'gato', 'papagaio']
    print(contador_caracteres(lista))