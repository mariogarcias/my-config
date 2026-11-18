# Test plan template

> Used by the `qa-test-plan` agent. One plan per story, or one per release for regression.

## Test plan: [story or release]

**Story / release:** KEY-??
**Scope:** what is tested.
**Out of scope:** what is not, and why.
**Devices and OS versions:** [e.g. iPhone 15 on iOS 18, iPhone SE on iOS 17]

### Traceability matrix
| Acceptance criterion | Test cases |
|---|---|
| AC1: ... | QA-01, QA-02 |
| AC2: ... | QA-03 |

### Test cases

#### QA-01 [Title that describes the behavior]
- **Criterion:** AC1
- **Type:** functional / edge case / negative / permissions / regression / accessibility
- **Preconditions:** user role, data and app state
- **Steps:**
  1. ...
  2. ...
- **Expected result:** observable and unambiguous
- **Priority:** high / medium / low
- **Automatable:** yes (unit / UI) / no (reason)
- **Result:** ✅ pass / ❌ fail (bug link) / ⏭ blocked

### Handed to automation
- [Cases that become unit or UI tests]

### Exit checklist
- [ ] All high-priority cases pass
- [ ] No open high-severity bugs
- [ ] Unit and UI tests are green
- [ ] Database changes scripted and access policies tested with every role
- [ ] Release notes reflect what was actually tested
