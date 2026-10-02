from socket import * # Kurose 2.7.1.


def rodar_client(serverName: str = "localhost", serverPort: int = 1205) -> None:
    print("\033[96m=== SERVIDOR DE HORA CERTA (UDP) ===\033[0m")

    # Cria o socket: AF_INET (IPv4) e SOCK_DGRAM (UDP)
    clientSocket = socket(AF_INET, SOCK_DGRAM) # Kurose 2.7.1.

    clientSocket.settimeout(3.0)

    try:
        while True:
            print("\033[96m1. Pedir Hora | 2. Sair\033[0m")
            try:
                opcao = input("\033[96mEscolha: \033[0m").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n\033[92mAté logo!\033[0m")
                break

            if opcao == "2":
                print("\033[92mAté logo!\033[0m")
                break

            if opcao != "1":
                print("\033[91m[!] Opção inválida! Digite 1 ou 2.\033[0m\n")
                continue

            # Envia o pacote: transmite os bytes b"TIME_REQUEST"
            clientSocket.sendto(b"TIME_REQUEST", (serverName, serverPort)) # Kurose 2.7.1.

            try:
                # Bloqueia e recebe a resposta: aguarda até 1024 bytes
                modifiedMessage, serverAddress = clientSocket.recvfrom(1024) # Kurose 2.7.1.
                print(
                    f"\033[92m[✓]\n{modifiedMessage.decode('utf-8')}\033[0m\n" # Kurose 2.7.1.
                )
            except timeout:
                print(
                    "\033[91m[!] Erro: Tempo limite de resposta excedido.\033[0m\n"
                )

    except error as socket_err:
        print(f"\033[91m[!] Erro no socket UDP: {socket_err}\033[0m")
    finally:
        clientSocket.close() # Kurose 2.7.1.


if __name__ == "__main__":
    rodar_client()
