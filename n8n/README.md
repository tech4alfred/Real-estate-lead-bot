# n8n Workflows — Real Estate Lead Bot

n8n is the workflow orchestration and automation layer.

## Responsibilities

- Trigger handling
- AI processing orchestration
- Lead qualification workflows
- Sales notifications
- Google Sheets synchronization
- Follow-up reminders
- Error handling

## Recommended Structure

```text
n8n/
│
├── workflows/
│   ├── lead-process-message.json
│   ├── lead-qualify.json
│   ├── lead-notify-sales.json
│   ├── followup-reminder.json
│   ├── sheet-sync-lead.json
│   └── error-handler.json
│
└── README.md
```

## Workflow Naming Convention

- `PRH-LEAD-PROCESS-MESSAGE`
- `PRH-LEAD-QUALIFY`
- `PRH-LEAD-NOTIFY-SALES`
- `PRH-FOLLOWUP-REMINDER`
- `PRH-SHEET-SYNC-LEAD`
- `PRH-ERROR-HANDLER`

See `docs/automation/n8n Workflow Specification.md`.
