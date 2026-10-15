# 5. Background Worker and Asynchronous Task Strategy

Date: 2026-10-15  
Status: Accepted  

## Context
Per `AGENTS.md` and `11_SCALABILITY_AND_RELIABILITY.md`, premature introduction of complex distributed job queues (Celery, RabbitMQ, Kafka) increases infrastructure overhead, memory footprint, and deployment fragility. We must define the threshold, architecture, and reliability guarantees under which asynchronous background task processing is introduced.

## Decision
1. **MVP Phase (Current):** Synchronous execution within request-response cycles is strictly bounded. All game actions (session start, session complete, score recording, COPPA data export) execute in <25ms on PostgreSQL with indices. No background queue is required for the core MVP.
2. **Phase 2 Expansion (Trigger Criteria):** When any of the following features are introduced:
   - Bulk transcode of parent audio recordings or SVG generation.
   - External transactional email delivery (guardian account verification / password reset).
   - Nightly aggregated learning analytics generation across millions of child profiles.
3. **Queue Architecture Selection:**
   - Use **Celery** with **Redis** as the message broker (matching our existing Redis caching infrastructure to avoid adding RabbitMQ).
   - **Idempotency Guarantee:** All task payloads must include a UUID `idempotency_key` stored in Redis with a 24-hour TTL to prevent duplicate execution during network retries.
   - **Retry Policy:** Exponential backoff with jitter (`max_retries=5`, initial delay 2s, factor 2, max delay 60s).
   - **Dead-Letter Queue (DLQ) & Monitoring:** Failed tasks after maximum retries are routed to a `celery_dead_letter` queue and trigger high-priority alerts in Sentry.

## Consequences
- The MVP remains lean, single-container deployable, and easy to maintain.
- A standardized, production-tested roadmap is locked in for asynchronous workloads once the traffic thresholds are reached.
