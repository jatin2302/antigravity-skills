# Preferred Tech Stack & Implementation Rules
When generating code or UI components for this brand, you **MUST** strictly adhere to the following technology choices.

## Core Stack
* **Framework:** React 18+
* **Styling:** Tailwind CSS (no CSS-in-JS unless specified)
* **Icons:** Lucide React
* **Components:** Radix UI primitives

## Tailwind Usage
* Always use standard Tailwind utility classes.
* Avoid arbitrary values (e.g., `text-[#333]`)—use the tokens from `design-tokens.json` mapped to Tailwind's theme if possible.

## Forbidden Patterns
* Do not use Bootstrap or Material UI.
* Do not use inline styles unless for dynamic values.
