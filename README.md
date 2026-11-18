<div align="center">

# 🤖 Agentes de Claude Code: de la idea al release

**Un equipo de agentes de IA para producto y calidad:** backlog, historias de usuario, TDD, revisión de código, PRs y notas de versión. Probados en una app iOS real.

[![Validar](https://github.com/mariogarcias/my-config/actions/workflows/validar.yml/badge.svg)](https://github.com/mariogarcias/my-config/actions/workflows/validar.yml)
[![Claude Code](https://img.shields.io/badge/Claude_Code-agents-D97757?logo=anthropic&logoColor=white)](https://claude.com/claude-code)
[![Swift](https://img.shields.io/badge/Swift-SwiftUI-F05138?logo=swift&logoColor=white)](https://developer.apple.com/swift/)
[![Supabase](https://img.shields.io/badge/Supabase-backend-3ECF8E?logo=supabase&logoColor=white)](https://supabase.com)
[![macOS](https://img.shields.io/badge/macOS-setup-000000?logo=apple&logoColor=white)](#instalación)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

## ¿Qué es esto?

Es mi forma de llevar un producto de la idea a producción con IA, empaquetada para que cualquiera la instale en un minuto:

- **11 agentes de Claude Code** que cubren todo el ciclo: producto, TDD, pruebas, patrones de diseño, revisión, documentación, Git y releases.
- **Un `CLAUDE.md` de ejemplo** que muestra cómo dar contexto de proyecto a Claude (stack, arquitectura, convenciones y reglas de seguridad).
- **Mi setup de terminal en macOS**: herramientas con Homebrew y aliases.

Los uso a diario en **Marito Detailing**, mi app iOS para reservar servicios de detailing de autos a domicilio (SwiftUI, Clean Architecture, Supabase y XCTest).

## El flujo

```mermaid
flowchart LR
    A[💡 Idea] --> B[product-backlog]
    B --> C[feature-tdd]
    B --> Q[qa-test-plan]
    Q --> D
    C <--> D[create-unittest<br/>test-doubles]
    C <--> E[code-review]
    E -.-> F[design-patterns]
    C --> G[git-commit-messages]
    G --> H[pr-description]
    H --> I[release-notes]
    I --> J[🚀 App Store]
```

1. `product-backlog` convierte una idea en una historia de usuario con criterios de aceptación, y `qa-test-plan` la convierte en casos de prueba.
2. `feature-tdd` la construye con pruebas primero y commits pequeños.
3. `code-review` la revisa hasta que queda limpia.
4. `pr-description` prepara el Pull Request y `release-notes` resume la versión.

## Los agentes

| Etapa | Agente | Qué hace |
|---|---|---|
| Producto | [`product-backlog`](claude/agents/product-backlog.md) | Ordena el backlog, escribe historias con criterios de aceptación, parte las grandes y planea sprints |
| QA | [`qa-test-plan`](claude/agents/qa-test-plan.md) | Convierte criterios de aceptación en casos de prueba, decide qué se automatiza y arma el checklist de release |
| Desarrollo | [`feature-tdd`](claude/agents/feature-tdd.md) | Construye una feature completa con TDD (rojo, verde, refactor) y la pasa por revisión |
| Pruebas | [`create-unittest`](claude/agents/create-unittest.md) | Escribe y ajusta pruebas unitarias con XCTest |
| Pruebas | [`test-doubles`](claude/agents/test-doubles.md) | Diseña dobles de prueba (dummy, stub, fake, spy) y revisa su concurrencia |
| Diseño | [`design-patterns`](claude/agents/design-patterns.md) | Decide si un problema merece un patrón. "Ningún patrón" es una respuesta válida |
| Revisión | [`code-review`](claude/agents/code-review.md) | Revisión priorizada con foco en arquitectura, Supabase y seguridad. Solo lectura |
| Documentación | [`swift-docs`](claude/agents/swift-docs.md) | Documenta contratos para Quick Help de Xcode y borra comentarios que repiten el código |
| Git | [`git-commit-messages`](claude/agents/git-commit-messages.md) | Propone mensajes de commit atómicos con el ticket de Jira |
| Git | [`pr-description`](claude/agents/pr-description.md) | Redacta título, cuerpo y etiquetas del PR a partir del diff |
| Release | [`release-notes`](claude/agents/release-notes.md) | Escribe notas de versión para clientes y operadores |

### Decisiones de diseño

- **Cada agente tiene un solo trabajo** y delega en los demás (por ejemplo, `code-review` manda los hallazgos de diseño a `design-patterns`).
- **Permisos mínimos:** los agentes de revisión y de texto son de solo lectura; solo los que construyen pueden editar archivos.
- **El modelo según la tarea:** Opus para las decisiones difíciles (TDD, revisión, backlog) y Sonnet para la redacción.
- **Los agentes también se prueban:** en cada PR, un workflow de GitHub Actions valida que cada agente tenga un frontmatter correcto y que no mencione agentes que no existen, y pasa `shellcheck` sobre `install.sh`.

### Por especialidad

- **Producto:** `product-backlog` y `release-notes` traducen ideas en historias con criterios de aceptación y cambios técnicos en notas que entiende el cliente.
- **Calidad (QA):** `qa-test-plan`, `feature-tdd`, `create-unittest`, `test-doubles` y `code-review` aseguran que cada criterio de aceptación tenga una prueba y que nada llegue a `main` sin revisión.
- **Ingeniería:** `design-patterns`, `swift-docs`, `git-commit-messages` y `pr-description` mantienen el código y el historial limpios.

## Instalación

Requisitos: macOS, [Homebrew](https://brew.sh) y [Claude Code](https://claude.com/claude-code).

```bash
git clone https://github.com/mariogarcias/my-config.git ~/Developer/my-config
cd ~/Developer/my-config
./install.sh
source ~/.zshrc
```

`install.sh` instala lo del `Brewfile`, agrega los aliases a tu `~/.zshrc`, copia el `CLAUDE.md` a `~/.claude/` y los agentes a `~/.claude/agents/`. Antes de reemplazar un archivo que ya tienes, guarda una copia de respaldo con fecha junto a él.

### Solo quiero los agentes

```bash
./install.sh --agents
```

No toca Homebrew, tu `~/.zshrc` ni tu `CLAUDE.md`: solo copia los agentes a `~/.claude/agents/`, que es la carpeta global. Si los quieres solo en un proyecto, cópialos a su carpeta `.claude/agents/`:

```bash
mkdir -p .claude/agents
cp ~/Developer/my-config/claude/agents/*.md .claude/agents/
```

Luego abre Claude Code y escribe `/agents` para verlos.

### Adáptalos a tu proyecto

Los agentes leen el contexto del proyecto desde `CLAUDE.md`. Toma [`claude/CLAUDE.md`](claude/CLAUDE.md) como plantilla y cambia el stack, la estructura de carpetas, los comandos de build y tus convenciones de Git.

## Uso

```bash
claude                      # sesión normal: pide un agente por su nombre
claude --agent feature-tdd  # para que feature-tdd pueda delegar en otros agentes
```

Ejemplos:

```text
> usa product-backlog para escribir la historia "el cliente puede reprogramar su cita"
> usa code-review para revisar la rama actual antes del PR
> usa release-notes para las notas entre v1.2.0 y main
```

## Estructura

```
my-config/
├── Brewfile              # herramientas de línea de comandos
├── LICENSE               # MIT
├── install.sh            # instala herramientas, aliases y agentes
├── .github/workflows/    # CI: valida agentes e install.sh
├── scripts/
│   └── validar-agentes.py
├── config/
│   └── aliases.zsh       # aliases de Git y Claude Code
└── claude/
    ├── CLAUDE.md         # contexto de proyecto (plantilla)
    └── agents/           # los 11 agentes
```

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

## Sobre mí

Soy **Mario García**. Me especializo en **Product Management** y **QA**, con enfoque en el uso de IA. Uso agentes como estos para convertir ideas en historias de usuario claras, asegurar la calidad con pruebas y revisiones de código, y llevar cada feature hasta producción.

**Lo que aporto a un equipo**

- 🧭 **Producto:** backlog ordenado, historias con criterios de aceptación verificables, priorización y planeación de sprints.
- ✅ **Calidad:** estrategia de pruebas, TDD, casos límite pensados desde el inicio y revisiones de código con foco en seguridad.
- 🤖 **IA aplicada:** diseño agentes que automatizan el trabajo repetitivo del ciclo de producto sin perder el control humano.

Swift · SwiftUI · Clean Architecture · TDD · Supabase · Claude Code · Jira · GitHub Actions

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Mario_Garc%C3%ADa-0A66C2?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/mario-garc%C3%ADa-suarez-051b7a135)

¿Te sirvió algún agente? Deja una ⭐ o abre un issue con tus ideas.

## Licencia

[MIT](LICENSE). Úsalos, cópialos y adáptalos.
