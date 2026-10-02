from datetime import datetime


def buscar_hora(text: str = "") -> str:

    agora = datetime.now()
    return f"Data: {agora.strftime('%d/%m/%Y')} | Hora: {agora.strftime('%H:%M:%S')}\n"
