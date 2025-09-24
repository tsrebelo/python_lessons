#
# uma aplicação em python que consulte um api público e mostre os dados
#
# Sismos - https://api.ipma.pt/open-data/observation/seismic/{idArea}.json
#
import requests

def main():
    idLocalizacao = input("Escolha a região pretendida 3 - Arq. Açores | 7 - Continente, Arq. Madeira: ")
    
    if idLocalizacao == "3" or idLocalizacao == "7":
        url = f"https://api.ipma.pt/open-data/observation/seismic/{idArea}.json"
        response = requests.get(url)

        if response.status_code == 200:
            sismos_data = response.json()
            return sismos_data
        else:
            print(f"Erro ao obter dados: {response.status_code}")
            return None
    else:
        print("Input incorreto! Tente novamente.")
        return None

data = main()
if data:
    print("Dados sísmicos obtidos: ", data)
else:
    print("Falha ao obter dados.")
        
