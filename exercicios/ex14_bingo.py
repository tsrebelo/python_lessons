#
# Jogo do Bingo só a parte de sortear os números
# 0-100 sortear sem repetir
# 
import random
import os

def mostrar_painel(numeros_sorteados):
    print("\nPainel de Números Sorteados:")
    for i in range(1, 101):
        if i in numeros_sorteados:
            print(f"{i:3}", end=" ")
        else:
            print("---", end=" ")
        if i % 10 == 0:
            print()
        print()

def main():
    numeros = list(range(1, 101))
    random.shuffle(numeros)
    numeros_sorteados = set()
    
    print("Bem-Vindo ao Jogo do Bingo!\n")
    while len(numeros_sorteados) < 100:
        input("Prima ENTER para sortear o próximo número...")
        numero = numeros.pop()
        numeros_sorteados.add(numero)
        print(f"\nNúmero sorteado: {numero}\n")
        mostrar_painel(numeros_sorteados)

    print("Todos os números foram sorteados! Fim do jogo.")
    
    if __name__ == "__main__":      
        main()