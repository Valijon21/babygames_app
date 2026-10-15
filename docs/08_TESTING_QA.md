# 08 — Testing & Quality Assurance

## Test qatlamlari
### Frontend unit
- O‘yin state reducerlari va scoring logic.
- Rang palitrasi, undo/redo, reset.
- Harf/raqam topshiriqlari va validatsiya.
- Xato, loading va empty state.

### Frontend component
- Keyboard navigation, focus, aria labels.
- Responsive layout va touch eventlar.
- Audio control va reduced motion.
- API loading/error handling.

### Backend
- Model constraints va migrations.
- Serializer validatsiyasi.
- Permission/ownership: bir ota-ona boshqa oilaning profilini ko‘ra olmaydi.
- Public API faqat published kontentni qaytaradi.
- Session completion, invalid score, negative duration.
- Rate limiting va upload validation.

### End-to-end
- Katalogdan o‘yin ochish va yakunlash.
- Bo‘yash: rang tanlash, regionni bo‘yash, undo, export.
- Harf/raqam mashqi.
- Xotira o‘yini juftlik topish.
- Ota-ona login, profil yaratish, progress ko‘rish.
- 360px mobil va planshet viewport.
- Offline/online qaytish — agar PWA sync qo‘shilsa.

## CI quality gates
- Lint va format.
- TypeScript `noEmit` typecheck.
- Frontend unit tests.
- Backend tests.
- Build.
- Migration check.
- Dependency/security scan — mavjud pipeline imkoniyatiga qarab.
- Pull requestda testlar yashil bo‘lmasa merge qilinmasin.

## Definition of Done
Task faqat quyidagilar bajarilganda tayyor:
1. Acceptance criteria bajarilgan.
2. Testlar yozilgan va o‘tgan.
3. Responsive/accessibility tekshirilgan.
4. Loading, empty, error, success holatlari bor.
5. API va docs yangilangan.
6. Secret yoki shaxsiy ma’lumot commit qilinmagan.
7. Mavjud funksiyalar regressiya qilmagan.
8. O‘zgarish va test natijalari hisobotda qayd etilgan.

## Release checklist
- `DEBUG=False`, env tekshirilgan.
- DB migration va backup.
- Static/media storage.
- HTTPS va domain.
- Health check/monitoring.
- Admin superuser xavfsiz yaratilgan.
- Seed content demo sifatida belgilangan.
- Rollback qadamlari yozilgan.
