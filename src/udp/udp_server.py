from socket import * # Kurose 2.7.1.
from time_domain import buscar_hora


def rodar_server(serverPort: int = 1205) -> None:
    # Cria o socket do servidor: AF_INET (IPv4) e SOCK_DGRAM (Protocolo UDP)
    serverSocket = socket(AF_INET, SOCK_DGRAM) # Kurose 2.7.1.

    # Vincula o socket: associa o socket ao "localhost" e à porta 1205
    serverSocket.bind(("localhost", serverPort)) # Kurose 2.7.1.

    print(f"\033[92m[Servidor UDP]\033[0m Ativo na porta {serverPort}...")

    try:
        while True:
            # Aguarda e lê o pacote: bloqueia até 1024 bytes e recebe a tupla (dados, (IP_origem, porta_origem))
            message, clientAddress = serverSocket.recvfrom(1024) # Kurose 2.7.1.

            # Decodifica a mensagem: converte o buffer de bytes recebido para string (UTF-8)
            resposta = buscar_hora(message.decode("utf-8"))

            # Envia a resposta: codifica a string em bytes e envia para o endereço de destino (clientAddress)
            serverSocket.sendto(resposta.encode("utf-8"), clientAddress) # Kurose 2.7.1.

    except KeyboardInterrupt:
        print("\n\033[91m[Servidor UDP]\033[0m Encerrado.")
    finally:
        # Encerra o socket: fecha a porta e libera os recursos no sistema operacional
        serverSocket.close() # Kurose 2.7.1.


if __name__ == "__main__":
    rodar_server()
