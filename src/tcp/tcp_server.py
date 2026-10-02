from socket import *
from word_domain import contar_palavras


def rodar_server(serverPort: int = 1205) -> None:
    # Cria o soquete de boas-vindas: IPv4 (AF_INET) e TCP orientado a conexão (SOCK_STREAM)
    serverSocket = socket(AF_INET, SOCK_STREAM) # Kurose 2.7.2.
    # Configura a opção SO_REUSEADDR para permitir a reutilização imediata do endereço e da porta local.
    serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    # Vincula o soquete: associa a porta local e ao localhost
    serverSocket.bind(("localhost", serverPort)) # Kurose 2.7.2.
    # Coloca o soquete em modo passivo de escuta para aguardar conexões de clientes
    serverSocket.listen(1) # Kurose 2.7.2.

    print(f"[Servidor TCP] Ativo na porta {serverPort}...")

    try:
        while True:
            # Aguarda a conexão e estabelece um novo soquete dedicado ao cliente após o 3-way handshake
            connectionSocket, addr = serverSocket.accept() # Kurose 2.7.2.
            print(f"[+] Cliente conectado: {addr}")

            try:
                while True:
                    # Lê até 2048 bytes do fluxo contínuo de dados (byte stream) do TCP
                    dados = connectionSocket.recv(2048) # Kurose 2.7.2.
                    if not dados:
                        break

                    mensagem = dados.decode("utf-8").strip()
                    if mensagem.upper() == "SAIR":
                        break

                    resposta = contar_palavras(mensagem)
                    # Codifica a resposta em UTF-8 e envia pelo soquete de conexão dedicado.
                    connectionSocket.send(resposta.encode("utf-8")) # Kurose 2.7.2.

            except Exception:
                print(f"[!] Erro ou desconexão abrupta do cliente {addr}.")
            finally:
                # Encerra o soquete
                connectionSocket.close() # Kurose 2.7.2.
                print(f"[-] Cliente {addr} desconectado.")

    except KeyboardInterrupt:
        print("\n[Servidor] Encerrado.")
    finally:
        serverSocket.close() # Kurose 2.7.2.


if __name__ == "__main__":
    rodar_server()
