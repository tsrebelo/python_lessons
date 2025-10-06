class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        print("O Construtor foi inicializado")
        
    def mostraMarca(self):
        print(self.marca)
        
    def mostraModelo(self):
        print(self.modelo)
        
c1 = Carro("BMW", "X3")
c1.mostraMarca()
c1.mostraModelo()