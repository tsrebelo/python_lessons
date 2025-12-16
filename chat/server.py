import socket
import threading

HOST = "172.20.0.1"
PORT = 5000

clientes = {}
lock = threading.Lock()

def handle_client(client_socket, client_address):
    nome = f"{client_address}"
    with lock:
        clientes[client_socket] = nome

    print(f"[NOVA CONEXÃO] {nome}")

    while True:
        try:
            mensagem = client_socket.recv(1024).decode("utf-8")
            if not mensagem:
                break

            # Comando /sair
            if mensagem.strip() == "/sair":
                break

            # Comando /nome
            if mensagem.startswith("/nome "):
                novo_nome = mensagem[6:].strip()
                if novo_nome:
                    with lock:
                        clientes[client_socket] = novo_nome
                    nome = novo_nome
                    client_socket.send("Nome alterado com sucesso.".encode("utf-8"))
                continue

            print(f"[{nome}] {mensagem}")

            resposta = input("Servidor: ")
            client_socket.send(resposta.encode("utf-8"))

        except:
            break

    print(f"[DESCONECTADO] {nome}")
    with lock:
        del clientes[client_socket]
    client_socket.close()


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    print(f"[SERVIDOR ATIVO] A ouvir em {HOST}:{PORT}")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, client_address)
        )
        thread.start()


if __name__ == "__main__":
    main()
