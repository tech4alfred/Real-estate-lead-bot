# Database — Real Estate Lead Bot

PostgreSQL is the **system of record**.

## Core Entities (planned)

- users
- roles
- leads
- conversations
- messages
- lead_scores
- lead_assignments
- follow_ups
- activities
- integration_syncs

## Structure

```text
database/
│
├── migrations/          # Alembic migrations (to be created)
├── seeds/               # Optional seed data
└── README.md
```

## Principles

- SQL is the authoritative source of truth.
- Google Sheets is secondary (operational / reporting only).
- Use Alembic for schema migrations.

See `docs/database/Database & Data Model Specification.md`.
