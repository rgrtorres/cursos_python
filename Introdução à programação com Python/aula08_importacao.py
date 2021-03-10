from aula07_televisao import Televisao
from aula08_contador_letras import contar_letras, teste

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    lista = ['cachorro', 'gato', 'renan']
    total_letras = contar_letras(lista)
    print('O total de letras é de {}'.format(total_letras))
    print(teste())