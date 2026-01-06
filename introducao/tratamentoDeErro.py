#try:
#    numero = int(input("Digite um número: "))
#    resultado = 10 / numero
#
#except ValueError:
#    print("Erro: Não é um número válido.")
#
#except ZeroDivisionError:
#    print("Erro: Divisão por zero não é permitida.")
#
#except Exception as e:
#    print(f"Ocorreu um erro inesperado: {e}")
#
#try:
#    entrada = float(input("Digite um número décimal: "))
#    print(f"O número digitado é: {entrada}")
#
#except ValueError:
#    print("Erro: Falha na conversão. O número inserido não é um décimal válido.")

frutas = {
    "maçã": 3.5,
    "banana": 2.00,
    "laranja": 4.00
}

try:
    fruta = input("Digite o nome da fruta: ")
    preco = frutas[fruta]
    print(f"O preço da {fruta} é {preco:.3f}€")

except KeyError:
    print("Erro: Não existe.")