#def decoradorLog(funcao):
#    def wrapper(*args, **kwargs):
#        print(f"Chamada função '{funcao.__name__}' com os argumentos: {args}")
#        resultado = funcao(*args, **kwargs)
#        print("Operação concluída!")
#        return resultado
#    return wrapper
#
#@decoradorLog
#def soma(a, b):
#    return a+b
#    
#@decoradorLog
#def saudacao(nome, saudacao="Olá"):
#    print(f"{saudacao}, {nome}!")
#    
#print(soma(6, 4))
#saudacao("Maria", saudacao="Bom dia")
#
#
#def verificaAdmin(funcao):
#    def wrapper(*args, **kwargs):
#        if args and args[0] == "admin":
#            return funcao(*args, **kwargs)
#        else:
#            print("Acesso negado")
#    return wrapper
#        
#@verificaAdmin
#def acederAoSistema(utilizador):
#    print(f"Bem-vindo ao sistema, {utilizador}! Acedendo a dados secretos.")
#    
#acederAoSistema("admin")
#acederAoSistema("u1")

def colocarMaiusculas(funcao):
    def wrapper():
        resultado = funcao()
        return resultado.upper()
    return wrapper

@colocarMaiusculas
def hello():
    return "hello world"

print(hello())