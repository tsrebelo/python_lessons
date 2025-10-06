import os

os.system("clear")

class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    
    def printname(self):
        print(self.firstname, self.lastname)
        
class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

p1 = Person("John", "Olsen")
print("Class Pessoa:")
print(p1.firstname, p1.lastname)

s1 = Student("Mike", "Olsen")
print("\nClass Student:")
s1.printname()

print("--------------------------------")

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

        
c1 = Carro("BMW", "X3") #instanciar um objeto
print(c1.acelerar(250))