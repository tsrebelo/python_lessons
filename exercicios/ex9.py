#
# Programa onde é definido um tuplet com 4 valores
# e uma função que aceita como parâmetro um tuplet
# e que imprime no ecrã o seu conteúdo
#

carros = ("BMW", "Audi", "Honda", "Seat")

def marcas(x):
    for i in x:
        print(i)
        
marcas(carros)