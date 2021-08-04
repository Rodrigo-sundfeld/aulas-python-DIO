class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def muliplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b


calculadora = Calculadora()
print(calculadora.soma(10, 3))
print(calculadora.subtracao(20, 19))
print(calculadora.muliplicacao(2.8, 10))
print(calculadora.divisao(89, 72))
