# Bolajon Platformasi — Dastlabki Arxitektura va Repozitoriy Auditi

**Hujjat turi:** Tizim auditi va texnik inventarizatsiya  
**Rol:** Senior Full-Stack Architect & QA Lead  
**Sana:** 2026-10-15  
**Repozitoriy:** `https://github.com/Valijon21/babygames_app.git`  
**Joriy branch:** `main`

---

## 1. Repozitoriy va Tizim Muhiti Holati (Faktlar)

| Komponent / Muhit | Aniqlangan Versiya / Manzil | Holat | Izoh |
| :--- | :--- | :--- | :--- |
| **Git** | `2.51.0.windows.2` | TAYYOR | Git init qilindi, `main` branch, remote origin qo‘shildi |
| **GitHub Remote** | `https://github.com/Valijon21/babygames_app.git` | BO‘SH | Masofaviy repo mavjud, 0 commit (toza) |
| **Python** | `3.11.9` (`C:\Users\nout.plus\AppData\Local\Programs\Python\Python311`) | MAVJUD | Tizimda o‘rnatilgan, `.venv` hali yaratilmagan |
| **Node.js** | `v24.13.0` (`C:\Program Files\nodejs`) | MAVJUD | Tizimda o‘rnatilgan, `frontend/` hali scaffold qilinmagan |
| **npm** | `11.x` | MAVJUD | Node bilan integratsiyalashgan |
| **PostgreSQL** | `PostgreSQL 18` (`C:\Program Files\PostgreSQL\18\bin`) | MAVJUD | Tizimda xizmat sifatida mavjud |
| **Redis** | `Redis 3.0` (`C:\Program Files\Redis`) | MAVJUD | Tizimda mavjud |
| **Docker** | Docker CLI (`C:\Program Files\Docker\Docker\resources\bin`) | MAVJUD | Tizimda mavjud |

---

## 2. Mavjud Hujjatlar va Tasklar Muvofiqligi

Barcha 15 ta asosiy arxitektura hujjati `docs/` katalogida to‘liq mavjud va o‘rganib chiqildi:
1. `01_PRODUCT_VISION.md` — Maqsadli auditoriya (2 yoshdan boshlab), MVP doirasi va ko‘nikmalar.
2. `02_ARCHITECTURE.md` — Modular monolith (Django DRF) + SPA (React/TypeScript).
3. `03_MODULES_AND_GAMES.md` — 4 ta MVP o‘yini (Rasm bo‘yash, Alifbo, Raqamlar, Xotira) va umumiy lifecycle.
4. `04_DATABASE_DESIGN.md` — Relatsion schema (Account, ChildProfile, GameCategory, Game, GameAsset, GameSession, ProgressRecord).
5. `05_API_SPEC.md` — `/api/v1/` endpointlar shartnomasi va standart xatolik formati.
6. `06_FRONTEND_DESIGN_SYSTEM.md` — Yosh toifalariga mos UI, WCAG kontrast, touch targetlar (>= 44x44px).
7. `07_SECURITY_PRIVACY.md` — COPPA/GDPR-K mosligi, bola PII minimallashtirish, IDOR himoyasi.
8. `08_TESTING_QA.md` — Test piramidasi: Unit (pytest, Vitest), Integration (API), E2E.
9. `09_ROADMAP.md` — 10 ta bosqich (Phase 00 dan Phase 09 gacha).
10. `10_TASKS.md` — Task backlog (BJ-001 dan BJ-131 gacha).
11. `11_SCALABILITY_AND_RELIABILITY.md` — Kengayish, N+1 query nazorati, caching, liveness/readiness, throttling.
12. `DECISIONS.md` — Arxitektura qarorlari va ochiq savollar.
13. `START_HERE_ANTIGRAVITY.md` — Bosqichma-bosqich boshlash yo‘riqnomasi.
14. `AGENTS.md` — Qat’iy coding agent shartnomasi va ish qoidalari.
15. `docs/adr/` — ADR 0001 (ADR formati), 0002 (Modular Monolith), 0003 (Child Privacy) yaratilgan.

---

## 3. Mavjud Funksiyalar va Yetishmayotgan Qatlamlar

### Bajarilgan / Tayyorlangan Qatlamlar:
- [x] Loyiha hujjatlari va spetsifikatsiyalari tartibga keltirildi (`docs/`).
- [x] Git repozitoriysi va remote origin ulandi (`babygames_app.git`).
- [x] Ishonchli `.gitignore` (Python, Django, Node, env, media) va `.gitattributes` yaratildi.
- [x] `.env.example`, `docker-compose.yml`, `.github/workflows/ci.yml` konfiguratsiya shablonlari tayyorlandi.
- [x] Backend boshlang‘ich kod skeleti (`apps/common`, `apps/accounts`, `apps/child_profiles`, `apps/catalog`, `apps/game_content`) loyihalashtirildi.

### Hali Bajarilmagan (Yetishmayotgan) Qatlamlar:
- [ ] Birinchi Git commit (`BJ-010`) amalga oshirilmagan va GitHub’ga push qilinmagan.
- [ ] Backend virtual muhiti (`.venv`) va kutubxonalar o‘rnatilmagan; migrationlar ishga tushirilmagan.
- [ ] Frontend (`frontend/`) ilovasi React/Vite/TypeScript bilan hali scaffold qilinmagan.
- [ ] Test suitelari (backend pytest, frontend Vitest) hali ishga tushirilmagan.
- [ ] API endpointlarining real javob berishi va integration testlari tekshirilmagan.

---

## 4. Aniqlangan Xavflar va Ularning Oldini Olish Choralari

1. **Xavf (Bolalar maxfiyligi):** Bolalarning shaxsiy ma’lumotlari (PII) oqib ketishi yoki IDOR orqali boshqa oila ma’lumotiga kirish.  
   *Oldini olish:* Bolalar uchun alohida akkaunt yo‘q; faqat vasiy (guardian) boshqaradi. Serializer va permissionlarda qat’iy `IsGuardianOfChild` tekshiruvi.
2. **Xavf (Mavjud o‘yinlarni buzish / Regressiya):** Yangi o‘yin qo‘shilganda eski o‘yinlarning API yoki session ma’lumotlari buzilishi.  
   *Oldini olish:* `11_SCALABILITY_AND_RELIABILITY.md` ga binoan versionlangan content schema va umumiy session contract qo‘llanadi.
3. **Xavf (Database N+1 va Resurs ortiqcha yuklanishi):** O‘yinlar katalogi va progress so‘rovlarida N+1 querylar yuzaga kelishi.  
   *Oldini olish:* `select_related('category')`, pagination va composite DB indekslari (`game_catalog_idx`) majburiy qilindi.
4. **Xavf (Testlanmagan kodni tasdiqlash):** Test ishlamay turib "tayyor" deb e’lon qilish.  
   *Oldini olish:* `AGENTS.md` bo‘yicha qat’iy taqiq — har bir task uchun acceptance criteria va test buyrug‘i dalili talab qilinadi.

---

## 5. Tavsiya Etiladigan Keyingi Eng Kichik 3 Ta Xavfsiz Task

`10_TASKS.md` va `09_ROADMAP.md` (Phase 01 — Foundation) bo‘yicha:

1. **`BJ-010` — Repozitoriy bazasi va ilk commit:**
   - **Maqsad:** Hujjatlar, konfiguratsiyalar (`.gitignore`, `.gitattributes`, `README.md`, `AGENTS.md`) va mavjud poydevorni tekshirib, Conventional Commits formatida birinchi commitni amalga oshirish va `origin main` ga push qilish.
   - **Acceptance Criteria:** `git status` toza, commit tarixi ravon, GitHub remote bilan sinxron.
2. **`BJ-013` & `BJ-014` — Backend virtualenv, dependencylar va migrationlar:**
   - **Maqsad:** Python virtual muhitini (`.venv`) yaratish, `requirements.txt` ni o‘rnatish, Django migrationlarini bajarish va `/api/v1/health/` endpointini testdan o‘tkazish.
   - **Acceptance Criteria:** `python manage.py test` 100% muvaffaqiyatli o‘tadi, health endpoint 200 qaytaradi.
3. **`BJ-011` & `BJ-012` — Frontend React + Vite + TypeScript strict scaffold:**
   - **Maqsad:** `frontend/` katalogida toza React/Vite/TS loyihasini o‘rnatish, Vitest va ESLint skriptlarini sozlash.
   - **Acceptance Criteria:** `npm run typecheck`, `npm run build` va `npm test` xatoliksiz ishlaydi.
