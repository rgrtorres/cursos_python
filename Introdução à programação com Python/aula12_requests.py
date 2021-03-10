import requests

def retorna_dado_cep():
    cep = int(input("Informe o cep (apenas números): "))

    response = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))

    # print(response.status_code)

    # print(response.text)

    # print(response.json())

    dados_cep = response.json()
    print("/******************** INFORMAÇÕES DO CEP ********************/")
    print("Endereço: {}".format(dados_cep['logradouro']))
    print("Bairro: {}".format(dados_cep['bairro']))
    print("Cidade: {}".format(dados_cep['localidade']))
    print("/************************* FIM *****************************/")
    return dados_cep

def retorna_dados_pokemon(pokemon):
    response = requests.get('https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon))
    dados_pokemon = response.json()
    return dados_pokemon

def retorna_response(url):
    response = requests.get(url)
    return response.text


if __name__ == '__main__':
    response = retorna_response('http://globo.com')
    print(response)
    #retorna_dado_cep()
    # dados_pokemon = retorna_dados_pokemon('pikachu')
    # print(dados_pokemon['sprites']['front_shiny'])
