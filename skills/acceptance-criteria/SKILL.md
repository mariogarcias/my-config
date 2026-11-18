---
name: acceptance-criteria
description: Writes or reviews acceptance criteria in Given / When / Then form so every criterion is testable. Use when a user story, ticket or feature request needs acceptance criteria, or when asked "is this story ready?", "write the AC" or "make these criteria testable".
---

# Acceptance criteria

Turn a story or feature request into acceptance criteria that a tester, a developer and a product owner would all read the same way, and that each map to at least one test.

## Steps

1. **Find the user and the outcome.** Identify the user role and what they can do when the story is done. If CLAUDE.md lists user roles, use those names. If the story serves two roles, write separate criteria for each, or suggest splitting the story.
2. **Write 3 to 6 criteria** in this form:
   > **Given** [the starting state], **when** [one action], **then** [an observable result].
   - One action per criterion. Two "when"s means two criteria.
   - The result must be observable from outside: something on screen, a saved record, a message, a notification. Never "the system handles it correctly".
3. **Cover the unhappy paths.** Add at least one criterion for an error or edge case. Check the domain risks in CLAUDE.md if they exist; otherwise consider invalid states, duplicates from repeated actions, empty data, offline, and one user reaching another user's data.
4. **Make every word measurable.** Replace vague words with numbers or concrete behavior:
   | Vague | Testable |
   |---|---|
   | fast | loads in under 2 seconds on 4G |
   | user-friendly | can be completed with VoiceOver |
   | shows an error | shows "That time slot is no longer available" and keeps the form filled |
   | recent | from the last 30 days |
5. **List what is out of scope**, so nobody tests or builds it by accident.
6. **Check each criterion** against the list below and fix the ones that fail.

## Quality checklist

- [ ] Each criterion has exactly one Given, one When and one Then (extra "and"s only for setup or for several results of the same action).
- [ ] Each Then can be verified by a test, manual or automated, with a clear pass or fail.
- [ ] No implementation details (no table names, endpoints or class names), unless the story is a technical task.
- [ ] At least one negative or edge-case criterion.
- [ ] No two criteria test the same thing.

## Output

Return the criteria as a numbered list (AC1, AC2...), then "Out of scope", then any open questions. When reviewing existing criteria, show each original next to its rewrite and say in one line what was wrong.

## Example

Story: *As a customer, I want to cancel an appointment so I don't pay for a service I no longer need.*

1. **AC1:** Given a confirmed appointment more than 24 hours away, when I cancel it, then its status changes to "Cancelled" and it no longer appears under "Upcoming".
2. **AC2:** Given an appointment less than 24 hours away, when I try to cancel it, then I see "Appointments can only be cancelled up to 24 hours before" and the appointment stays confirmed.
3. **AC3:** Given an appointment that is already completed, when I open it, then the cancel option is not shown.
4. **AC4:** Given I tap "Cancel" twice quickly, when the request finishes, then the appointment is cancelled once and I see one confirmation.

Out of scope: refunds, cancellation by the operator.
