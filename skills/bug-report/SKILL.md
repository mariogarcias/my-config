---
name: bug-report
description: Writes a clear, reproducible bug report with severity, environment, steps, expected and actual result. Use when someone describes something broken, pastes an error or a failing test, or asks to "write a bug", "file an issue" or "report this".
---

# Bug report

Turn a vague "it doesn't work" into a report anyone can reproduce on the first try, without asking a single question.

## Steps

1. **Gather the facts first.** From the conversation, logs, failing tests or code, collect: what the user did, what they expected, what happened, where (app version, device, OS, user role, network), and how often it happens. If something essential is missing, ask for it (at most 3 questions). Never invent steps or versions.
2. **Write a title** that says what is wrong and where, in under 80 characters. Good: "Cancelled appointment still shows under Upcoming after pull to refresh". Bad: "Appointments bug".
3. **Pick the severity** by impact on users, not by how hard it is to fix:
   - **Critical:** data loss, a security or privacy issue, or the main flow is blocked for everyone.
   - **High:** a core feature fails with no workaround.
   - **Medium:** a feature fails but there is a workaround.
   - **Low:** cosmetic or a minor inconvenience.
4. **Write numbered steps** starting from a known state (signed in as which role, with what data). Each step is one action. Include the exact input values.
5. **Separate expected from actual.** Expected quotes the acceptance criterion when there is one. Actual includes the exact error text.
6. **Add evidence and remove personal data** from it: names, emails, phone numbers, addresses, tokens.
7. **Link it** to the story, the test case (for example QA-03) or the failing test, if known.

If the repository has `templates/bug-report.md` or a GitHub issue form for bugs, follow its fields and order instead of the format below.

## Output format

```markdown
## [Title]

**Severity:** High
**Environment:** App 1.4.0 (212), iPhone 15, iOS 18.1, customer account, Wi-Fi
**Reproducible:** always / sometimes (x of y) / once

### Steps to reproduce
1. ...
2. ...

### Expected result
...

### Actual result
...

### Evidence
...

### Notes
Related: KEY-?? / QA-??. First seen in: ...
```

## Rules

- One bug per report. If you find two problems, write two reports.
- Describe behavior, not a guess at the cause. A suspected cause goes under Notes, marked as a guess.
- Do not soften or exaggerate the severity.
