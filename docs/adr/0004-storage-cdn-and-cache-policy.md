# 4. Storage, CDN, and Cache Policy

Date: 2026-10-15  
Status: Accepted  

## Context
Educational media assets (SVG line art, WebP thumbnails, Uzbek phonics audio clips) must be delivered to young children with low latency (<100ms) and high availability across Uzbekistan. Under `11_SCALABILITY_AND_RELIABILITY.md`, application instances must remain completely stateless — no persistent media can be tied to local container filesystems in production.

## Decision
1. **Object Storage:** Use S3-compatible cloud object storage (e.g., Cloudflare R2, AWS S3, or self-hosted MinIO) via `django-storages`. In local development and automated CI, local filesystem storage (`MEDIA_ROOT`) is preserved.
2. **CDN Delivery:** Place a global CDN (Cloudflare or regional edge proxy) in front of the asset storage.
3. **Cache Policy:**
   - **Static & Media Assets:** Hashed/versioned files are served with `Cache-Control: public, max-age=31536000, immutable`.
   - **Catalog API:** Cached in Redis using versioned namespace keys (`bolajon:v{version}:catalog:...`). When content is published or updated, the version is bumped, instantly invalidating stale keys in $O(1)$ time without costly Redis `FLUSHALL`.
   - **Degradation / Fallback:** If Redis is disconnected, `apps.common.cache` catches exceptions and queries the database directly with warning logs, ensuring 100% catalog uptime for users.

## Consequences
- Application web pods can scale horizontally from 1 to 50+ instances without file sync issues.
- Bandwidth and server load are reduced by >90% as media is served from edge caches.
- Seamless disaster recovery and zero downtime during content updates.
