# Runbook: Pilot Feedback and Bug Triage (BJ-116)

## 1. Pilot Program Scope
The pilot rollout targets:
- 50 families with children aged 2–7 across Uzbekistan.
- 3 preschool educational centers in Tashkent and Samarkand.
- Testing across mobile (Android / iOS), low-cost tablets, and desktop browsers.

---

## 2. Bug Severity Matrix & SLAs

| Severity | Definition | Examples | SLA for Fix |
| :--- | :--- | :--- | :--- |
| **P0 — Blocker** | Safety or crash bug affecting all users; parental gate bypass; COPPA/GDPR leak. | Math gate returns correct for invalid answer; app freezes on game launch. | **< 4 hours** |
| **P1 — High** | Core game mechanic broken on specific devices or resolutions; audio failure. | Tracing canvas unresponsive on Samsung Galaxy Tab A7; counting counter skips numbers. | **< 24 hours** |
| **P2 — Medium** | Cosmetic or localization discrepancy that does not impede gameplay. | Uzbek Latin character accent display quirk (`O‘` vs `O'`); minor button padding mismatch. | **Next release cycle** |
| **P3 — Low** | Feature requests, nice-to-have additions. | Request for extra animal coloring templates; dark mode for parent dashboard. | **Backlog triage** |

---

## 3. Feedback Intake & Child Privacy Rules
- **Rule 1 (Zero Child PII):** Feedback forms must NEVER ask for children's names, photos, or birthdates. Only guardian contact email and general age band (`2-3`, `4-5`, `6-7`) are collected.
- **Rule 2 (Telemetry Correlation):** Bug reports include the anonymous `X-Request-ID` from response headers to correlate server logs without exposing user data.
- **Rule 3 (Weekly Triage Cadence):** Every Monday 10:00 AM UZT, the core engineering team reviews incoming issues and assigns them into GitHub Milestones.
