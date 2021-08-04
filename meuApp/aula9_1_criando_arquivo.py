def escrever_arquivo(texto):
    arquivo = open('Teste primeiro arquivo.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualiza_arquivo(texto):
    arquivo = open('Teste primeiro arquivo.txt', 'a')
    arquivo.write(texto)
    arquivo.close()

def leitura_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)
if __name__ == '__main__':
    #escrever_arquivo('Primeira linha. \n')
    #atualiza_arquivo('Segunda linha. \n')
    leitura_arquivo('Teste primeiro arquivo.txt')
