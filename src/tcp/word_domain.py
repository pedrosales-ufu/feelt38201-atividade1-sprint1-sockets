import re


def contar_palavras(texto: str) -> str:
    if not texto.strip():
        return "[!] Nenhuma palavra encontrada."

    palavras = re.findall(r"\b\w+\b", texto, re.UNICODE)
    return f"Total de palavras: {len(palavras)}"
