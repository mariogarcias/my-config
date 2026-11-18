#!/usr/bin/env python3
"""Valida que cada agente en claude/agents/ tenga un frontmatter correcto.

Revisa que:
- el archivo empiece con un bloque --- ... --- válido;
- tenga `name` y `description`, y que `name` coincida con el nombre del archivo;
- `model`, si está, sea opus, sonnet, haiku o inherit;
- cada agente que se menciona con backticks en otros agentes exista.
"""
import pathlib
import re
import sys

CARPETA = pathlib.Path(__file__).resolve().parent.parent / "claude" / "agents"
MODELOS = {"opus", "sonnet", "haiku", "inherit"}


def leer_frontmatter(texto):
    if not texto.startswith("---\n"):
        return None
    fin = texto.find("\n---", 4)
    if fin == -1:
        return None
    campos = {}
    for linea in texto[4:fin].splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            campos[clave.strip()] = valor.strip()
    return campos


def main():
    errores = []
    agentes = sorted(CARPETA.glob("*.md"))
    nombres = {a.stem for a in agentes}
    if not agentes:
        errores.append(f"No hay agentes en {CARPETA}")

    for archivo in agentes:
        texto = archivo.read_text(encoding="utf-8")
        campos = leer_frontmatter(texto)
        if campos is None:
            errores.append(f"{archivo.name}: falta el frontmatter (--- ... ---)")
            continue
        for campo in ("name", "description"):
            if not campos.get(campo):
                errores.append(f"{archivo.name}: falta `{campo}`")
        if campos.get("name") and campos["name"] != archivo.stem:
            errores.append(f"{archivo.name}: `name` es '{campos['name']}', debería ser '{archivo.stem}'")
        modelo = campos.get("model")
        if modelo and modelo not in MODELOS:
            errores.append(f"{archivo.name}: `model: {modelo}` no es válido")
        for mencion in set(re.findall(r"\b([a-z]+(?:-[a-z]+)+)\b agent|agente ([a-z]+(?:-[a-z]+)+)", texto)):
            nombre = mencion[0] or mencion[1]
            if nombre not in nombres:
                errores.append(f"{archivo.name}: menciona al agente '{nombre}', que no existe")

    if errores:
        print("Errores encontrados:")
        for error in errores:
            print(f"  - {error}")
        return 1
    print(f"OK: {len(agentes)} agentes válidos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
