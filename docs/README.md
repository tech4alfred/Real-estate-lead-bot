# Documentation Index — Real Estate Lead Bot

All approved foundational documents live here.

## Core Documents

| Document | Location | Purpose |
|----------|----------|---------|
| **PRD** | [../PRD.md](../PRD.md) *(still at root — move locally)* | Product Requirements — what we are building and why |
| **System Architecture (SAD)** | [architecture/System Architecture Document (SAD).md](./architecture/System%20Architecture%20Document%20(SAD).md) | Technical architecture, responsibilities, data flow |
| **Database & Data Model** | [database/Database & Data Model Specification.md](./database/Database%20%26%20Data%20Model%20Specification.md) | Schema, entities, relationships |
| **API Specification** | [api/API Specification.md](./api/API%20Specification.md) | Endpoints, contracts, validation |
| **n8n Workflow Spec** | [automation/n8n Workflow Specification.md](./automation/n8n%20Workflow%20Specification.md) | Automation workflows |
| **AI Specification** | [ai/AI Specification.md](./ai/AI%20Specification.md) | Intent, extraction, response rules |
| **UI/UX Specification** | [frontend/UI-UX Specification.md](./frontend/UI-UX%20Specification.md) | Screens, components, interactions |
| **Lead Qualification** | [qualification/LEAD_QUALIFICATION_SPEC.md](./qualification/LEAD_QUALIFICATION_SPEC.md) | Scoring rules & classification |
| **Testing Spec** | [testing/TESTING_SPEC.md](./testing/TESTING_SPEC.md) | Test strategy & scenarios |
| **Deployment Spec** | [deployment/DEPLOYMENT_SPEC.md](./deployment/DEPLOYMENT_SPEC.md) | Deployment & operations |
| **Development Setup** | [development/DEVELOPMENT_SETUP.md](./development/DEVELOPMENT_SETUP.md) | How to set up and develop |
| **Task Tracker** | [tasks/TASK.md](./tasks/TASK.md) | Project tasks & roadmap |

## How to Use These Documents

1. **Before coding** — Read the relevant document(s).
2. **Do not invent architecture** — Follow the contracts defined here.
3. **Keep changes focused** — Update the corresponding doc when behaviour changes.

These documents are the single source of truth for the product.

> **Note:** The original full `PRD.md` is still at the repository root. Move it locally with:
> ```bash
> git mv PRD.md docs/PRD.md
> ```
