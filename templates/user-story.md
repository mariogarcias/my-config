# User story template

> Used by the `product-backlog` agent. Copy it into your tracker and fill every section. A story is ready for a sprint only when it meets the definition of ready at the bottom.

## KEY-?? Short, clear title

**As a** [user role]
**I want** [action]
**so that** [benefit].

**Value:** why this matters to the user or the business, in one line.

### Acceptance criteria
Each criterion must be verifiable by a test.

1. **Given** [context] **when** [action] **then** [observable result].
2. **Given** ... **when** ... **then** ...
3. **Given** ... **when** ... **then** ...

### Edge cases
- [What can go wrong: invalid state, duplicates, offline, permissions, time zones...]

### Details
| | |
|---|---|
| Touches the database | yes / no (which tables or access policies) |
| Dependencies | [stories that must come first] |
| Size | S / M / L (L must be split) |
| Suggested branch | `feature/KEY-??-short-description` |

### Out of scope
- [What this story explicitly does not cover]

---

**Definition of ready**
- [ ] Clear value and user role
- [ ] 3 to 6 testable acceptance criteria
- [ ] Edge cases listed
- [ ] Size S or M
- [ ] Dependencies identified
- [ ] No blocking open questions
