#!/usr/bin/env bash
# Instala las herramientas, los aliases y los agentes de Claude Code.
# Uso: ./install.sh            todo
#      ./install.sh --agents   solo los agentes (no toca Homebrew ni ~/.zshrc)
set -euo pipefail
cd "$(dirname "$0")"

solo_agentes=false
[ "${1:-}" = "--agents" ] && solo_agentes=true

respaldar() {
  # Guarda una copia con fecha antes de reemplazar un archivo existente.
  if [ -f "$1" ] && ! cmp -s "$1" "$2"; then
    local copia
    copia="$1.respaldo-$(date +%Y%m%d-%H%M%S)"
    cp "$1" "$copia"
    echo "Copia de respaldo: $copia"
  fi
}

if [ "$solo_agentes" = false ]; then
  command -v brew >/dev/null || { echo "Instala Homebrew primero (https://brew.sh)"; exit 1; }
  brew bundle --file=Brewfile

  mkdir -p ~/.config
  cp config/aliases.zsh ~/.config/aliases.zsh
  grep -q "aliases.zsh" ~/.zshrc 2>/dev/null || echo 'source ~/.config/aliases.zsh' >> ~/.zshrc

  respaldar ~/.claude/CLAUDE.md claude/CLAUDE.md
  mkdir -p ~/.claude
  cp claude/CLAUDE.md ~/.claude/CLAUDE.md
fi

mkdir -p ~/.claude/agents
for agente in claude/agents/*.md; do
  destino=~/.claude/agents/$(basename "$agente")
  respaldar "$destino" "$agente"
  cp "$agente" "$destino"
done
echo "Agentes instalados en ~/.claude/agents/"

[ "$solo_agentes" = false ] && echo "Listo. Ejecuta: source ~/.zshrc"
exit 0
