"""
Funções utilitárias compartilhadas
"""

import os
import re
from typing import List


def natural_key(filename: str) -> List:
    """
    Cria uma chave de ordenação natural para nomes de arquivo.
    Exemplo: ['arquivo', 1] para 'arquivo1'
    """
    base = os.path.basename(filename).lower()
    parts = re.split(r"(\d+)", base)
    return [int(p) if p.isdigit() else p for p in parts]


def format_duration(seconds: float) -> str:
    """
    Formata a duração em segundos para um formato legível.
    Exemplo: 65s -> "1m05s"
    """
    seconds_int = int(round(seconds))
    m, s = divmod(seconds_int, 60)
    if m > 0:
        return f"{m}m{s:02d}s"
    return f"{seconds_int}s"


def get_supported_files(directory: str, extensions: tuple) -> List[str]:
    """
    Lista arquivos com extensões suportadas em um diretório.
    Retorna ordenado por natural_key.
    """
    try:
        files = [
            os.path.join(directory, f)
            for f in os.listdir(directory)
            if f.lower().endswith(extensions) and not f.startswith('.')
        ]
        files.sort(key=natural_key)
        return files
    except FileNotFoundError:
        return []
