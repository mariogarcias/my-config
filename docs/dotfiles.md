# My macOS setup (dotfiles)

Besides the agents, this repo holds the command-line setup I use every day.

## Install

```bash
./install.sh
source ~/.zshrc
```

Requires macOS and [Homebrew](https://brew.sh). It installs the tools in the `Brewfile` (`jq`, `eza`, `git`, `gh`) and adds the aliases below to your `~/.zshrc`.

## Aliases

| Alias | Command |
|---|---|
| `gst` | `git status` |
| `gl` | `git pull` |
| `gp` | `git push` |
| `ga` | `git add .` |
| `gc` | `git commit` |
| `ll` | `eza --long --icons --sort=type` |
| `cl` | `claude` |
