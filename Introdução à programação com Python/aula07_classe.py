class Calculadora:
    def __init__(self,a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def multiplicacao(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

calculadora = Calculadora(10, 2)

print("Valor de a: {}".format(calculadora.a))
print("Valor de b: {}".format(calculadora.b))

print(calculadora.soma())
print(calculadora.subtracao())
print(calculadora.multiplicacao())
print(calculadora.divisao())