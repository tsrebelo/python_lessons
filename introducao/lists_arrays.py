frutas = ["maçã", "banana", "laranja"]
frutasN = []

print(frutas)

print(frutas[1])
print(frutas[2])

frutas[0] = "pera"

frutas.append("uva")
frutas.remove("laranja")
#frutas.insert(1, "melão")
#frutas.sort()
#frutas.count()

for i in frutas:
    if "n" in i:
        frutasN.append(i)
        
print(frutasN)