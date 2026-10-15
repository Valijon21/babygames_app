# Bolajon — Bolalar uchun ta’limiy o‘yinlar platformasi

> Ishchi nom: **Bolajon**. Nomi keyinchalik almashtirilishi mumkin. Ushbu hujjatlar Antigravity/Gemini kabi coding agentlar bilan bosqichma-bosqich ishlab chiqish uchun tayyorlangan.

## Mahsulot maqsadi
2 yoshdan boshlab bolalar, maktabgacha yoshdagilar, boshlang‘ich sinf o‘quvchilari va kattaroq yoshdagilar uchun brauzerda ishlaydigan, o‘zbek tiliga mos, xavfsiz va qiziqarli ta’limiy o‘yinlar platformasi.

Asosiy yo‘nalishlar:
- Rasm bo‘yash: hayvonlar, gullar, daraxtlar, transport, tabiat va mavzuli sahifalar.
- Harflar va o‘zbek alifbosi: harfni tanish, tovushni eshitish, harfni yozish.
- Raqamlar va matematika: raqam yozish, sanash, taqqoslash, qo‘shish/ayirish, yoshga mos masalalar.
- Xotira o‘yinlari: juftlik topish, ketma-ketlikni eslab qolish, shakl va ranglarni ajratish.
- Mantiq va ijod: shakllarni joylashtirish, labirint, naqshni davom ettirish, farqlarni topish.
- Yosh va qiyinlik bo‘yicha moslashtirilgan yo‘llanma, ota-ona paneli va o‘rganish progressi.

## Texnologiyalar
- Frontend: React + Vite + TypeScript.
- UI: Tailwind CSS, accessible komponentlar, ikonlar va animatsiyalar uchun tanlangan kutubxonalar.
- Backend: Python + Django + Django REST Framework.
- Ma’lumotlar bazasi: PostgreSQL.
- Kesh/navbat: Redis — faqat zaruratga qarab; fon vazifalari keyingi bosqichda.
- Fayllar: lokal developmentda media storage, productionda S3-compatible object storage.
- Testlar: Vitest/React Testing Library, pytest, Django API tests, Playwright end-to-end.
- Deployment: Docker Compose; production muhitiga alohida konfiguratsiya.

## Hujjatlar
1. `01_PRODUCT_VISION.md` — mahsulot talabi va auditoriya.
2. `02_ARCHITECTURE.md` — tizim arxitekturasi.
3. `03_MODULES_AND_GAMES.md` — modullar va o‘yinlar katalogi.
4. `04_DATABASE_DESIGN.md` — ma’lumotlar modeli.
5. `05_API_SPEC.md` — REST API konvensiyalari va endpointlar.
6. `06_FRONTEND_DESIGN_SYSTEM.md` — UI/UX va dizayn tizimi.
7. `07_SECURITY_PRIVACY.md` — xavfsizlik va bolalar maxfiyligi.
8. `08_TESTING_QA.md` — test strategiyasi va sifat mezonlari.
9. `09_ROADMAP.md` — bosqichlar va release reja.
10. `10_TASKS.md` — agent bajaradigan tasklar.
11. `AGENTS.md` — coding agent uchun qat’iy ish qoidalari.
12. `DECISIONS.md` — arxitektura qarorlari va taxminlar.
13. `11_SCALABILITY_AND_RELIABILITY.md` — kengayuvchanlik, performance, monitoring va server barqarorligi.

## Scale strategiyasi
Dastlab modular monolith, keyin metrikalar ko‘rsatgan ehtiyojga qarab cache/CDN, gorizontal app scaling, fon workerlar va zarurat bo‘lsa alohida servislar. Microservice yoki Kubernetes MVP uchun avtomatik talab emas. `11_SCALABILITY_AND_RELIABILITY.md` majburiy o‘qilsin.

## Ishlash qoidasi
Avval hujjatlarni o‘qiting, repozitoriy holatini tekshirtiring va faqat shundan keyin tasklarni bajartiring. Barcha funksiyani bir promptda yozdirish tavsiya etilmaydi. Har bir milestone alohida branch/commit, test va review bilan yakunlansin.

## MVP chegarasi
Birinchi relizda rasm bo‘yash, harflar, raqamlar/sanash, xotira o‘yini, yosh bo‘yicha kontent tanlash, progressni saqlash va admin orqali kontent boshqaruvi bo‘ladi. To‘lov, ijtimoiy tarmoq, chat, reklama va AI-tutor MVPga kiritilmaydi.
