# 09 — Roadmap & Milestones

Muddatlar jamoa hajmi, kontent sifati va asset tayyorligiga bog‘liq. Quyidagi bosqichlar majburiy ketma-ketlik; muddatlar kafolat emas.

## Phase 00 — Discovery & project baseline
- Mahsulot doirasi, yosh segmentlari, MVP va success metrics tasdiqlash.
- Rasm/audio asset litsenziyasi va kontent manbalarini aniqlash.
- Repository, coding conventions, ADR va issue template.
**Gate:** MVP scope yozma tasdiqlangan.

## Phase 01 — Foundation
- React/Vite/TS va Django/DRF setup.
- PostgreSQL, env config, Docker Compose.
- CI, lint, test, health endpoint, OpenAPI.
**Gate:** clean checkoutdan loyihani ishga tushirish va testlarni bajarish mumkin.

## Phase 02 — Design system & catalog
- Tokenlar, umumiy komponentlar, responsive layout.
- Category/Game models, public catalog API, seed content.
- Home, category, game detail.
**Gate:** API va UI katalogi testlangan.

## Phase 03 — Coloring MVP
- Bitta SVG region-fill o‘yini.
- Palette, undo/redo, reset, export.
- Keyin 10–20 ta sifatli rasm kontent paketi.
**Gate:** turli qurilmalarda ishlaydi, asset litsenziyasi aniq.

## Phase 04 — Alphabet & numbers
- O‘zbek alifbosi kontenti.
- Harf/raqam tanish va izidan yozish.
- Sanash va sodda matematik topshiriqlar.
**Gate:** content schema va o‘yinlar testlangan.

## Phase 05 — Memory game & results
- Memory engine, qiyinlik sozlamalari.
- Session API va natija ekrani.
**Gate:** scoring server/client validatsiyasi va E2E.

## Phase 06 — Parent profile & progress
- Auth, child profile, ownership permissions.
- Progress dashboard, data deletion flow.
**Gate:** IDOR va privacy testlari o‘tgan.

## Phase 07 — Admin content workflow
- Django Admin, draft/review/published state.
- Asset upload validatsiyasi, preview va content version.
**Gate:** kontentni kod deploy qilmasdan nashr qilish mumkin.

## Phase 08 — Hardening & pilot
- Accessibility, performance, security review.
- Mobil/tablet/desktop test.
- Ota-onalar/pedagoglar bilan kichik pilot, fikrlarni hujjatlashtirish.
**Gate:** critical/high bug yo‘q, backup restore sinovdan o‘tgan.

## Phase 09 — Launch & iteration
- Monitoring, incident playbook, privacy pages.
- Kontent rejasini va analyticsni yaxshilash.
- PWA/offline, ko‘proq o‘yinlar va monetizatsiyani alohida qaror qilish.

## Parallel bajariladigan ishlar
Kontent jamoasi rasm/audio litsenziyasi va pedagogik tekshiruvni platforma kodidan mustaqil tayyorlashi mumkin. Kontentning mualliflik huquqi va bolaga mosligi release gate bo‘lsin.
