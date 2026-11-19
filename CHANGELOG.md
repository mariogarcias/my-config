# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- **Credits** to Alfredo Hernández, whose `my-config` the original agents are adapted from, and his copyright notice in `LICENSE` as the MIT License requires.

## [1.0.0] — 2026-11-18

First public release.

### New
- **11 Claude Code agents** for the full product cycle: `product-backlog`, `qa-test-plan`, `feature-tdd`, `create-unittest`, `test-doubles`, `design-patterns`, `code-review`, `swift-docs`, `git-commit-messages`, `pr-description` and `release-notes`.
- **2 skills:** `acceptance-criteria` writes and reviews testable Given / When / Then criteria, and `bug-report` turns a vague problem into a reproducible report.
- **Claude Code plugin** `product-team-ai-toolkit`, installable in one command from the `mariogarcias` marketplace.
- **Product and QA templates** for user stories, test plans and bug reports, plus a pull request template.
- **Case study** of Marito Detailing, the iOS app the agents were built on, and a **walkthrough** that follows one feature through six agents.
- **Roadmap** and **security policy**.
- **CI** that validates every agent and skill and runs `shellcheck` on `install.sh` on each pull request.
- `install.sh --agents` installs only the agents and skills, without touching Homebrew or the shell.

### Changed
- The agents are project-agnostic: everything specific to a project (user roles, domain risks, commands, conventions) now comes from its `CLAUDE.md`. The Marito Detailing context lives in `examples/marito-detailing/CLAUDE.md`.
- Everything is in English.

### Fixed
- `install.sh` no longer overwrites your global `~/.claude/CLAUDE.md`, and it backs up any agent or skill it is about to replace.
- Added the `create-unittest` agent, which four other agents already delegated to.

[1.0.0]: https://github.com/mariogarcias/product-team-ai-toolkit/releases/tag/v1.0.0
