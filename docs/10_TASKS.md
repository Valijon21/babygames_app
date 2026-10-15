# 10 — Development Task Backlog

## Task formati
Har task uchun: ID, maqsad, dependency, acceptance criteria, test va deliverable. Agent tasklarni tartib bilan bajaradi. Bir sprintda juda ko‘p mustaqil qatlamni o‘zgartirmasin.

## EPIC E00 — Discovery
- [ ] `BJ-001` MVP scope va out-of-scope hujjatini yakunlash. **AC:** must-have/must-not-have aniq.
- [ ] `BJ-002` Yosh segmentlari va UX talablarini product owner bilan tasdiqlash. **AC:** har segment uchun 3+ dizayn qoidasi.
- [ ] `BJ-003` Asset litsenziyasi va kontent provenance jadvalini yaratish. **AC:** har bir asset manbasi va ruxsati qayd etiladi.
- [ ] `BJ-004` Architecture Decision Records (ADR) shabloni yaratish. **AC:** muhim texnik qarorlar qayd etiladi.

## EPIC E01 — Repository & engineering foundation
- [ ] `BJ-010` Repository strukturasi va README yaratish.
- [ ] `BJ-011` Frontend React/Vite/TypeScript strict setup.
- [ ] `BJ-012` Frontend lint/format/typecheck/test scripts.
- [ ] `BJ-013` Backend Django/DRF setup va app registry.
- [ ] `BJ-014` PostgreSQL env konfiguratsiyasi.
- [ ] `BJ-015` Docker Compose development muhiti.
- [ ] `BJ-016` `.env.example`; secretlar gitignore’da.
- [ ] `BJ-017` CI pipeline: lint, typecheck, tests, build.
- [ ] `BJ-018` Backend health endpoint va structured error format.
- [ ] `BJ-019` OpenAPI schema va API docs.
**AC:** clean checkoutdan hujjatdagi buyruqlar bilan ishga tushadi.

## EPIC E02 — Backend domain
- [ ] `BJ-020` `GameCategory` modeli, migration, admin va test.
- [ ] `BJ-021` `Game` modeli, status/difficulty/age validation.
- [ ] `BJ-022` `GameAsset` modeli va metadata.
- [ ] `BJ-023` Public categories endpoint.
- [ ] `BJ-024` Published games list/detail endpoint.
- [ ] `BJ-025` Katalog filter/search/pagination.
- [ ] `BJ-026` Idempotent seed data command.
**AC:** draft kontent public API orqali chiqmaydi; filterlar testlangan.

## EPIC E03 — Frontend foundation & catalog
- [ ] `BJ-030` Design tokens va global CSS.
- [ ] `BJ-031` Button/Card/Modal/Toast/Loading/Error/Empty komponentlari.
- [ ] `BJ-032` Router va app shell.
- [ ] `BJ-033` API client va typed response/error.
- [ ] `BJ-034` Home page.
- [ ] `BJ-035` Category listing, filter va search.
- [ ] `BJ-036` Game detail/launch page.
- [ ] `BJ-037` Mobile/tablet/desktop responsive testlar.
**AC:** API bilan ishlaydi, mock data production code’da qolmaydi.

## EPIC E04 — Coloring
- [ ] `BJ-040` SVG region asset schema va validatsiya.
- [ ] `BJ-041` Coloring runtime interface.
- [ ] `BJ-042` Rang palitrasi va active color.
- [ ] `BJ-043` SVG region fill.
- [ ] `BJ-044` Undo/redo history.
- [ ] `BJ-045` Reset confirmation.
- [ ] `BJ-046` PNG export.
- [ ] `BJ-047` Touch/mouse/keyboard accessibility.
- [ ] `BJ-048` 5 ta litsenziyasi tasdiqlangan demo rasm.
- [ ] `BJ-049` Coloring unit + E2E tests.
**AC:** asosiy bo‘yash jarayoni 360px mobil va desktopda ishlaydi; rasm assetlarida region IDlar unique.

## EPIC E05 — Alphabet
- [ ] `BJ-050` Uzbek alphabet content schema va qoidalarini hujjatlashtirish.
- [ ] `BJ-051` Harf kontent modeli/API.
- [ ] `BJ-052` Harf kartalari va audio playback control.
- [ ] `BJ-053` Harf izidan yozish prototipi.
- [ ] `BJ-054` Harfni rasm/so‘zga moslashtirish o‘yini.
- [ ] `BJ-055` Keyboard/touch accessibility va test.
**AC:** `O‘`, `G‘`, `Sh`, `Ch`, `Ng` kontenti izchil ko‘rsatiladi; audio mavjud bo‘lmasa fallback bor.

## EPIC E06 — Numbers & math
- [ ] `BJ-060` Math task schema va difficulty rules.
- [ ] `BJ-061` 1–10 sanash o‘yini.
- [ ] `BJ-062` Raqam tanish va trace o‘yini.
- [ ] `BJ-063` Ko‘p/kam va katta/kichik.
- [ ] `BJ-064` Qo‘shish/ayirish task generatori yoki authoring flow.
- [ ] `BJ-065` Javobni tekshirish va feedback.
- [ ] `BJ-066` Math logic unit tests.
**AC:** tasodifiy tasklar takrorlansa ham valid; answer range va difficulty qoidalari tekshiriladi.

## EPIC E07 — Memory game
- [ ] `BJ-070` Memory deck schema.
- [ ] `BJ-071` Shuffle va matching logic pure functions.
- [ ] `BJ-072` Kartalarni aylantirish UI.
- [ ] `BJ-073` Difficulty va accessible feedback.
- [ ] `BJ-074` Completion/result state.
**AC:** ikki marta bosish, tez bosish, qayta boshlash va juftlik tekshiruvi race-condition bermaydi.

## EPIC E08 — Sessions & progress
- [ ] `BJ-080` GameSession model/API.
- [ ] `BJ-081` Session start/complete endpointlari.
- [ ] `BJ-082` Server-side payload validation.
- [ ] `BJ-083` ProgressRecord upsert va constraints.
- [ ] `BJ-084` Results screen va replay.
- [ ] `BJ-085` Progress dashboard aggregate endpoint.
**AC:** takroriy complete requestlar progressni noto‘g‘ri ko‘paytirmaydi; ownership tekshiriladi.

## EPIC E09 — Parent accounts & child profiles
- [ ] `BJ-090` Auth strategiyasini ADR orqali tanlash.
- [ ] `BJ-091` Register/login/logout va throttling.
- [ ] `BJ-092` ChildProfile CRUD.
- [ ] `BJ-093` Object-level permissions.
- [ ] `BJ-094` Parent dashboard.
- [ ] `BJ-095` Profilni eksport/o‘chirish siyosati va test.
**AC:** boshqa account bola profiliga kira olmaydi; ma’lumot o‘chirish jarayoni hujjatlashtirilgan.

## EPIC E10 — Content admin
- [ ] `BJ-100` Django Admin category/game konfiguratsiyasi.
- [ ] `BJ-101` Draft/review/published workflow.
- [ ] `BJ-102` Asset upload size/type validation.
- [ ] `BJ-103` Preview va content version.
- [ ] `BJ-104` Audit eventlar.
**AC:** draft noto‘g‘ri tasodifan nashr bo‘lmaydi; upload testlari o‘tadi.

## EPIC E11 — Security, accessibility & release
- [ ] `BJ-110` Security checklist va dependency audit.
- [ ] `BJ-111` WCAG asosiy tekshiruvlar.
- [ ] `BJ-112` Performance budget va Lighthouse baseline.
- [ ] `BJ-113` Production settings, HTTPS, CORS/CSRF.
- [ ] `BJ-114` Backup/restore runbook.
- [ ] `BJ-115` E2E smoke tests.
- [ ] `BJ-116` Pilot feedback va bug triage.
- [ ] `BJ-117` Release checklist va rollback plan.
**AC:** critical/high buglar yopilgan; deploy/rollback qadamlari hujjatlangan.

## Agent bajarish protokoli
1. Birinchi ishda repozitoriy va barcha docsni o‘qish.
2. `git status`, mavjud kod, testlar va konfiguratsiyani tekshirish.
3. Task dependencylarini tekshirish; tayyor bo‘lmagan taskga o‘tmaslik.
4. Har safar bitta kichik task yoki mantiqiy kichik guruh.
5. Avval test/acceptance criteria, keyin implementatsiya, so‘ng test.
6. Eski API yoki UI kontraktini o‘zgartirishdan oldin impact tahlili.
7. Fayllarni o‘chirib yuborish, katta refactor yoki dependency almashtirishdan oldin sabab va xavfni yozish.
8. Har task yakunida o‘zgargan fayllar, test buyruqlari/natijasi, qolgan muammo va keyingi taskni hisobot qilish.


## EPIC E12 — Scalability & reliability baseline
- [ ] `BJ-120` Domen boundary va dependency qoidalarini hujjatlashtirish. **AC:** applararo bog‘lanishlar va service interfaces yozilgan.
- [ ] `BJ-121` Game content schema versioning va validation registry. **AC:** noto‘g‘ri yoki noma’lum schema publish bo‘lmaydi.
- [ ] `BJ-122` API pagination, max page size va response-size limits. **AC:** katta query cheksiz response qaytarmaydi.
- [ ] `BJ-123` Katalog query profiling, kerakli indekslar va N+1 test/review. **AC:** query plan va benchmark qayd etilgan.
- [ ] `BJ-124` Structured logging, request ID va safe error reporting. **AC:** token va child PII loglarda yo‘q.
- [ ] `BJ-125` Liveness/readiness health checks va deployment runbook. **AC:** readiness dependency muammosida trafik qabul qilmaydi.
- [ ] `BJ-126` Rate limit, upload/payload limit va overload response. **AC:** endpointlar stress testda cheksiz resurs ishlatmaydi.
- [ ] `BJ-127` Object storage/CDN integration decision va cache policy. **AC:** production assetlar app instance local diskiga bog‘liq emas.
- [ ] `BJ-128` Cache key/version invalidation va Redis unavailable fallback. **AC:** stale content siyosati testlangan.
- [ ] `BJ-129` Load/soak test scenariylari va baseline dashboard. **AC:** test report latency, error, CPU/RAM, DB va cache metrikalarini ko‘rsatadi.
- [ ] `BJ-130` Backup restore drill va rollback runbook. **AC:** restore va rollback qadamlar amalda sinovdan o‘tgan.
- [ ] `BJ-131` Queue/worker faqat real background workload talabiga ko‘ra ADR bilan qo‘shilsin. **AC:** retry, idempotency va failed-job monitoring mavjud.
**AC umumiy:** yangi o‘yin qo‘shish boshqa o‘yinlarni regressiya qildirmaydi; scalability/reliability qarorlari taxmin emas, test va metrikalar bilan tekshiriladi.
