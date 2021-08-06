from bs4 import BeautifulSoup

import requests

site = requests.get('https://www.climatempo.com.br/').content
# Objeto site recebendo o conteudo da requisiçao HTTP do site acima

soup = BeautifulSoup(site, 'html.parser')
# Objeto soup baixando do site o html

#print(soup.prettify())
# Transforma o html em string e o print exibe o html

#print(soup.title.string)

#print(soup.a)
