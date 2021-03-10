lista = [1, 10]
try:
    arquivo = open('teste.txt', 'r')
    texto = arquivo.read()
    divisao = 10 / 0
    numero = lista[1]
    print(arquivo)
except BaseException as ex:
    print("Não é possivel realizar uma divisão por zero.")
except ArithmeticError:
    print("Houve um erro ao realizar a operação aritmética!")
except IndexError:
    print("Erro ao acessar um indice da lista invalido da lista.")
else:
    print("Executa quando não tem exceções")
finally:
    print('Sempre executa')
    print('Fechando arquivo...')
    arquivo.close()