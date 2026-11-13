#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"

command -v brew >/dev/null || { echo "Instala Homebrew primero (brew.sh)"; exit 1; }
brew bundle --file=Brewfile

mkdir -p ~/.config ~/.claude/agents
cp config/aliases.zsh ~/.config/aliases.zsh
grep -q "aliases.zsh" ~/.zshrc 2>/dev/null || echo 'source ~/.config/aliases.zsh' >> ~/.zshrc

[ -f claude/CLAUDE.md ] && cp claude/CLAUDE.md ~/.claude/CLAUDE.md
cp claude/agents/*.md ~/.claude/agents/ 2>/dev/null || true

echo "Listo. Ejecuta: source ~/.zshrc"
