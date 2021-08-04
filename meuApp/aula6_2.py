conjunto = {1, 2, 3, 4, 5}
conjunto2 = {3, 5, 6, 7, 8}

conjunto_diferenca = conjunto.difference(conjunto2)
print('Conjunto diferença 1: {}'.format(conjunto_diferenca))

conjunto_diferenca1 = conjunto2.difference(conjunto)
print('Conjunto diferença 2: {}'.format(conjunto_diferenca1))

conjunto_dif_simetrica = conjunto.symmetric_difference(conjunto2)
print('Diferença simetrica: {}'.format(conjunto_dif_simetrica))

