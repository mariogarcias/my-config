# my-config

Mi configuración de desarrollo para macOS y mis agentes de Claude Code para **Marito Detailing**, una app iOS para reservar servicios de detailing de autos a domicilio.

## Qué incluye

- **Herramientas** con Homebrew (`Brewfile`): `jq`, `eza`, `git` y `gh`.
- **Aliases de shell** para Git y para lanzar Claude Code.
- **`CLAUDE.md`** de Marito Detailing: contexto de la app para que Claude trabaje como yo quiero.
- **10 agentes de Claude Code** para el flujo de desarrollo, de la idea al release.

## Estructura

```
my-config/
├── Brewfile              # herramientas de línea de comandos
├── install.sh            # instala herramientas, aliases y agentes
├── config/
│   └── aliases.zsh       # aliases de Git y Claude Code
├── claude/
│   ├── CLAUDE.md         # contexto de Marito Detailing
│   ├── agents/           # agentes de Claude Code
│   └── skills/           # skills (por ahora vacío)
└── scripts/              # scripts propios (por ahora vacío)
```

## Instalación

Requisitos: macOS, [Homebrew](https://brew.sh) y [Claude Code](https://claude.com/claude-code).

```bash
git clone https://github.com/mariogarcias/my-config.git ~/Developer/my-config
cd ~/Developer/my-config
./install.sh
source ~/.zshrc
```

El script instala lo del `Brewfile`, copia los aliases a `~/.config/aliases.zsh`, los carga desde `~/.zshrc` y copia los agentes a `~/.claude/agents/`.

> Los agentes están escritos para Marito Detailing. Para usarlos solo en ese proyecto, cópialos a la carpeta `.claude/agents/` de la app en lugar de dejarlos en `~/.claude/agents/`, que es la carpeta global.

## Aliases

| Alias | Comando |
|---|---|
| `gst` | `git status` |
| `gl` | `git pull` |
| `gp` | `git push` |
| `ga` | `git add .` |
| `gc` | `git commit` |
| `ll` | `eza --long --icons --sort=type` |
| `cl` | `claude` |

## La app: Marito Detailing

App iOS con SwiftUI y Clean Architecture, iOS 17+, con Supabase como backend (autenticación, base de datos con RLS, realtime y Edge Functions) y pruebas con XCTest. Los clientes registran sus vehículos y agendan, consultan, cancelan o cambian citas a domicilio. Hay también un módulo para operadores.

## Agentes de Claude Code

Los agentes siguen el recorrido de una feature:

| Etapa | Agente | Qué hace |
|---|---|---|
| Producto | `product-backlog` | Ordena el backlog, escribe historias con criterios de aceptación, parte las grandes y planea sprints |
| Desarrollo | `feature-tdd` | Construye una feature completa con TDD, con commits pequeños y rondas de revisión |
| Pruebas | `create-unittest` | Escribe y ajusta pruebas unitarias con XCTest |
| Pruebas | `test-doubles` | Diseña dobles de prueba (dummy, stub, fake, spy) |
| Diseño | `design-patterns` | Decide si un problema merece un patrón de diseño. "Ningún patrón" es una respuesta válida |
| Revisión | `code-review` | Revisa cambios con foco en citas, cliente vs operador, Supabase y seguridad. Solo lectura |
| Documentación | `swift-docs` | Documenta contratos con comentarios de Quick Help y borra comentarios que repiten el código |
| Git | `git-commit-messages` | Propone mensajes de commit con el ticket de Jira |
| Git | `pr-description` | Redacta título, cuerpo y etiquetas del Pull Request |
| Release | `release-notes` | Escribe notas de versión para clientes y operadores |

### Cómo usarlos

Desde la carpeta de la app:

```bash
claude                      # sesión normal; pide un agente por su nombre
claude --agent feature-tdd  # para que feature-tdd pueda delegar en otros agentes
```

En una sesión, `/agents` muestra los que Claude Code reconoce.

Flujo típico: `product-backlog` convierte una idea en historia, `feature-tdd` la construye con pruebas, `code-review` la revisa, `pr-description` prepara el PR y `release-notes` resume la versión.

## Convenciones de Git y Jira

- Proyecto de Jira: Marito-Detailing. Clave de tickets: `MARITO`.
- **Ramas:** `tipo/MARITO-123-descripcion-corta`, en minúsculas y con guiones.
  Tipos: `feature`, `fix`, `hotfix`, `refactor`, `test`, `docs`, `chore`, `db`, `release`.
- **Commits:** `tipo: MARITO-123 descripción en español`.
  Tipos: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `db`.
- **PRs:** título `MARITO-123 descripción`. Nada se sube directo a `main`; se fusiona con squash merge.

## Reglas

- Nunca se suben `.env`, claves de Supabase ni tokens.
- La `service_role` key no va dentro de la app.
- Las pruebas se corren antes de cada commit.
- Cada cambio de esquema o de políticas RLS va como script nuevo en `database/` de la app.

## Pendiente

- Skills propios en `claude/skills/`.
- Más scripts de apoyo en `scripts/`.
