class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Carro:
    
    velocidadeMax = 240
    velocidadeAtual = 0
    
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def acelerar(self, velocidade):
        self.velocidadeAtual += velocidade
        if self.velocidadeAtual > self.velocidadeMax:
            self.velocidadeAtual = self.velocidadeMax
        return self.velocidadeAtual
        
c1 = Carro("BMW", "X3")
print(c1.acelerar(250))