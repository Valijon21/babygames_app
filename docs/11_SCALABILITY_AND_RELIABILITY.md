# 11 — Scalability, Performance & Reliability Architecture

## Maqsad
Yangi o‘yin yoki kategoriya qo‘shilganda mavjud o‘yinlarni buzmaslik; trafik oshganda tizimni gorizontal kengaytirish; sekin so‘rov, tashqi xizmat yoki bitta worker xatosi butun platformani to‘xtatmasligi. Hech bir arxitektura “hech qachon qotmaydi” deb kafolat bera olmaydi — bu talablar monitoring, yuklama sinovi va operatsion intizom bilan tekshiriladi.

## 1. Evolyutsion arxitektura
**Boshlanishi: modulga ajratilgan Django monolith.** Har bir domen alohida Django app, aniq ownership va public interface bilan ishlaydi. O‘yinlar backend ichida alohida plugin-like content/runtime contractga ega bo‘ladi, lekin har bir o‘yin uchun alohida server yoki Django app shart emas.

Tavsiya etilgan domen chegaralari:
- Identity & Guardian: akkaunt, auth, ota-ona ruxsati.
- Child Profiles & Privacy: bola profili va ma’lumot hayot sikli.
- Catalog & Publishing: kategoriya, o‘yin metadata, draft/review/publish.
- Game Content: versionlangan JSON/SVG/audio metadata va assetlar.
- Game Sessions & Progress: sessiya, natija, progress.
- Admin & Audit: ichki boshqaruv, audit izlari.
- Platform Infrastructure: cache, storage, telemetry, common error contracts.

Domenlar bir-birining private model/helper funksiyalariga to‘g‘ridan-to‘g‘ri bog‘lanmasin. Kerakli amallar service/interface qatlamidan o‘tsin. Biroq har bir model uchun ortiqcha abstraksiya yoki generic framework yaratilmang.

## 2. Yangi o‘yin qo‘shish kontrakti
Har bir o‘yin:
- `game_type`, `slug`, `content_version`, `schema_version`, age range, difficulty va locale metadata bilan ro‘yxatdan o‘tadi.
- O‘z kontent schema va validatsiyasiga ega bo‘ladi.
- Umumiy lifecycle’ga mos keladi: load → start → play → complete/reset → dispose.
- Natijani umumiy session contract orqali yuboradi; o‘yin-specific payload allowlist va size limit bilan tekshiriladi.
- Backendda yangi o‘yin qo‘shish mavjud API response yoki boshqa o‘yinlar schema’sini buzmasligi kerak.
- Feature flag yoki draft/published status orqali bosqichma-bosqich chiqarilishi mumkin.

Yangi o‘yinlar uchun umumiy katalog va session API saqlanadi. Maxsus server logic faqat real talab bo‘lsa qo‘shiladi. Kontent versiyalari bilan eski saqlangan sessiyalarni talqin qilish strategiyasi bo‘lsin.

## 3. Trafik va statik kontent
- Rasmlar, SVG, audio va boshqa katta assetlar Django worker orqali har so‘rovda uzatilmasin; productionda object storage + CDN ishlatilsin.
- Assetlar hash/version bilan nomlansin; uzoq cache muddati faqat immutable assetlar uchun.
- API JSON response’lari uchun `Cache-Control` siyosati endpointga qarab belgilanadi. Shaxsiy progress/child data public cache’ga tushmasin.
- Katalog va published game metadata uchun Redis cache key/version invalidation strategiyasi bo‘lsin; Redis ishlamay qolsa tizim xavfsiz tarzda DBga qayta olishi yoki cheklangan degraded mode’da ishlashi kerak.
- Pagination majburiy; barcha katalog yoki progressni cheksiz qaytarish taqiqlanadi.

## 4. Backend va database barqarorligi
- Productionda Django development server ishlatilmaydi; Gunicorn yoki mos production WSGI/ASGI server va reverse proxy ishlatiladi.
- App stateless bo‘lsin; session/local file’ga bog‘lanib qolmasin, shunda bir nechta app instance ishga tushirish mumkin.
- Worker/concurrency soni CPU/RAM va load test bilan belgilanadi, taxminiy defaultlar production qarori sifatida qabul qilinmaydi.
- DB connection limit va connection lifetime boshqarilsin; connection pooling faqat hosting/deployment topologiyasi bilan mosligi tekshirilganda qo‘shiladi.
- Querysetlarda N+1 muammosi tekshirilsin (`select_related`, `prefetch_related` kerak bo‘lgan joyda), kerakli indekslar query plan bilan tasdiqlansin.
- Transactionlar qisqa bo‘lsin; uzoq hisob-kitob yoki fayl ishlovi transaction ichida bajarilmasin.
- `statement_timeout`, request timeout va upload limitlar belgilanadi; timeoutlar real profiling asosida tanlanadi.
- DB migrationlar backward-compatible bosqichlarda bajarilsin: expand → deploy compatible code → migrate data → contract. Katta jadvalga bloklovchi migration release oldidan tekshirilsin.
- Backup va restore muntazam sinovdan o‘tkazilsin; backup mavjudligi restore ishlashini isbotlamaydi.

## 5. Fon vazifalari
MVPda request ichida tez bajariladigan ishlar bajarilishi mumkin. Quyidagilar ko‘payganda Celery + Redis/RabbitMQ yoki mos queue qo‘shish ko‘rib chiqiladi: thumbnail yaratish, media tekshirish, eksport, katta hisobotlar, bulk import, email kabi ishlar.
- Queue joblar idempotent bo‘lsin, retry/backoff va maksimal urinishga ega bo‘lsin.
- Dead-letter yoki failed-task monitoring bo‘lsin.
- Foydalanuvchi requesti fon job yakunlanishini kutib worker band qilib turmasin.
- Redis faqat cache va queue broker vazifasida ishlatilsa, durability va broker tanlovi alohida qaror qilinsin.

## 6. Rate limits va overload himoyasi
- Auth, session complete, search, artwork upload va admin endpointlar uchun alohida throttling.
- Request body, upload hajmi, pagination page size va payload uzunligiga limit.
- DB/queue/worker saturation kuzatilganda ortiqcha trafikni 429/503 bilan boshqarish; cheksiz navbatga qo‘ymaslik.
- Tashqi xizmatlar bo‘lsa timeout, retry limit, circuit breaker yoki fallback ishlatiladi.
- O‘yinlarning asosiy client-side interaktivligi API vaqtincha ishlamasa ham imkon qadar davom etsin; natija lokal navbatga yozilsa, sync va conflict qoidasi hujjatlashtirilsin. Offline sync MVPga kirmasa, muvaffaqiyatsiz natija yuborilishi foydalanuvchiga aniq ko‘rsatilsin.

## 7. Observability
- Structured logs: request ID/correlation ID, endpoint, status, latency; tokenlar va bola ma’lumotlari loglanmasin.
- Metrics: request rate, p50/p95/p99 latency, 4xx/5xx, CPU/RAM, worker saturation, DB connections/slow queries, cache hit ratio, queue depth/age, storage errors.
- Error tracking va alertlar: 5xx o‘sishi, DB connection exhaustion, queue backlog, disk/storage va backup xatolari.
- Health checks ajratilsin: liveness (process tirik), readiness (trafik qabul qilishga tayyor), dependency checks. Health endpoint secretlarni chiqarmasin.
- Har release oldidan dashboard va rollback mezonlari aniqlangan bo‘lsin.

## 8. Performance va reliability gates
Quyidagi raqamlar boshlang‘ich **maqsad**, real SLA va trafik profili pilot/load testdan keyin tasdiqlanadi:
- Oddiy katalog API p95 < 300–500 ms, warm cache va test muhitida.
- Muhim APIlar uchun 5xx < 1% normal yuklama ostida.
- Birinchi ekranda yirik assetlarni lazy-load qilish; o‘yin sahifasi kerak bo‘lmagan assetlarni oldindan yuklamaslik.
- Har bir release uchun smoke tests; asosiy flowlar uchun E2E.
- Har bir katta relizdan oldin kutilayotgan pikdan yuqori yuklamada load test va soak test.
- Yuklama sinovida latency, error rate, CPU/RAM, DB connection, cache va queue birgalikda tahlil qilinsin.
- Aniq concurrent user sonini load testdan oldin va infrastruktura ma’lum bo‘lmasdan va’da qilinmasin.

## 9. Scale-up va scale-out bosqichlari
1. **Stage A — MVP:** bitta production app deployment, managed yoki nazoratdagi PostgreSQL, object storage, basic monitoring, backup.
2. **Stage B — o‘sish:** CDN, Redis cache, query/index optimizatsiyasi, app instance’larni load balancer ortida gorizontal ko‘paytirish.
3. **Stage C — background workload:** queue va workerlarni web serverdan alohida scale qilish.
4. **Stage D — katta yuklama:** read replica yoki DB scaling faqat query/metrics isbotlaganda; connection pooler va partitioning faqat o‘lchov bilan asoslanganda.
5. **Stage E — selective service extraction:** faqat aniq domen mustaqil scale/release talab qilsa va modular boundarylar yetarli isbotlansa, masalan media processingni alohida service qilish. “Kelajakda kerak bo‘lishi mumkin” degan sababning o‘zi microservice uchun yetarli emas.

## 10. Qat’iy anti-patternlar
- Bitta ulkan React component yoki bitta `games.py` ichiga barcha o‘yinlar logikasini yig‘ish.
- Har bir requestda barcha o‘yinlar/assetlarni DBdan olish.
- Har bir rasm/audio faylini Django app diskida saqlash va instance’lar orasida umumiy disk bor deb taxmin qilish.
- Frontenddagi hidden buttonni ruxsat nazorati deb hisoblash.
- Test qilinmagan “auto-scale”ni barqarorlik kafolati sifatida taqdim etish.
- Barcha funksiyalarni microservice’ga ajratish va MVPni ortiqcha murakkablashtirish.
- Keshni invalidation strategiyasiz qo‘shish.
- Monitoring, backup restore va load testni launchdan keyinga qoldirish.
