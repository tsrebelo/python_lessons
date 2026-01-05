def alertaDeEntrada(funcao_local):
    def wrapper():
        print("Atenção, movimento detetado!")
        funcao_local()
    return wrapper

# alerta = alertaDeEntrada

@alertaDeEntrada
def salaDeEstar():
    print("Alguém entrou na sala de estar")
    
@alertaDeEntrada
def quarto():
    print("Alguém entrou no quarto")
    
salaDeEstar()
quarto()
