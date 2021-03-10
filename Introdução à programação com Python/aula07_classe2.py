class Calculadora:

    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def multiplicacao(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

calculadora = Calculadora()

print(calculadora.soma(10,2))
print(calculadora.subtracao(5,9))
print(calculadora.multiplicacao(30,4))
print(calculadora.divisao(20,5))