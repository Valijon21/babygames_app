# 02 — System Architecture

## 1. Arxitektura tamoyillari
1. Avval modular monolith: bitta Django backend va bitta React frontend. MVPda microservice kerak emas.
2. Kontent ma’lumotlari bilan o‘yin mexanikasini ajratish.
3. API shartnomasi aniq, versiyalangan (`/api/v1/`).
4. Bolalar ma’lumotlari minimal va private-by-default.
5. O‘yinlar frontendda interaktiv ishlaydi; natija/progress APIga yoziladi.
6. Har bir muhim funksiyada loading, empty, error va success holatlari bo‘lsin.

## 2. Yuqori darajali komponentlar
- React SPA/PWA: sahifalar, o‘yin runtime, canvas, local draft state, API client.
- Django REST API: auth, profile, catalog, game content, session/progress, admin endpoints.
- PostgreSQL: akkauntlar, bola profillari, kontent metadata, sessiyalar va natijalar.
- Media storage: rasmlar, audio, preview thumbnaillar.
- Django Admin: ichki kontent boshqaruvi.
- Reverse proxy/web server: HTTPS, static/media routing va security headers.
- Optional Redis/Celery: keyinchalik audio processing, thumbnail, email kabi fon ishlar bo‘lsa.

## 3. Tavsiya etilgan repository
```text
bolajon/
  AGENTS.md
  README.md
  docs/
  frontend/
    src/
      app/
      pages/
      components/
      features/
        catalog/
        coloring/
        alphabet/
        numbers/
        memory/
        progress/
        parent/
      lib/
      hooks/
      types/
      styles/
    public/
    tests/
  backend/
    config/
    apps/
      common/
      accounts/
      child_profiles/
      catalog/
      game_content/
      game_sessions/
      progress/
    tests/
    manage.py
  infra/
    docker/
  .env.example
  docker-compose.yml
```

## 4. Frontend arxitekturasi
- React + Vite + TypeScript strict mode.
- Feature-based folder structure; har bir feature UI, API, types va testlarini yonma-yon saqlaydi.
- React Router — routing.
- TanStack Query yoki ekvivalent — server state/cache.
- React Hook Form + Zod — admin/parent form validatsiyasi (loyihaga mos bo‘lsa).
- Tailwind CSS va dizayn tokenlari.
- API client yagona joyda; komponentlar ichida takroriy `fetch` yozilmasin.
- O‘yin mexanikasi UI komponentidan ajratilsin; masalan, memory game state pure function sifatida test qilinadi.
- Bo‘yash uchun HTML Canvas/SVG tanlovi prototipdan keyin tasdiqlansin. MVPda SVG region-fill qulay; murakkab erkin chizish uchun Canvas. Har bir rasm uchun `viewBox`, region ID va kontent validatsiyasi bo‘lsin.
- Audio foydalanuvchi gesture’idan keyin ishga tushishi mumkin; autoplayga tayanilmasin.
- Responsive layout va reduced-motion sozlamasi qo‘llansin.

## 5. Backend arxitekturasi
Django apps:
- `common`: base models, pagination, error format, health endpoint.
- `accounts`: ota-ona/pedagog akkaunti va auth.
- `child_profiles`: ota-ona nazoratidagi bola profillari; bola alohida email talab qilmaydi.
- `catalog`: categories, games, age ranges, tags, publication state.
- `game_content`: coloring assets, alphabet items, math tasks, memory decks.
- `game_sessions`: session start/finish, score, duration va minimal telemetry.
- `progress`: foydalanuvchi/bola bo‘yicha progress summary.
- Django Admin: ichki operatorlar uchun; public admin endpointlari bilan aralashtirmang.

## 6. Auth va ruxsat
- Ota-ona akkaunti: email/password yoki tasdiqlangan mos auth usuli; parolni Django xavfsiz hash qiladi.
- JWT ishlatilsa access qisqa muddatli, refresh rotation/blacklist siyosati ko‘rib chiqilsin; tokenni `localStorage`da saqlash xavfi baholansin.
- Cookie auth tanlansa CSRF himoyasi sozlansin.
- Bola profili ota-ona akkauntiga bog‘langan; har requestda ownership tekshirilsin.
- Anonymous demo o‘yinlar bo‘lishi mumkin, ammo ular serverda shaxsiy profil yaratmasin.
- Admin uchun alohida role va kuchli autentifikatsiya.

## 7. API va xato formati
- `/api/v1/` versiyasi.
- JSON; ISO-8601 datetime UTC.
- Pagination: `{ "count": 0, "next": null, "previous": null, "results": [] }`.
- Xatolar: `{ "error": { "code": "VALIDATION_ERROR", "message": "Ma’lumotni tekshiring", "details": {} } }`.
- API schema OpenAPI/Swagger orqali generatsiya qilinadi.
- Query params serverda validate qilinadi.

## 8. Deployment
Development: Docker Compose (PostgreSQL, backend, frontend).
Production: HTTPS, secret manager/environment variables, managed PostgreSQL yoki backup nazoratidagi DB, object storage, monitoring va log rotation.
`DEBUG=False`, `ALLOWED_HOSTS`, CORS/CSRF origins aniq; productionda `*` ruxsat etilmaydi.


## 9. Scale va reliability talablari (majburiy)
Ushbu loyiha uchun `11_SCALABILITY_AND_RELIABILITY.md` arxitektura kontraktining bir qismi hisoblanadi. Yangi feature shu talablarga zid bo‘lmasligi kerak.
- Domenlar modular monolith ichida aniq ajratiladi; o‘yinlar mustaqil content schema va umumiy runtime/session kontraktidan foydalanadi.
- App stateless; static/media fayllar productionda object storage/CDN’da.
- Redis cache faqat cacheable published katalog/metadata uchun; private progress public cache qilinmaydi. Cache invalidation va fallback yoziladi.
- Pagination, query profiling, DB indekslar, timeout, upload/payload limit va endpoint throttling majburiy.
- Observability: structured logs, request ID, latency/error/DB/worker/cache metrikalari va alertlar.
- Release oldidan load test, smoke/E2E tests, backup restore va rollback reja. Konkret capacity faqat o‘lchov bilan tasdiqlanadi.
- Queue, read replica, microservices va boshqa murakkab infratuzilma faqat metrics va real ehtiyoj asosida qo‘shiladi.
