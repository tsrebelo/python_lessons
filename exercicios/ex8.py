#
# uma aplicação em python que consulte um api público e mostre os dados
#
# Sismos - https://api.ipma.pt/open-data/observation/seismic/{idArea}.json
#
import requests
import os

os.system('clear')

def localizacao():
    id_loc = input("Escolha uma região 3 - Arq. Açores | 7 - Continente, Arq. Madeira: ")
    
    if id_loc == "3" or id_loc == "7":
        url = f"https://api.ipma.pt/open-data/observation/seismic/{id_loc}.json"
        response = requests.get(url)

        if response.status_code == 200:
            sismos_data = response.json()
            return sismos_data
        else:
            os.system('clear')
            print(f"Erro ao obter dados: {response.status_code}")
            return None
    else:
        os.system('clear')
        print("Região incorreta! Tente novamente.")
        return None

data = localizacao()
if data:
    os.system('clear')
    print("Dados sísmicos obtidos:\n\n", data)
else:
    print("Falha ao obter dados.")