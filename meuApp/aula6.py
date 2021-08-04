conjunto = {1, 2, 3, 4, 5, 6, 7}
print(type(conjunto))
print(conjunto)

conjunto_1 = {1, 2, 3, 4, 5, 6, 7, 7, 7, 7, 7}
print(conjunto_1)

conjunto.add(10)
print(conjunto)
conjunto.discard(2)
print(conjunto)