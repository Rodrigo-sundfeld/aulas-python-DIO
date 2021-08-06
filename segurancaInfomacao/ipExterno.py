import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'
resposta = urlopen(url)
dados = json.load(resposta)

ip = dados['ip']
organizacao = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print('Detalhes do IP externo\n')
print('Organizaçao: {0}\n'
      'Região: {1}\n'
      'Pais: {2}\n'
      'Cidade: {3}\n'
      'IP: {4}\n'
      .format(organizacao, regiao, pais, cidade, ip))