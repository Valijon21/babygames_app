# Bolajon — Bolalar uchun ta’limiy o‘yinlar platformasi

[![TypeScript](https://img.shields.io/badge/TypeScript-5.x-blue?logo=typescript)](https://www.typescriptlang.org/)
[![React](https://img.shields.io/badge/React-18-61dafb?logo=react)](https://react.dev/)
[![Vite](https://img.shields.io/badge/Vite-6-646CFF?logo=vite)](https://vitejs.dev/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?logo=postgresql)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED?logo=docker)](https://www.docker.com/)

> Ishchi nom: **Bolajon** (`babygames`). 2 yoshdan boshlab bolalar, maktabgacha yoshdagilar va boshlang‘ich sinf o‘quvchilari uchun o‘zbek tiliga moslashtirilgan, xavfsiz, yuqori sifatli va interaktiv ta’limiy o‘yinlar platformasi.

---

## 1. Mahsulot maqsadi va asosiy yo‘nalishlar

- **Rasm bo‘yash:** Hayvonlar, tabiat, transport va mavzuli sahifalar (SVG region-fill va erkin ijod).
- **O‘zbek alifbosi:** Harfni tanish, audio talaffuz (`O‘`, `G‘`, `Sh`, `Ch`, `Ng` to‘liq qo‘llab-quvvatlash), harf izidan yozish (tracing).
- **Raqamlar va matematika:** 1–10 sanash, taqqoslash, qo‘shish/ayirish va mantiqiy masalalar.
- **Xotira o‘yinlari:** Juftlik topish (memory match), ketma-ketlikni eslab qolish.
- **Xavfsiz ota-ona nazorati:** Bola profillari, progress monitoring va ma’lumotlar maxfiyligi (COPPA / GDPR-K).

---

## 2. Loyiha tuzilmasi (Repository Structure)

```text
babygames/
├── .github/                 # CI/CD workflowlar (GitHub Actions)
├── docs/                    # Loyiha hujjatlari, spetsifikatsiyalar va ADRlar
│   ├── 01_PRODUCT_VISION.md
│   ├── 02_ARCHITECTURE.md
│   ├── 03_MODULES_AND_GAMES.md
│   ├── 04_DATABASE_DESIGN.md
│   ├── 05_API_SPEC.md
│   ├── 06_FRONTEND_DESIGN_SYSTEM.md
│   ├── 07_SECURITY_PRIVACY.md
│   ├── 08_TESTING_QA.md
│   ├── 09_ROADMAP.md
│   ├── 10_TASKS.md
│   ├── 11_SCALABILITY_AND_RELIABILITY.md
│   ├── DECISIONS.md
│   ├── IMPLEMENTATION_STATUS.md
│   ├── IMPLEMENTATION_PROGRESS.md
│   └── adr/                 # Architecture Decision Records
├── frontend/                # React + TypeScript + Vite SPA
│   ├── src/
│   │   ├── app/             # Router va global providers
│   │   ├── components/      # UI dizayn tizimi komponentlari
│   │   ├── features/        # Modulli o‘yin va domen komponentlari
│   │   ├── hooks/           # Reusable React hooks
│   │   ├── lib/             # API client va utilities
│   │   ├── styles/          # Global CSS va dizayn tokenlari
│   │   └── types/           # TypeScript interfeyslari
│   └── tests/               # Vitest va Testing Library testlari
├── backend/                 # Django + Django REST Framework API
│   ├── config/              # Django settings, WSGI/ASGI, asosiy urls
│   ├── apps/
│   │   ├── common/          # Base models, health check, exceptions
│   │   ├── accounts/        # Ota-ona auth va permissions
│   │   ├── child_profiles/  # Bola profillari va sozlamalari
│   │   ├── catalog/         # Kategoriyalar va o‘yinlar katalogi
│   │   ├── game_content/    # O‘yin kontenti va assetlar
│   │   ├── game_sessions/   # O‘yin sessiyalari va natijalar
│   │   └── progress/        # Yutuqlar va agregat progress
│   └── tests/               # Pytest va DRF API testlari
├── infra/                   # Docker va server konfiguratsiyalari
│   └── docker/
├── .gitignore               # Git ignore qoidalari
├── .gitattributes          # Line endings va fayl turlari
├── AGENTS.md                # AI coding agent qoidalari
└── docker-compose.yml       # Lokal to‘liq muhit konteynerlari
```

---

## 3. Texnologik stek

- **Frontend:** React 18+, TypeScript (strict mode), Vite, Tailwind CSS.
- **Backend:** Python 3.11+, Django 5+, Django REST Framework.
- **Ma’lumotlar bazasi:** PostgreSQL 15+.
- **API Formati:** RESTful JSON (`/api/v1/`), OpenAPI 3.0 (drf-spectacular).
- **Testlash:** Vitest, Testing Library, pytest, pytest-django.
- **DevOps:** Docker, Docker Compose, GitHub Actions.

---

## 4. Boshlash (Quick Start)

### Talablar
- Node.js >= 20.x va npm
- Python >= 3.11
- PostgreSQL >= 15 (yoki Docker)

### Frontendni ishga tushirish
```bash
cd frontend
npm install
npm run dev
```

### Backendni ishga tushirish
```bash
cd backend
python -m venv .venv
# Windows:
.venv\Scripts\activate
# Linux/macOS:
# source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

---

## 5. Git va Commit qoidalari (Conventional Commits)

Loyihada **Conventional Commits** standarti qo‘llaniladi:
- `feat:` yangi funksionallik (masalan: `feat(catalog): add GameCategory API endpoint`)
- `fix:` xatolikni to‘g‘rilash (masalan: `fix(auth): enforce child profile ownership check`)
- `docs:` hujjatlashtirish (masalan: `docs(adr): record decision for modular monolith`)
- `test:` testlar qo‘shish yoki yangilash (masalan: `test(coloring): add SVG region fill unit tests`)
- `refactor:` kodni qayta ishlash
- `chore:` texnik sozlamalar va konfiguratsiyalar

---

## 6. Xavfsizlik va bolalar maxfiyligi

1. Bolalar uchun alohida login/parol yoki shaxsiy ma’lumot (telefon, manzil, aniq tug‘ilgan sana) yig‘ilmaydi.
2. Bolalar profillari faqat ota-ona / vasiy akkauntiga biriktirilgan taxalluslar orqali boshqariladi.
3. Tizimda tashqi reklama, ochiq chat va uchinchi tomon trekerlari yo‘q.
4. Batafsil: `docs/07_SECURITY_PRIVACY.md` va `docs/adr/0003-child-safety-and-data-privacy.md`.
