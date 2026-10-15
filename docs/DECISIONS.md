# Architecture Decisions & Open Questions

## Confirmed starting decisions
- D01: MVP modular monolith; Django REST + PostgreSQL.
- D02: React + Vite + TypeScript frontend.
- D03: Uzbek Latin asosiy locale; tarjimalar keyinchalik qo‘shilishi mumkin.
- D04: Django Admin MVP kontent boshqaruvi uchun.
- D05: Bolalar profili ota-ona akkauntiga bog‘lanadi; minimal ma’lumot yig‘iladi.
- D06: MVPda reklama, public chat, to‘lov va AI-tutor yo‘q.
- D07: Har bir o‘yin mustaqil feature/runtime bo‘ladi.

## Before implementation, owner must decide
- D08: Yakuniy brend nomi, domain va vizual identitet.
- D09: Auth: email/password, email verification va JWT/cookie strategiyasi.
- D10: MVPda login majburiymi yoki anonymous play + ixtiyoriy ota-ona akkaunti bo‘ladimi?
- D11: Rasm assetlari: o‘zimiz chizamizmi, litsenziyalangan paketmi yoki buyurtma asosida illustratsiyami?
- D12: Bo‘yashda birinchi usul: SVG region-fill (tavsiya) yoki freehand Canvas.
- D13: O‘yin natijasi uchun qanday pedagogik scoring kerak; yosh bo‘yicha baholash mutaxassis bilan ko‘rib chiqilsin.
- D14: Offline/PWA MVPga kiradimi yoki MVP+mi?
- D15: Production hosting, domain, media storage va backup budjeti.
- D16: 13–16+ uchun vizual uslub va kontent chuqurligi.

## Decision record format
- Context
- Options considered
- Decision
- Consequences
- Date/owner
