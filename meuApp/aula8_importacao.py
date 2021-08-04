# No Python os modulos são os arquivos .py
# Os modulos conseguem interagir entre si

from aula7_televisao import Televisao
from aula7_calculadora1 import Calculadora
from aula8_contador_caracteres import contador_caracteres

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora (10, 9)
    print(calculadora.soma())
    print(calculadora.divisao())
    lista = ['peixe', 'avestruz', 'marreco', 'urubu']
    print('Total de caracteres de cada palavra {}'.format(contador_caracteres(lista)))
