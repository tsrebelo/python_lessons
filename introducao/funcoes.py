def repetir():
    i = 0
    while i < 10:
        print("Repetição", i)
        i += 1
    return
    
repetir()

print("---------------")

# Função com parametros
def repetirVezes(vezes):
    i = 0
    while i < vezes:
        print("Repetição", i)
        i += 1
    return

repetirVezes(5)

print("---------------")

# Funções de retorno

def somar(a, b):
    return a + b
resultado = somar(5, 3)
print("Resultado:", resultado)