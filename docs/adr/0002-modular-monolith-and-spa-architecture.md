# 2. Modular Monolith Backend and SPA Frontend

Date: 2026-10-15  
Status: Accepted  

## Context
Bolajon is an educational game platform for children. In early and MVP stages, development velocity, transactional consistency, clear domain boundaries, and zero-overhead local deployment are essential. Premature microservices would introduce distributed transaction complexities, network latency, and operational burden.

## Decision
1. **Backend:** Modular monolith using Python 3.11+, Django 5+, and Django REST Framework. The application is logically partitioned into independent domain apps (`common`, `accounts`, `child_profiles`, `catalog`, `game_content`, `game_sessions`, `progress`).
2. **Frontend:** Single Page Application (SPA) using React 18+, TypeScript (strict mode), and Vite. Fast builds, strict typing, responsive layout, and isolated game engines.
3. **Database:** PostgreSQL for ACID compliance, relational integrity, JSONB support for versioned content payloads, and indexing.

## Consequences
- Fast development cycle, simple continuous integration and local deployment with Docker Compose.
- Easy to extract independent microservices in the future if a specific domain (such as real-time multi-tenant telemetry) demands separate horizontal scaling.
