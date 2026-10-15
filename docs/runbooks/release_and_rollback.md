# Runbook: Release Checklist and Rollback Plan (BJ-117)

## 1. Release Pre-Flight Checklist
Before triggering any production deployment:

- [ ] **Git Working Tree Clean:** All commits pushed to `main` with Conventional Commits.
- [ ] **CI Pipeline Green:** GitHub Actions build, lint, and test jobs passed 100%.
- [ ] **Frontend Strict Validation:**
  ```bash
  cd frontend
  npm run build    # tsc -b && vite build (0 errors)
  npm test -- --run # 14/14 tests green
  ```
- [ ] **Backend Strict Validation:**
  ```bash
  cd backend
  flake8           # 0 lint errors
  pytest           # 21/21 tests green
  python manage.py spectacular --validate # OpenAPI schema valid
  ```
- [ ] **Database Migration Impact:**
  - Verify if migrations are backward-compatible (non-locking column additions).
  - Pre-deployment DB snapshot taken (`backup_db.ps1`).

---

## 2. Zero-Downtime Deployment Execution
1. **Pull and Build Containers:**
   ```bash
   docker compose pull
   docker compose build --no-cache
   ```
2. **Apply Migrations (Idempotent):**
   ```bash
   docker compose run --rm api python manage.py migrate
   ```
3. **Rolling Container Restart:**
   Restart API instances one at a time to ensure zero drop in service availability:
   ```bash
   docker compose up -d --no-deps --build api
   ```
4. **Post-Deployment Health Probe Verification:**
   ```bash
   curl -i https://api.bolajon.uz/api/v1/health/live/
   # Expected: HTTP 200 {"status": "alive"}
   curl -i https://api.bolajon.uz/api/v1/health/ready/
   # Expected: HTTP 200 {"status": "ready", "database": "connected"}
   ```

---

## 3. Rollback Procedure (Emergency Reversion)
If post-release monitoring detects elevated error rates (>1%), p99 latency > 200ms, or failed readiness probes:

### Immediate Action (< 3 minutes):
1. **Revert Docker Image / Release Tag:**
   ```bash
   docker tag bolajon-api:previous bolajon-api:latest
   docker compose up -d --no-deps api
   ```
2. **Rollback Database Migration (if applicable):**
   ```bash
   # Revert to migration before current release
   docker compose run --rm api python manage.py migrate <app_name> <previous_migration_number>
   ```
3. **Invalidate Cache:**
   ```bash
   docker compose run --rm api python -c "from apps.common.cache import invalidate_catalog_cache; invalidate_catalog_cache()"
   ```
4. **Verify Health:**
   Check `/api/v1/health/ready/` returns HTTP 200.
5. **Incident Report:** Post failure summary in `#devops-incidents` and initiate post-mortem analysis.
