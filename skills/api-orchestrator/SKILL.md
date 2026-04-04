---
name: api-orchestrator
description: Strategy for managing complex API integrations, multi-step authentication flows, and error handling for external services.
version: 1.0.0
---

# API Orchestrator

This skill provides a structured approach to managing 3rd-party API integrations and complex service orchestrations.

## 🛠 Workflow

### 1. The API Audit
Before writing integration code, perform a deep search for:
- API Documentation (use `mcp_context7_query-docs` if available).
- Rate limits and quotas.
- Authentication requirements (JWT, OAuth2, API Keys).

### 2. Mocking & Simulation
- Always create a mock environment or use `JSON-Server` to simulate API responses before connecting to live services.
- Define expected success and error schemas.

### 3. The Resilience Layer
Implement standard error handling for all API calls:
- **Retries:** Exponential backoff for 5xx errors.
- **Timeouts:** Hard limits on all external requests.
- **Circuit Breakers:** Stop calling the API if failure rate exceeds 20%.

### 4. Secret Management
- **NEVER** hardcode API keys. 
- Use `.env` files (added to `.gitignore`) or system environment variables.
- When creating repositories, ensure secrets are never committed.
