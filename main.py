from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return {'Hello':'Gabriel!!!'}

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):

    '''

    Endopoint que retorna lista de restaurantes da API da URL
    (Usar o comando [uvicorn main:app --reload], pegar o endereço IP fornecido para o servidor
    e colocar um /docs no final para ver o swaggers)

    :param restaurante:
    :return:
    '''

    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json()
        if restaurante is None:
            return {'Dados': dados_json}

        dados_restaurante = []
        for item in dados_json:
            if item['Company'] ==  restaurante:

                dados_restaurante.append({
                    "item:": item['Item'],
                    "price": item['price'],
                    "description": item['description']
                })
        return {'Restaurante': restaurante, 'Cardápio': dados_restaurante}

    else:
        print(f'O erro foi {response.status_code} - {response.text}')