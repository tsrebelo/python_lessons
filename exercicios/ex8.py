#
# uma aplicação em python que consulte um api público e mostre os dados
#

import requests
import json

def consultar_api():
    url = "https://official-joke-api.appspot.com/random_joke"
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            dados = resposta.json()
            return dados
        else:
            print(f"Erro na API: {resposta.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None

def mostrar_dados(dados):
    if dados:
        print("=== DADOS DA API ===")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
    else:
        print("Não foi possível obter os dados.")

if __name__ == "__main__":
    dados_api = consultar_api()
    mostrar_dados(dados_api)