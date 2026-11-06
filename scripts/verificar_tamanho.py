#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Verifica se nenhum arquivo do repositório passa do limite de tamanho.

Limite: 20 KB (20.480 bytes) por arquivo.

Uso:
    uv run scripts/verificar_tamanho.py
"""

import subprocess
import sys
from pathlib import Path

LIMITE_BYTES = 20 * 1024


def listar_arquivos() -> list[Path]:
    """Lista arquivos versionados e novos (não ignorados pelo .gitignore)."""
    saida = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        check=True,
        capture_output=True,
    ).stdout.decode()
    return [Path(p) for p in saida.split("\0") if p and Path(p).is_file()]


def main() -> int:
    grandes = []
    for arquivo in listar_arquivos():
        tamanho = arquivo.stat().st_size
        if tamanho > LIMITE_BYTES:
            grandes.append((arquivo, tamanho))

    if not grandes:
        print(f"OK: todos os arquivos têm até {LIMITE_BYTES} bytes (20 KB).")
        return 0

    print(f"ERRO: {len(grandes)} arquivo(s) acima de {LIMITE_BYTES} bytes (20 KB):")
    for arquivo, tamanho in sorted(grandes):
        print(f"  - {arquivo}: {tamanho} bytes ({tamanho / 1024:.1f} KB)")
    print("Divida esses arquivos em partes menores (veja o AGENTS.md).")
    return 1


if __name__ == "__main__":
    sys.exit(main())
