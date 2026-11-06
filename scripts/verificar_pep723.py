#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Verifica se todos os scripts do repositório seguem a regra:
scripts em Python, com metadados PEP 723, executáveis com `uv run`.

Falha se encontrar:
- arquivo .py sem bloco PEP 723 (`# /// script` ... `# ///`);
- bloco PEP 723 com TOML inválido ou sem `requires-python`;
- scripts em outras linguagens (.sh, .bash, .ps1, .bat, .js etc.).

Uso:
    uv run scripts/verificar_pep723.py
"""

import re
import subprocess
import sys
import tomllib
from pathlib import Path

# Expressão regular de referência da própria PEP 723.
REGEX_BLOCO = re.compile(
    r"(?m)^# /// (?P<tipo>[a-zA-Z0-9-]+)$\s(?P<conteudo>(^#(| .*)$\s)+)^# ///$"
)

EXTENSOES_PROIBIDAS = {
    ".sh", ".bash", ".zsh", ".fish", ".ps1", ".bat", ".cmd",
    ".js", ".mjs", ".cjs", ".ts", ".rb", ".pl", ".php", ".r",
}


def listar_arquivos() -> list[Path]:
    saida = subprocess.run(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard", "-z"],
        check=True,
        capture_output=True,
    ).stdout.decode()
    return [Path(p) for p in saida.split("\0") if p and Path(p).is_file()]


def verificar_python(arquivo: Path) -> list[str]:
    texto = arquivo.read_text(encoding="utf-8")
    blocos = [m for m in REGEX_BLOCO.finditer(texto) if m["tipo"] == "script"]
    if not blocos:
        return ["sem bloco PEP 723 ('# /// script' ... '# ///')"]
    if len(blocos) > 1:
        return ["mais de um bloco '# /// script'"]

    conteudo = "".join(
        linha[2:] if linha.startswith("# ") else linha[1:]
        for linha in blocos[0]["conteudo"].splitlines(keepends=True)
    )
    try:
        metadados = tomllib.loads(conteudo)
    except tomllib.TOMLDecodeError as erro:
        return [f"TOML inválido no bloco PEP 723: {erro}"]

    if "requires-python" not in metadados:
        return ["bloco PEP 723 sem 'requires-python'"]
    return []


def main() -> int:
    problemas: list[str] = []
    total_py = 0
    for arquivo in listar_arquivos():
        sufixo = arquivo.suffix.lower()
        if sufixo in EXTENSOES_PROIBIDAS:
            problemas.append(
                f"{arquivo}: scripts devem ser em Python (PEP 723), não '{sufixo}'"
            )
        elif sufixo == ".py":
            total_py += 1
            problemas += [f"{arquivo}: {erro}" for erro in verificar_python(arquivo)]

    if not problemas:
        print(f"OK: {total_py} script(s) Python seguem a PEP 723.")
        return 0

    print(f"ERRO: {len(problemas)} problema(s) encontrado(s):")
    for problema in sorted(problemas):
        print(f"  - {problema}")
    print("Todo script deve ser Python com bloco PEP 723 e rodar com `uv run`.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
