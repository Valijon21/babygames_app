# 10 — Development Task Backlog

## Task formati
Har task uchun: ID, maqsad, dependency, acceptance criteria, test va deliverable. Agent tasklarni tartib bilan bajaradi. Bir sprintda juda ko‘p mustaqil qatlamni o‘zgartirmasin.

## EPIC E00 — Discovery
- [x] `BJ-001` MVP scope va out-of-scope hujjatini yakunlash. **AC:** must-have/must-not-have aniq.
- [x] `BJ-002` Yosh segmentlari va UX talablarini product owner bilan tasdiqlash. **AC:** har segment uchun 3+ dizayn qoidasi.
- [x] `BJ-003` Asset litsenziyasi va kontent provenance jadvalini yaratish. **AC:** har bir asset manbasi va ruxsati qayd etiladi.
- [x] `BJ-004` Architecture Decision Records (ADR) shabloni yaratish. **AC:** muhim texnik qarorlar qayd etiladi.

## EPIC E01 — Repository & engineering foundation
- [x] `BJ-010` Repository strukturasi va README yaratish.
- [x] `BJ-011` Frontend React/Vite/TypeScript strict setup.
- [x] `BJ-012` Frontend lint/format/typecheck/test scripts.
- [x] `BJ-013` Backend Django/DRF setup va app registry.
- [x] `BJ-014` PostgreSQL env konfiguratsiyasi.
- [x] `BJ-015` Docker Compose development muhiti.
- [x] `BJ-016` `.env.example`; secretlar gitignore’da.
- [x] `BJ-017` CI pipeline: lint, typecheck, tests, build.
- [x] `BJ-018` Backend health endpoint va structured error format.
- [x] `BJ-019` OpenAPI schema va API docs.
**AC:** clean checkoutdan hujjatdagi buyruqlar bilan ishga tushadi.

## EPIC E02 — Backend domain
- [x] `BJ-020` `GameCategory` modeli, migration, admin va test.
- [x] `BJ-021` `Game` modeli, status/difficulty/age validation.
- [x] `BJ-022` `GameAsset` modeli va metadata.
- [x] `BJ-023` Public categories endpoint.
- [x] `BJ-024` Published games list/detail endpoint.
- [x] `BJ-025` Katalog filter/search/pagination.
- [x] `BJ-026` Idempotent seed data command.
**AC:** draft kontent public API orqali chiqmaydi; filterlar testlangan.

## EPIC E03 — Frontend foundation & catalog
- [x] `BJ-030` Design tokens va global CSS.
- [x] `BJ-031` Button/Card/Modal/Toast/Loading/Error/Empty komponentlari.
- [x] `BJ-032` Router va app shell.
- [x] `BJ-033` API client va typed response/error.
- [x] `BJ-034` Home page.
- [x] `BJ-035` Category listing, filter va search.
- [x] `BJ-036` Game detail/launch page.
- [x] `BJ-037` Mobile/tablet/desktop responsive testlar.
**AC:** API bilan ishlaydi, mock data production code’da qolmaydi.

## EPIC E04 — Coloring
- [x] `BJ-040` SVG region asset schema va validatsiya.
- [x] `BJ-041` Coloring runtime interface.
- [x] `BJ-042` Rang palitrasi va active color.
- [x] `BJ-043` SVG region fill.
- [x] `BJ-044` Undo/redo history.
- [x] `BJ-045` Reset confirmation.
- [x] `BJ-046` PNG export.
- [x] `BJ-047` Touch/mouse/keyboard accessibility.
- [x] `BJ-048` 5 ta litsenziyasi tasdiqlangan demo rasm to‘plami.
- [x] `BJ-049` Coloring unit + E2E tests.
**AC:** asosiy bo‘yash jarayoni 360px mobil va desktopda ishlaydi; rasm assetlarida region IDlar unique.

## EPIC E05 — Alphabet
- [x] `BJ-050` Uzbek alphabet content schema va qoidalarini hujjatlashtirish.
- [x] `BJ-051` Harf kontent modeli/API.
- [x] `BJ-052` Harf kartalari va audio playback control.
- [x] `BJ-053` Harf izidan yozish prototipi.
- [x] `BJ-054` Harfni rasm/so‘zga moslashtirish o‘yini.
- [x] `BJ-055` Keyboard/touch accessibility va test.
**AC:** `O‘`, `G‘`, `Sh`, `Ch`, `Ng` kontenti izchil ko‘rsatiladi; audio mavjud bo‘lmasa fallback bor.

## EPIC E06 — Numbers & math
- [x] `BJ-060` Math task schema va difficulty rules.
- [x] `BJ-061` 1–10 sanash o‘yini.
- [x] `BJ-062` Raqam tanish va trace o‘yini.
- [x] `BJ-063` Ko‘p/kam va katta/kichik.
- [x] `BJ-064` Qo‘shish/ayirish task generatori yoki authoring flow.
- [x] `BJ-065` Javobni tekshirish va feedback.
- [x] `BJ-066` Math logic unit tests.
**AC:** tasodifiy tasklar takrorlansa ham valid; answer range va difficulty qoidalari tekshiriladi.

## EPIC E07 — Memory game
- [x] `BJ-070` Memory deck schema.
- [x] `BJ-071` Shuffle va matching logic pure functions.
- [x] `BJ-072` Kartalarni aylantirish UI.
- [x] `BJ-073` Difficulty va accessible feedback.
- [x] `BJ-074` Completion/result state.
**AC:** ikki marta bosish, tez bosish, qayta boshlash va juftlik tekshiruvi race-condition bermaydi.

## EPIC E08 — Sessions & progress
- [x] `BJ-080` GameSession model/API.
- [x] `BJ-081` Session start/complete endpointlari.
- [x] `BJ-082` Server-side payload validation.
- [x] `BJ-083` ProgressRecord upsert va constraints.
- [x] `BJ-084` Results screen va replay.
- [x] `BJ-085` Progress dashboard aggregate endpoint.
**AC:** takroriy complete requestlar progressni noto‘g‘ri ko‘paytirmaydi; ownership tekshiriladi.

## EPIC E09 — Parent accounts & child profiles
- [x] `BJ-090` Auth strategiyasini ADR orqali tanlash.
- [x] `BJ-091` Register/login/logout va throttling.
- [x] `BJ-092` ChildProfile CRUD.
- [x] `BJ-093` Object-level permissions.
- [x] `BJ-094` Parent dashboard.
- [x] `BJ-095` Profilni eksport/o‘chirish siyosati va test.
**AC:** boshqa account bola profiliga kira olmaydi; ma’lumot o‘chirish jarayoni hujjatlashtirilgan.

## EPIC E10 — Content admin
- [x] `BJ-100` Django Admin category/game konfiguratsiyasi.
- [x] `BJ-101` Draft/review/published workflow.
- [x] `BJ-102` Asset upload size/type validation.
- [x] `BJ-103` Preview va content version.
- [x] `BJ-104` Audit eventlar.
**AC:** draft noto‘g‘ri tasodifan nashr bo‘lmaydi; upload testlari o‘tadi.

## EPIC E11 — Security, accessibility & release
- [x] `BJ-110` Security checklist va dependency audit.
- [x] `BJ-111` WCAG asosiy tekshiruvlar.
- [x] `BJ-112` Performance budget va Lighthouse baseline.
- [x] `BJ-113` Production settings, HTTPS, CORS/CSRF.
- [x] `BJ-114` Backup/restore runbook.
- [x] `BJ-115` E2E smoke tests.
- [x] `BJ-116` Pilot feedback va bug triage.
- [x] `BJ-117` Release checklist va rollback plan.
**AC:** critical/high buglar yopilgan; deploy/rollback qadamlari hujjatlangan.

## EPIC E12 — Scalability & reliability baseline
- [x] `BJ-120` Domen boundary va dependency qoidalarini hujjatlashtirish. **AC:** applararo bog‘lanishlar va service interfaces yozilgan.
- [x] `BJ-121` Game content schema versioning va validation registry. **AC:** noto‘g‘ri yoki noma’lum schema publish bo‘lmaydi.
- [x] `BJ-122` API pagination, max page size va response-size limits. **AC:** katta query cheksiz response qaytarmaydi.
- [x] `BJ-123` Katalog query profiling, kerakli indekslar va N+1 test/review. **AC:** query plan va benchmark qayd etilgan.
- [x] `BJ-124` Structured logging, request ID va safe error reporting. **AC:** token va child PII loglarda yo‘q.
- [x] `BJ-125` Liveness/readiness health checks va deployment runbook. **AC:** readiness dependency muammosida trafik qabul qilmaydi.
- [x] `BJ-126` Rate limit, upload/payload limit va overload response. **AC:** endpointlar stress testda cheksiz resurs ishlatmaydi.
- [x] `BJ-127` Object storage/CDN integration decision va cache policy. **AC:** production assetlar app instance local diskiga bog‘liq emas.
- [x] `BJ-128` Cache key/version invalidation va Redis unavailable fallback. **AC:** stale content siyosati testlangan.
- [x] `BJ-129` Load/soak test scenariylari va baseline dashboard. **AC:** test report latency, error, CPU/RAM, DB va cache metrikalarini ko‘rsatadi.
- [x] `BJ-130` Backup restore drill va rollback runbook. **AC:** restore va rollback qadamlar amalda sinovdan o‘tgan.
- [x] `BJ-131` Queue/worker faqat real background workload talabiga ko‘ra ADR bilan qo‘shilsin. **AC:** retry, idempotency va failed-job monitoring mavjud.
**AC umumiy:** yangi o‘yin qo‘shish boshqa o‘yinlarni regressiya qildirmaydi; scalability/reliability qarorlari taxmin emas, test va metrikalar bilan tekshiriladi.

