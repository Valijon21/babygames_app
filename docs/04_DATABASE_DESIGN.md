# 04 — Database Design

## 1. Asosiy modellar
### Account
Django user modeli yoki custom user. Maydonlar: id, email/username, password hash (Django boshqaradi), is_active, created_at, updated_at. Keraksiz tug‘ilgan sana, telefon va manzilni majburiy yig‘mang.

### ChildProfile
- id (UUID)
- guardian (FK Account)
- display_name (taxallus bo‘lishi mumkin)
- birth_year yoki age_band (aniq tug‘ilgan sana o‘rniga yosh diapazoni afzal)
- avatar_key (oldindan belgilangan avatar)
- preferences (faqat whitelist qilingan sozlamalar)
- created_at, updated_at, is_active

### GameCategory
- id, slug unique, title, description, icon_key, sort_order, is_active

### Game
- id, category FK, slug unique, title, description, min_age, max_age, difficulty, thumbnail, estimated_minutes, status, content_version, created_at, updated_at
- published_at nullable
- `status` uchun choices; draft kontent public API orqali ko‘rinmasin.

### GameAsset
- id, game FK, asset_type (`svg`, `png`, `audio`, `json`), storage_key, alt_text, locale, metadata JSON, checksum, created_at
- upload MIME, size va haqiqiy fayl turi tekshiriladi.

### GameSession
- id UUID, child_profile FK nullable (anonymous demo uchun), game FK, started_at, completed_at nullable, duration_seconds, status, score nullable, result_summary JSON (faqat schema whitelist), content_version
- Har bir sessionni faqat egasi ko‘rishi mumkin.

### ProgressRecord
- id, child_profile FK, game FK, completed_count, best_score nullable, last_played_at, updated_at
- Unique constraint `(child_profile, game)`.

### ColoringArtwork (MVP+)
- id UUID, child_profile FK, game_asset FK nullable, title, storage_key yoki JSON vector representation, created_at, updated_at
- Private by default; public sharing yo‘q.

### AuditEvent
Faqat ota-ona/adminning muhim o‘zgarishlari uchun: actor, action, object_type, object_id, timestamp, safe metadata. Maxfiy qiymatlar loglanmaydi.

## 2. Munosabatlar
- Account 1:N ChildProfile.
- GameCategory 1:N Game.
- Game 1:N GameAsset.
- ChildProfile 1:N GameSession.
- ChildProfile 1:N ProgressRecord.
- Account/role orqali admin kontentni boshqaradi.

## 3. Indekslar va cheklovlar
- `Game.slug`, `GameCategory.slug`: unique.
- `Game(status, category_id, min_age, max_age)`: katalog filtrlari uchun indeks.
- `GameSession(child_profile_id, started_at)` va `(game_id, status)`.
- `ProgressRecord(child_profile_id, game_id)`: unique.
- `duration_seconds >= 0`, age ranges mantiqan to‘g‘ri, score chegaralari o‘yin turiga mos.
- FKlar uchun on-delete siyosati ongli tanlansin; progress tarixini tasodifan o‘chirib yubormaslik kerak.

## 4. Migration va ma’lumotlar
- Dastlabki kundan migrations commit qilinadi.
- Production DBni qo‘lda tahrirlash taqiqlanadi; migration review va backup bo‘lsin.
- Demo seed data idempotent management command orqali yaratiladi.
- Seedga real bolalar ma’lumotlari qo‘shilmaydi.
- JSON field erkin “hamma narsani shu yerga” joylash uchun emas; versionlangan va validatsiyalangan payload bo‘lsin.

## 5. Analytics
MVPda agregat, minimal metrikalar. Har bir pointer harakati, har bir harf yozish stroke’i yoki keraksiz batafsil xulq-atvorni yig‘mang. Analytics eventlari shaxsiy ma’lumotlarsiz va retention siyosati bilan.
