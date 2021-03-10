def contar_letras(lista_palavra):
    contador = []
    for x in lista_palavra:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste():
    return 'teste'

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contar_letras(lista))