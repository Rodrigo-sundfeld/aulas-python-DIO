conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjunto_subset = conjunto_a.issubset(conjunto_b)
print('A é um subconjunto de B? {}'.format(conjunto_subset))

conjunto_subset_2 = conjunto_b.issubset(conjunto_a)
print('B é um subconjunto de A? {}'.format(conjunto_subset_2))

conjunto_superset = conjunto_a.issuperset(conjunto_b)
print('A é um superconjunto de B? {}'.format(conjunto_superset))

conjunto_superset_2 = conjunto_b.issuperset(conjunto_a)
print('B é um superconjunto de A? {}'.format(conjunto_superset_2))