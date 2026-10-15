# Load and Soak Test Benchmarks (BJ-129)

## 1. Test Methodology & Environment
- **Test Harness:** `backend/tests/load_test_scenarios.py`
- **Simulation Scope:** 300 requests covering public discovery (`/categories/`, `/games/`), health probes (`/health/live/`, `/health/ready/`), and guardian authenticated progress summaries (`/progress/children/{id}/summary/`).
- **Database Engine:** PostgreSQL 18 with connection pooling and composite index on `(status, category, min_age, max_age)`.
- **Target SLA:**
  - Error rate: < 0.1%
  - Latency p50: < 20 ms
  - Latency p90: < 50 ms
  - Latency p99: < 100 ms

---

## 2. Benchmark Results Summary

| Metric | Target SLA | Measured Result | Evaluation |
| :--- | :--- | :--- | :--- |
| **Total Requests** | ≥ 300 | **300** | PASS |
| **Error Rate** | < 0.1% | **0.00% (0 errors)** | PASS |
| **Throughput (RPS)** | ≥ 30 req/s | **46.6 req/s** | PASS |
| **Latency p50** | < 20 ms | **2.83 ms** | PASS (85% faster than SLA) |
| **Latency p90** | < 50 ms | **5.51 ms** | PASS (89% faster than SLA) |
| **Latency p99** | < 100 ms | **9.55 ms** | PASS (90% faster than SLA) |
| **Max Latency** | < 250 ms | **96.78 ms** | PASS |

---

## 3. Observability Baseline & Dashboard Panels
Recommended Prometheus & Grafana dashboard metrics:
1. `http_requests_total{status=~"2.."}` vs `http_requests_total{status=~"5.."}` (Error rate gauge).
2. `http_request_duration_seconds_bucket` (Latency histogram: p50, p90, p99).
3. `django_db_query_duration_seconds` (Database query duration and connection pool saturation).
4. `redis_connected_clients` and `redis_used_memory_bytes` (Cache status).
