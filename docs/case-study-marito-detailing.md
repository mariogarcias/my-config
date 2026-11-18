# Case study: Marito Detailing

**At-home car detailing, booked from an iOS app.**
My role: product owner and QA lead, using AI agents across the whole delivery cycle.

---

## The product

Marito Detailing lets customers book car detailing services (washing, paint, carpets and more) that come to their home. Customers sign up, register one or more vehicles with their details, see exactly what each package includes, and book, cancel or reschedule appointments. Operators have their own module to see and handle the appointments assigned to them.

**Stack:** Swift and SwiftUI (iOS 17+), Clean Architecture, Supabase (auth, Postgres with row-level security, realtime and Edge Functions), XCTest.

## The problem

Booking a service at home has more ways to fail than it looks:

- Two customers can try to book the same time slot, or the same operator, at once.
- A customer with several cars needs the appointment tied to the right vehicle.
- Appointments move through states (pending, confirmed, in progress, completed, cancelled), and only some changes are valid.
- Customers and operators share the same data but must see very different slices of it.
- Time zones, daylight saving, flaky mobile networks and double taps can all create wrong or duplicate bookings.

Any of these reaches a real person waiting at home for a service that never shows up, or shows up twice.

## Key product decisions

**Two user roles, never mixed.** Every story is written for either the customer or the operator. If one serves both, it gets split. This keeps acceptance criteria testable and prevents operator features from leaking into the customer app.

**Security enforced by the backend, not the screen.** A customer must never see another customer's data. That rule is enforced with Supabase row-level security policies for each role, and every schema change ships as a new SQL script with its policies reviewed. The UI hiding something is never considered enough.

**Slice by value, not by layer.** Large stories are split into pieces a user can actually use ("see my appointments", then "cancel an appointment"), not into "database first, screen later". Every slice can be tested and shipped on its own.

**A shared list of domain risks.** Double booking, invalid state changes, wrong vehicle, time zones, duplicates from retries, offline states and cross-customer access are written down once, in the project context. Every story, test plan and code review checks against the same list.

## Quality strategy

- **Acceptance criteria first.** Each criterion is written in Given / When / Then form and must be verifiable by a test.
- **Traceability.** Every criterion maps to at least one test case, and every test case maps back to a criterion.
- **Test-driven development.** Business rules are written test-first. Tests never touch the real backend, the network or the system clock: collaborators are replaced with protocol-based test doubles, and time is injected.
- **Automate the rules, test the experience by hand.** Validations and business rules are always unit tests. Critical end-to-end flows are UI test candidates. Visuals, accessibility (VoiceOver, Dynamic Type, contrast) and device-specific behavior are tested manually, with a reason recorded for each.
- **Review before merge.** Nothing goes straight to `main`. Every change goes through a prioritized code review focused on data, security, concurrency and the booking rules before cosmetics.
- **Release regression.** Each release gets a risk-based regression of the features it touched, plus a smoke run with both roles.

**Definition of done:** acceptance criteria met with passing tests, code review with no blocking findings, test plan executed, database changes scripted with access policies reviewed, and a PR linked to its ticket.

## How AI fits in

I designed a team of [11 Claude Code agents](../README.md#the-agents) that mirror this process. Each one has a single job, the minimum permissions it needs, and hands off to the next:

1. `product-backlog` turns an idea into a story with acceptance criteria and edge cases.
2. `qa-test-plan` turns those criteria into test cases and decides what to automate.
3. `feature-tdd` builds the feature test-first, with `create-unittest` and `test-doubles` for the tests.
4. `code-review` reviews until no blocking findings remain, and sends design questions to `design-patterns`.
5. `git-commit-messages`, `pr-description` and `release-notes` keep the history and the communication clean.

The agents speed up the repetitive work. The decisions stay human: what to build, in what order, what risk is acceptable, and when a release is ready.

## Delivery process

- Every piece of work has a Jira ticket.
- Short-lived branches named `type/TICKET-description`, always from an up-to-date `main`.
- Small commits, one per layer or topic, in the format `type: TICKET description`.
- Pull requests with the ticket, why, use cases, how to test and database changes, merged with squash.
- Secrets never enter the repository, and the Supabase admin key never ships in the app.

## What I took away

- The most valuable quality work happens before any code: a clear, testable acceptance criterion prevents more bugs than any review.
- Writing the domain risks down once, and reusing them everywhere, keeps product, development and QA aligned.
- AI agents work best with narrow responsibilities, explicit handoffs and a human making the final call.
