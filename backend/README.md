# Backend — Real Estate Lead Bot

FastAPI application responsible for:

- API endpoints
- Request validation
- Authentication & authorization
- Business logic
- Database access
- Lead / conversation / message management
- Integration boundary with n8n

## Recommended Structure

```text
backend/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── v1/
│   │       ├── auth.py
│   │       ├── leads.py
│   │       ├── conversations.py
│   │       ├── messages.py
│   │       ├── followups.py
│   │       └── health.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── repositories/
│   ├── core/
│   └── db/
│
├── tests/
├── requirements.txt
└── README.md
```

## Principles

- FastAPI is the application boundary.
- Deterministic business rules (scoring, state transitions, validation) live here.
- Heavy automation workflows belong in n8n.

See `docs/api/API Specification.md` and `docs/development/DEVELOPMENT_SETUP.md`.
