#
# Jogo do Bingo só a parte de sortear os números
# 0-100 sortear sem repetir
# 
import random
import os

# Reset
RESET = "\033[0m"   

# Regular Colors
BLACK = "\033[0;30m"      
RED = "\033[0;31m"      
GREEN = "\033[0;32m"    
YELLOW = "\033[0;33m"    
BLUE = "\033[0;34m"     
PURPLE = "\033[0;35m"      
CYAN = "\033[0;36m"        
WHITE = "\033[0;37m" 

def mostrar_painel(numeros_sorteados):
    os.system('clear') 
    print(CYAN + "\nPainel de Números Sorteados:\n" + RESET)
    for i in range(1, 101):
        if i in numeros_sorteados:
            print(PURPLE + f"{i:3}", end=" " + RESET)
        else:
            print(PURPLE + "---", end=" " + RESET)
        if i % 10 == 0:
            print()
    print()

def main():
    numeros = list(range(1, 101))
    random.shuffle(numeros)
    numeros_sorteados = set()
    
    print(BLUE + "Bem-Vindo ao Jogo do Bingo!\n" + RESET)
    while len(numeros_sorteados) < 100:
        input("Prima ENTER para sortear o próximo número...")
        numero = numeros.pop()
        numeros_sorteados.add(numero)
        print(f"\nNúmero sorteado: {numero}\n")
        mostrar_painel(numeros_sorteados)

    print(YELLOW + "Todos os números foram sorteados! Fim do jogo." + RESET)
    
if __name__ == "__main__":    
    os.system('clear')      
    main()