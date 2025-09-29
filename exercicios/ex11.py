#
# Programa com uma função que recebe um dicionário
# e imprime no ecrã no seguinte formato:
#
# chave : valor

thisdict = {
    "brand": "BMW",
    "model": "X3",
    "year": 2000
}

for key in thisdict:
    print(key, ":", thisdict[key]) 