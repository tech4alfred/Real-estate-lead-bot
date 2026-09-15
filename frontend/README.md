# Frontend — Real Estate Lead Bot

React application for:

- Customer chat interface
- Lead capture
- Sales dashboard
- Follow-up management

## Recommended Structure

```text
frontend/
│
├── src/
│   ├── components/
│   │   ├── ui/
│   │   ├── chat/
│   │   ├── leads/
│   │   ├── dashboard/
│   │   └── followups/
│   │
│   ├── pages/
│   │   ├── customer/
│   │   ├── auth/
│   │   └── dashboard/
│   │
│   ├── services/
│   ├── hooks/
│   ├── types/
│   ├── utils/
│   └── app/
│
├── package.json
└── README.md
```

## Principles

- React handles **UI only**.
- No business rules, scoring, or direct database access.
- All communication goes through the FastAPI backend.

See `docs/frontend/UI-UX Specification.md` and `docs/development/DEVELOPMENT_SETUP.md` for details.
