# Security policy

## Supported versions

| Version | Supported |
|---|---|
| 1.x | ✅ |

## Reporting a problem

If you find a security issue, for example an agent that could leak secrets, run destructive commands or skip a review step, please do not post it publicly. Send me a private message on [LinkedIn](https://www.linkedin.com/in/mario-garc%C3%ADa-suarez-051b7a135) with:

- what you found and which agent, skill or script it affects
- the steps to reproduce it
- what impact you think it has

I will reply within 7 days and credit you in the changelog once it is fixed, unless you prefer not to be named.

## How the toolkit limits risk

- Review and writing agents are read-only. Only the agents that build can edit files.
- `install.sh` never overwrites your global `~/.claude/CLAUDE.md` and backs up any agent or skill it replaces.
- CI validates every agent and skill and runs `shellcheck` on `install.sh` on every pull request.
