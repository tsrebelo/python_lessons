
# Exercício 2: Lista de Compras

#Cria uma lista chamada compras com 3 produtos à tua escolha
#(por exemplo "pão", "leite", "maçãs"). Pede ao utilizador para introduzir
#um novo produto e adiciona-o à lista.
#Guarda numa variável o número total de produtos da lista.
#Mostra na consola uma frase formatada como esta:

#A tua lista de compras tem 4 produtos:
#pão, leite, maçãs, arroz.

#Dicas:
#Usa input() para ler o produto do utilizador.
#Para juntar os elementos da lista numa única frase podes usar
#", ".join(lista). Para formatação de strings podes usar f-strings:


import os

os.system('clear')

lista = ["pão", "leite", "maçã"]

produto = str(input("Adiciona um novo produto: "))

print("\nProduto adicionado com sucesso!\n")

lista.append(produto)

txt = f"A tua lista de compras tem {len(lista)} produtos:"
print(txt)

print(", ".join(lista))
