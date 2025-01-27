import requests
import json
'''
    Estudo de consumo de API utilizando uma URL que leva a uma lista JSON que mostra
    restaurantes e seus devidos pratos
    
    Passos:

    1- Primeiro fornecemos uma url;
    2- Depois pediremos um código de status como resposta ao requisitarmos o acesso à lista JSON na URL
    3- Se o código de status dessa resposta for 200 (significando em ter 
    sucesso no retorno da resposta, entraremos no 'if';
    4- Esse if pegará os dados da lista JSON e irá iniciar um dicionário vazio;
    5- Faremos um 'for' para analisar a lista JSON em que cada vez que tiver um nome diferente
    de um restaurante (item['Company']), o 'for' passará para o próximo nome do restaurante e 
    adicionará os nomes dos restaurantes no dicionário;
    6- Cada vez que for adicionado um nome de um restaurante, o 'for' deve adicionar os pratos de 
    seus respectivos restaurantes antes de ir para o próximo nome na lista;
    7- Agora que o dicionário passou por todos os restaurantes e seus respectivos pratos, hora de usar
    comandos para serem criados arquivos com os nomes dos restaurantes (encontrados na pasta Restaurantes)
    e adicionar apenas os pratos de cada restaurante nos nomes dos arquivos que contém os nomes dos 
    restaurantes
    
'''

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []

        dados_restaurante[nome_restaurante].append({
            "item:": item['Item'],
            "price": item['price'],
            "description": item['description']
        })

else:
    print(f'O erro foi {response.status_code}')


for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        json.dump(dados, arquivo_restaurante, indent=4)

