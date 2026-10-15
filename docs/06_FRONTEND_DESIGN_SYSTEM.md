# 06 — Frontend Design System

## 1. Vizual yo‘nalish
Quvnoq, ishonchli, zamonaviy va tartibli. Barcha yoshlarni bir xil “kichkintoycha” uslubga majburlamang: 2–8 uchun rangli va sodda; 9–16+ uchun toza, zamonaviy, yoshga mos ko‘rinish. Har bir ekranda bitta asosiy vazifa.

## 2. Dizayn tokenlari
- Ranglar CSS variables orqali: primary, secondary, accent, success, warning, danger, surface, text, muted.
- Rang ma’nosini faqat rang bilan bildirmang; ikon/matn bilan ham ko‘rsating.
- Burchaklar, spacing, elevation va typography tokenlari.
- Minimal matn, aniq kontrast, katta touch target (kamida taxminan 44×44 CSS px maqsad).
- Animatsiyalar qisqa, foydali; `prefers-reduced-motion` qo‘llab-quvvatlansin.
- Fontlar: o‘zbek lotin belgilarini to‘liq qo‘llaydigan font.

## 3. Asosiy sahifalar
1. Home — yosh/kategoriya tanlash, davom ettirish, featured games.
2. Category listing — kartalar, filtrlar, bo‘sh holat.
3. Game detail/launch — tavsif, taxminiy davomiylik, boshlash.
4. Game runtime — o‘yin maydoni, minimal nazorat, qayta boshlash.
5. Results — ijobiy feedback, qayta o‘ynash, keyingi tavsiya.
6. Parent area — bola profili, progress, sozlamalar.
7. Parent auth — kirish/ro‘yxatdan o‘tish, xatolar tushunarli.
8. Accessibility/settings — ovoz, harakat, til.
9. Admin — MVPda Django Admin.

## 4. Bo‘yash UX
- Palitra klaviatura va touch bilan ishlasin.
- Tanlangan rang aniq ko‘rinsin.
- Undo/redo, reset (tasdiq bilan), zoom agar kerak bo‘lsa.
- Region bo‘yashda bo‘yalgan hudud chegaralari ko‘rinarli bo‘lsin.
- SVG `aria-label`/accessible alternatives; Canvas bo‘lsa klaviatura bilan muqobil boshqaruv.
- Saqlash/PNG eksport holatlari, xatolar va katta fayl cheklovi.

## 5. Accessibility
- Semantik HTML, focus indicator, klaviatura navigatsiyasi.
- Matn va fon kontrasti WCAG 2.2 AA darajasiga intilsin.
- Har bir mazmunli rasmda alt text; dekorativ rasmlarda bo‘sh alt.
- Audio topshiriqlar uchun qayta eshitish tugmasi va zarur joyda matnli alternativa.
- Harf yozish canvasiga qo‘shimcha tanlash yoki tugmalar orqali muqobil mashq.
- Avtomatik fokus ko‘chishi va miltillashdan qochish.

## 6. UI komponentlar
`Button`, `IconButton`, `Card`, `GameTile`, `CategoryChip`, `AgeSelector`, `ProgressRing` (faqat ma’noli bo‘lsa), `Modal`, `Toast`, `AudioControl`, `ColorPalette`, `GameToolbar`, `EmptyState`, `ErrorState`, `LoadingSkeleton`.
Bir komponentni faqat kerakli joylarda qayta ishlating; barcha sahifani bitta universal komponentga aylantirmang.

## 7. Responsive
- Mobile-first.
- Touch input va mouse input bir xil o‘yin mexanikasiga bog‘lansin.
- Landscape/portrait holati tekshirilsin.
- 360px telefon, katta telefon, planshet va desktop test viewportlari.
- Virtual keyboard chiqishida yozuv mashqlari maydoni foydalanishga yaroqli bo‘lsin.
