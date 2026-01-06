# abordagem normal
quadradosA = []

for x in range(1,6):
    quadradosA.append(x**2)

# list comprehension

quadradosB = [x**2 for x in range(1,6)]

nomes = ["Ana", "Bruno", "Alice", "Carlos"]
nomes_com_a = [n for n in nomes if n.startswith("A")]

print(nomes_com_a)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [i for i in numeros if i % 2 == 0]

print(pares)

# conversão de unidades Celsius para Fahrehneit
celsius = [0, 10, 20, 30, 40, 50]
fahrenheit = [c in celsius * 1.8 + 32 for c in celsius]
print(fahrenheit)

# contagem de caracteres
palavras = ["maçã", "banana", "cereja", "damasco"]
tamanhos = [len(t) for t in palavras]

print(tamanhos)