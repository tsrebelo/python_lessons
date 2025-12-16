import socket
import threading

HOST = "172.25.123.94"
PORT = 5000

def receber_mensagens(client_socket):
    while True:
        try:
            mensagem = client_socket.recv(1024).decode("utf-8")
            if not mensagem:
                break
            print(f"\nServidor: {mensagem}")
        except:
            break

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    print("[CONECTADO AO SERVIDOR]")
    print("Comandos disponíveis:")
    print("/nome SEU_NOME  -> altera o nome")
    print("/sair           -> sair do chat")

    thread_receber = threading.Thread(
        target=receber_mensagens,
        args=(client,)
    )
    thread_receber.start()

    while True:
        mensagem = input("Cliente: ")
        client.send(mensagem.encode("utf-8"))

        if mensagem.strip() == "/sair":
            break

    client.close()

if __name__ == "__main__":
    main()
