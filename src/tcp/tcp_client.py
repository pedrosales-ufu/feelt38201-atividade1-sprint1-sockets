from socket import * # Kurose 2.7.2.


def rodar_client(
    serverName: str = "localhost", serverPort: int = 1205 # Kurose 2.7.2.
) -> None:
    print("=== CONTADOR DE PALAVRAS (TCP) ===")

    try:
        # Cria o soquete do cliente: IPv4 (AF_INET) e TCP orientado a conexão (SOCK_STREAM)
        clientSocket = socket(AF_INET, SOCK_STREAM) # Kurose 2.7.2.
        # Inicia ativamente o Handshake de Três Vias para estabelecer a conexão TCP com o servidor
        clientSocket.connect((serverName, serverPort)) # Kurose 2.7.2.

        while True:
            try:
                texto = input("Digite o texto (ou 'sair'): ").strip()
            except (KeyboardInterrupt, EOFError):
                texto = "sair"

            if not texto:
                continue

            # Envia o comando de saída codificado e encerra o loop local
            if texto.lower() == "sair":
                clientSocket.send("SAIR".encode("utf-8")) # Kurose 2.7.2.
                break

            # Transmite os dados codificados em UTF-8 através do fluxo TCP estabelecido
            clientSocket.send(texto.encode("utf-8")) # Kurose 2.7.2.

            # Aguarda e lê até 2048 bytes da resposta enviada pelo servidor
            resposta_bytes = clientSocket.recv(2048) # Kurose 2.7.2.
            
            if not resposta_bytes:
                print("[!] O servidor encerrou a conexão.")
                break

            print(resposta_bytes.decode("utf-8") + "\n")

        # Fecha o soquete
        clientSocket.close() # Kurose 2.7.2.
        print("Conexão encerrada.")

    except (ConnectionRefusedError, error):
        print("[!] Não foi possível conectar ao servidor.")


if __name__ == "__main__":
    rodar_client()
