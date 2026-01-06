# funcoes lambda map e filter
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map (<funcao_lambda>, <iterador>)
# usando map para elevar cada elemento ao quadrado

quadrados = list(map(lambda x: x ** 2, lista))
print("Lista de quadrados: ", quadrados)

# filter (<funcao_lambda>, <iterador>)
# usando filter para obter apenas os numeros pares
pares = list(filter(lambda x: x % 2 == 0, quadrados))
print("Lista de numeros pares: ", pares)    

# exercicio #1
# filtrar palavras curtas: dada uma lista de palavras ["sol", "computador", "lua", "python", "mar"], usa filter()
# para criar uma lista que contenha apenas as palavras com mais de 3 caracteres.

palavras = ["sol", "computador", "lua", "python", "mar"]

palavras_compridas = list(filter(lambda p: len(p) > 3, palavras))
print("Palavras com mais de 3 caracteres: ", palavras_compridas)

# exercicio #2
# conversao de preços: tens uma lista de preços em euros [10, 50 ,100].
# usa map() para aplicar um desconto de 10% a cada preço, multiplicar por 0.9.
precos = [10, 50, 100]

desconto = list(map(lambda p: p * 0.9, precos))
print("Preços com desconto de 10%: ", desconto)