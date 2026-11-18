# Marito Detailing (detailingCar)

> Example project context. The agents in this repo read their project-specific knowledge from a file like this one. Copy it to the root of your project as `CLAUDE.md` and replace each section with your own.

## Product
iOS app to book at-home car detailing services (washing, paint, carpets, etc.). Customers sign up, register one or more vehicles with their details, book appointments, see what each package includes, and can view, cancel or reschedule their appointments. Operators have their own module (`Features/Operator`) to handle the appointments. The design is modern, inspired by Spotify and Uber.

## User roles
- **Customer:** signs up, registers vehicles, browses packages, books, cancels and reschedules appointments.
- **Operator:** sees and handles the appointments assigned to them.
A customer must never see or change another customer's data, and operator screens must not leak into the customer app. Role checks are enforced by RLS, not only by the UI.

## Stack
- Swift and SwiftUI, iOS 17.0 minimum
- Clean Architecture
- Backend: Supabase (supabase-swift 2.47.x): auth, database with RLS, realtime and Edge Functions (`supabase/functions/`)
- Tests: XCTest

## Structure
- `detailingCar/App/`: entry point
- `detailingCar/Core/`: Auth, Networking, Supabase, UI, Validation, Extensions
- `detailingCar/Features/`: Home, Registration, Authentication, Login, Operator
- `detailingCar/Resources/`: assets
- `detailingCarTests/`: mirrors the app structure (Core/, Features/)
- `database/`: SQL scripts (schema, customer and operator RLS, realtime, triggers, seed)
- `supabase/functions/`: Edge Functions (auth-login, auth-register, _shared)
- `Scripts/`: helper scripts

## Commands
- Scheme: `DetailingCar`. Targets: `DetailingCar` and `DetailingCarTests`
- Build: `xcodebuild -scheme DetailingCar -destination 'platform=iOS Simulator,name=iPhone 17' build`
- Tests: `xcodebuild test -scheme DetailingCar -destination 'platform=iOS Simulator,name=iPhone 17'`
- Single test class: add `-only-testing:DetailingCarTests/<Class>`

## Conventions
- camelCase for variables and functions, PascalCase for types
- Language for code comments, docs, commits and release notes: Spanish
- Respect the Clean Architecture layers: the UI never talks to Supabase directly
- Every new feature ships with unit tests, in the same path inside `detailingCarTests/`
- Use async/await for concurrency

## Domain risks
The agents check these on every story, test plan and review:
- Double booking of the same time slot or operator
- Cancelling or rescheduling an appointment in a state that does not allow it
- A customer with several vehicles: the appointment must go to the right vehicle
- Time zones and daylight saving changes
- Double taps or network retries that create duplicate appointments
- Offline, server error, empty response
- A customer trying to see another customer's data (RLS must stop it, not only the UI)
- Realtime subscriptions that must be cancelled when leaving the screen
- The price and contents shown for a package must match what gets booked

## Database and backend
- Every schema or RLS policy change goes in a new script in `database/`
- After any table change, check that customer and operator RLS policies are still correct
- Tables with realtime enabled are listed in `enable_appointments_realtime.sql`

## Rules
- Never commit `.env`, Supabase keys or tokens
- Never put the `service_role` key inside the app
- Run the tests before committing
- Do not change production code while writing tests: if there is a bug, report it

## Git and tickets
- Jira project: Marito-Detailing. Ticket key: `MARITO` (e.g. MARITO-123)
- All work has a Jira ticket
- Branches: `type/MARITO-123-short-description` (lowercase, hyphens, no accents)
  - Types: feature, fix, hotfix, refactor, test, docs, chore, db, release
  - Always branch from an up-to-date `main`, keep them short-lived, delete after merging
- Commits: `type: MARITO-123 description` (types: feat, fix, refactor, test, docs, chore, db; `db` is for `database/` or `supabase/`)
- PRs: title `MARITO-123 description`. Nothing goes straight to `main`; merge with squash
