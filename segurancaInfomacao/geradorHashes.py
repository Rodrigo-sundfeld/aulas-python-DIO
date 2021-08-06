import hashlib

stringMd5 = input('Digite o texto a ser gerado a hash md5: ')
stringSha1 = input('Digite o texto a ser gerado a hash sha1: ')

resultadoMd5 = hashlib.md5(stringMd5.encode('utf-8'))
resultadoSha1 = hashlib.sha1(stringSha1.encode('utf-8'))

print('O hash da string pelo algoritmo md5 é: ', resultadoMd5.hexdigest())
print('O hash da string pelo algoritmo sha1 é:', resultadoSha1.hexdigest())