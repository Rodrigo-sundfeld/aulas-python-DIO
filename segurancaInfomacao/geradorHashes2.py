import hashlib

string = input('Digite o texto a ser gerado a hash: ')

menu = int(input('''### MENU - ESCOLHA UM TIPO DE ALGORITMO HASH ###
                1) md5
                2) sha1
                3) sha256
                4) sha512
                Digite o número do hash a gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print('A hash MD5 da string: ', string, 'é', resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print('A hash SHA1 da string: ', string, 'é', resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print('A hash SHA256 da string: ', string, 'é', resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print('A hash SHA512 da string: ', string, 'é', resultado.hexdigest())
else:
    print('Erro! Digite um número de 1 a 4.')

