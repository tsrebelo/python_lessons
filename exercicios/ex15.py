#
# Faz uma função que receba um set e dentro
# da função, um a um, os elementos do set são 
# transferidos para outro set
#
# setA = {1, 2, 3, 4, 5}
# setB = {}
# |
# V
# setA = {}
# setB = {1, 2, 3, 4, 5}
#

setA = {1, 2, 3, 4, 5}
setB = set()

def transferirSets(x):
    for x in range(len(setA)):
        numero = setA.pop()
        setB.add(numero)
    print(setA)
    print(setB)

if __name__ == "__main__":
    transferirSets(setA)