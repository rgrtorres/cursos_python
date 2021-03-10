import shutil

def escreverArquivo(texto):
    arquivo = open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizaArquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()

def lerArquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

def mediasNotas(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)

    aluno_nota = aluno_nota.split('\n')
    lista_media = []

    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        
        media = lambda notas: sum([int(i) for i in notas]) / 4
        print(media(lista_notas))
        lista_media.append({aluno:media(lista_notas)})

    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo, 'C:\projetos\python\digitalInovation\__pycache__')

def mover_arquivo(nome_arquivo):
    shutil.move(nome_arquivo, 'C:\projetos\python\digitalInovation\__pycache__')

if __name__ == '__main__':
    print('')
    #mover_arquivo('notas.txt')
    #copia_arquivo('./notas.txt')
    # lista_media = mediasNotas('notas.txt')
    # print(lista_media)
    # mediasNotas('notas.txt')
    # aluno = "\nGabriel Gustavo, 7, 5, 5, 4"
    #escreverArquivo('notas.txt', aluno)
    #atualizaArquivo('notas.txt', aluno)
    #lerArquivo('teste.txt')