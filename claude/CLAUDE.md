# Marito Detailing (detailingCar)

## Descripción
App iOS para reservar servicios de detailing de autos (lavado, pintura,
alfombras, etc.) a domicilio. Los clientes se registran, dan de alta varios
vehículos con sus características, agendan citas, ven qué incluye cada paquete
y pueden consultar, cancelar o cambiar sus citas. También hay un módulo
de operador (`Features/Operator`). El diseño es moderno, inspirado en
Spotify y Uber.

## Stack
- Swift y SwiftUI, iOS 17.0 mínimo
- Clean Architecture
- Backend: Supabase (supabase-swift 2.47.x): auth, base de datos, realtime
  y Edge Functions (`supabase/functions/`)
- Tests: XCTest

## Estructura
- `detailingCar/App/`: punto de entrada
- `detailingCar/Core/`: Auth, Networking, Supabase, UI, Validation, Extensions
- `detailingCar/Features/`: Home, Registration, Authentication, Login, Operator
- `detailingCar/Resources/`: assets
- `detailingCarTests/`: replica la estructura de la app (Core/, Features/)
- `database/`: scripts SQL (esquema, RLS cliente y operador, realtime, triggers, seed)
- `supabase/functions/`: Edge Functions (auth-login, auth-register, _shared)
- `Scripts/`: scripts de apoyo

## Comandos
- Esquema: `DetailingCar`. Targets: `DetailingCar` y `DetailingCarTests`
- Build: `xcodebuild -scheme DetailingCar -destination 'platform=iOS Simulator,name=iPhone 17' build`
- Tests: `xcodebuild test -scheme DetailingCar -destination 'platform=iOS Simulator,name=iPhone 17'`

## Convenciones
- camelCase para variables y funciones, PascalCase para tipos
- Comentarios en español
- Respetar las capas de Clean Architecture: la UI no habla directo con Supabase
- Toda feature nueva lleva tests unitarios, en la misma ruta dentro de `detailingCarTests/`
- Usar async/await para concurrencia

## Base de datos y Supabase
- Cada cambio de esquema o de políticas RLS va como script nuevo en `database/`
- Revisar que las políticas RLS de cliente y de operador sigan siendo correctas
  después de cualquier cambio en las tablas
- Las tablas con realtime activado están en `enable_appointments_realtime.sql`

## Reglas
- Nunca subir `.env`, claves de Supabase ni tokens al repo
- Nunca poner la `service_role` key dentro de la app
- Correr los tests antes de hacer commit
- No modificar código de producción al escribir tests: si hay un bug, reportarlo

## Jira y Git
- Proyecto de Jira: Marito-Detailing. Clave de tickets: MARITO (ej. MARITO-123)
- Todo trabajo tiene un ticket de Jira
- Ramas: `tipo/MARITO-123-descripcion-corta` (minúsculas, guiones, sin acentos)
  - Tipos: feature, fix, hotfix, refactor, test, docs, chore, db, release
  - Siempre salen de `main` actualizada, duran pocos días y se borran al fusionar
- Commits: `tipo: MARITO-123 descripción` en español (tipos: feat, fix, refactor, test, docs, chore, db)
- PRs: título `MARITO-123 descripción`. Nada se sube directo a `main`; se fusiona con squash merge
