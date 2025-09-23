cubo = lambda a : a * a * a
print(cubo(3))

print("--------------------------------------")

intervalo = lambda : [print(i) for i in range(11)]
intervalo()

print("--------------------------------------")

thisdict = {
    "brand": "BMW",
    "model": "M4",
    "year": 2013
}

for key in thisdict:
    print(key)

print("--------------------------------------")