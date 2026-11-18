#!/usr/bin/env bash
# Installs the command-line tools, the shell aliases and the Claude Code agents.
# Usage: ./install.sh            everything
#        ./install.sh --agents   agents only (does not touch Homebrew or ~/.zshrc)
set -euo pipefail
cd "$(dirname "$0")"

agents_only=false
[ "${1:-}" = "--agents" ] && agents_only=true

backup() {
  # Saves a dated copy before replacing an existing file that differs.
  if [ -f "$1" ] && ! cmp -s "$1" "$2"; then
    local copy
    copy="$1.backup-$(date +%Y%m%d-%H%M%S)"
    cp "$1" "$copy"
    echo "Backup: $copy"
  fi
}

if [ "$agents_only" = false ]; then
  command -v brew >/dev/null || { echo "Install Homebrew first (https://brew.sh)"; exit 1; }
  brew bundle --file=Brewfile

  mkdir -p ~/.config
  cp config/aliases.zsh ~/.config/aliases.zsh
  grep -q "aliases.zsh" ~/.zshrc 2>/dev/null || echo 'source ~/.config/aliases.zsh' >> ~/.zshrc
fi

mkdir -p ~/.claude/agents
for agent in agents/*.md; do
  target=~/.claude/agents/$(basename "$agent")
  backup "$target" "$agent"
  cp "$agent" "$target"
done
echo "Agents installed in ~/.claude/agents/"

[ "$agents_only" = false ] && echo "Done. Run: source ~/.zshrc"
exit 0
