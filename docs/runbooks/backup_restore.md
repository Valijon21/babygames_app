# Runbook: Database Backup and Disaster Recovery (BJ-114, BJ-130)

## 1. Overview & Service Level Objectives (SLO)
- **Target System:** PostgreSQL 18 production database (`bolajon_db`).
- **Recovery Point Objective (RPO):** < 24 hours (daily scheduled automated backups).
- **Recovery Time Objective (RTO):** < 30 minutes from disaster declaration to full service resumption.
- **Storage Location:** Backups are compressed, SHA-256 hashed, and uploaded to cold object storage with write-once-read-many (WORM) retention.

---

## 2. Automated Daily Backup Execution
Run the automated PowerShell backup script:
```powershell
.\scripts\backup_db.ps1 -DbName "bolajon_db" -BackupDir "backups" -RetentionDays 7
```

Or via direct PostgreSQL toolchain inside container:
```bash
docker exec -t bolajon-db pg_dump -U bolajon_user -d bolajon_db -Fc > backups/bolajon_db_$(date +%Y%m%d_%H%M%S).dump
```

---

## 3. Restore Drill Procedure (Step-by-Step)

### Step 1: Verify Integrity Checksum
```powershell
Get-FileHash -Path backups/bolajon_db_latest.dump -Algorithm SHA256
# Compare against .sha256 file
```

### Step 2: Stop Ingress Traffic
Prevent partial writes by setting maintenance mode on ingress or stopping the API pod:
```bash
docker compose stop api
```

### Step 3: Recreate Target Database
```bash
docker exec -i bolajon-db psql -U bolajon_user -d postgres -c "DROP DATABASE IF EXISTS bolajon_restore_drill;"
docker exec -i bolajon-db psql -U bolajon_user -d postgres -c "CREATE DATABASE bolajon_restore_drill OWNER bolajon_user;"
```

### Step 4: Execute Restoration
```bash
docker exec -i bolajon-db pg_restore -U bolajon_user -d bolajon_restore_drill --clean --if-exists --no-owner < backups/bolajon_db_latest.dump
```

### Step 5: Data Consistency Verification
Run validation checks on the restored database:
```sql
SELECT count(*) FROM catalog_game;
SELECT count(*) FROM child_profiles_childprofile;
SELECT count(*) FROM progress_progressrecord;
```

### Step 6: Resume Service Traffic
Switch environment database pointer to restored database and restart backend:
```bash
docker compose start api
curl -f http://localhost:8000/api/v1/health/ready/
```
Verification passes if `{"status": "ready", "database": "connected"}` is returned with HTTP 200.
