#
# uma aplicação em python que consulte um api público e mostre os dados
#
# https://api.ipma.pt/open-data/observation/seismic/{idArea}.json 
# https://api.ipma.pt/open-data/sea-locations.json
#

import requests

def consultaIDLocadidade():

    url = "https://api.ipma.pt/open-data/sea-locations.json"
    
    try:
        resposta = requests.get(url)
        
        if resposta.status_code == 200:
            return resposta.json()
        else:
            print(f"Erro ao obter localizações: {resposta.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
        return None 

