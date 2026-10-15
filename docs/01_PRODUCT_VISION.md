# 01 — Product Vision & Requirements

## 1. Mahsulot tavsifi
Bolajon — bolalarning ijodiy fikrlashi, boshlang‘ich savodxonligi, matematik tafakkuri, diqqati va xotirasini rivojlantiradigan web-platforma. Platforma bolaga mustaqil, katta tugmalar va kam matn bilan o‘yin o‘ynash imkonini beradi; ota-ona yoki pedagog esa yoshga mos kontent va progressni boshqaradi.

## 2. Auditoriya va yosh bo‘yicha yondashuv
Yosh toifalari mahsulotni tashkil qilish uchun tavsiya etiladi; bolaning individual rivojlanishi farq qilishi mumkin.

| Segment | UX va kontent |
|---|---|
| 2–3 | Katta bosiladigan elementlar, qisqa mashg‘ulotlar, rang/shakl/ovoz, yozuv talab qilmaydigan o‘yinlar. Katta kishi yordami tavsiya qilinadi. |
| 4–5 | Rang berish, shakl ajratish, sodda moslashtirish, harf va raqam bilan tanishish. |
| 6–8 | O‘zbek alifbosi, yozuv mashqlari, sanash, sodda arifmetika, xotira va mantiq. |
| 9–12 | Murakkabroq matematika, so‘z/harf o‘yinlari, naqsh, strategiya va mantiq. |
| 13–16 | Tezlikka asoslangan viktorinalar, murakkab mantiq, matematika va ijodiy topshiriqlar; bolalarcha dizayn majburiy emas. |
| 16+ | Kattaroq yoshdagilar uchun alohida “Kengaytirilgan” kontent yo‘li; platforma faqat kichik bolalarga mo‘ljallangan ko‘rinishda qolib ketmasin. |

## 3. Muammo va qiymat taklifi
- O‘zbek alifbosi va o‘zbekcha interfeysga yo‘naltirilgan o‘yinlar.
- Bo‘yash, yozish, eslab qolish va hisoblashni bitta joyda birlashtirish.
- Yosh, ko‘nikma va qiyinlik bo‘yicha tartiblangan kontent.
- Bola uchun xavfsiz va chalg‘itmaydigan interfeys.
- Ota-ona/pedagog uchun progress ko‘rinishi, lekin bolaning shaxsiy ma’lumotlarini minimal yig‘ish.

## 4. MVP funksional talablar
### Must-have
- Bosh sahifa: yosh yo‘nalishi va o‘yin kategoriyalari.
- Kategoriyalar va o‘yinlar katalogi; qidirish va filtrlar.
- Bo‘yash canvas: rang palitrasi, brush/chelak (bucket fill), undo/redo, reset, saqlash/chiqarish.
- O‘zbek alifbosi: harfni ko‘rsatish, audio talaffuz (audio fayl bo‘lsa), harf izidan yozish.
- Raqamlar: raqamni tanish/yozish, sanash va sodda topshiriqlar.
- Xotira: kartalarni aylantirish va juftlik topish.
- O‘yin sessiyasi yakuni: natija, yulduz/feedback, qayta o‘ynash.
- Progress: yakunlangan o‘yinlar va oxirgi faoliyat.
- Ota-ona bo‘limi: bolaning lokal profili yoki ota-ona akkaunti orqali profil; yosh diapazoni va progress.
- Admin panel: kategoriya, o‘yin metadata, rasm/audio assetlari, topshiriq va nashr holatini boshqarish.
- Responsive: telefon, planshet, desktop; klaviatura va touch input.
- Uzbek Latin asosiy til; matnlar i18n orqali boshqarilsin.

### Should-have (MVP+)
- PWA installability va asosiy statik kontent uchun offline cache.
- Ota-ona bir nechta bola profilini boshqarishi.
- O‘yin ichidagi sozlanadigan audio/musiqa.
- Pedagog uchun guruh rejimi.

### MVPdan tashqarida
- Ochiq chat, user-generated public profiles, leaderboard orqali ommaviy taqqoslash.
- Reklama va uchinchi tomon tracking.
- AI bilan bolaga erkin chat.
- Real pul mukofoti, loot box yoki manipulyativ daily streak.
- To‘lov va premium obuna — bozor sinovidan keyin alohida qaror.

## 5. Nofunksional talablar
- Birinchi mazmunli ko‘rinish: maqsadli mobil tarmoqda 3 soniyadan kam bo‘lishiga intilish; real o‘lchov bilan tasdiqlash.
- Asosiy ekranlar 360px kenglikdan boshlab ishlashi.
- API pagination, validatsiya, aniq xato formatlari.
- Serverda ruxsat tekshiruvi; frontend yashirishi xavfsizlik o‘rnini bosa olmaydi.
- Loglarda bolaning ortiqcha shaxsiy ma’lumotlari bo‘lmasin.
- O‘yinlar kontenti kod deploy qilmasdan admin orqali yangilanishi mumkin bo‘lsin.
- Har bir release uchun test, migratsiya tekshiruvi va rollback rejasi.

## 6. Muvaffaqiyat metrikalari
- O‘yin boshlashdan yakunlashgacha bo‘lgan konversiya.
- Kategoriya bo‘yicha o‘yin yakunlash darajasi.
- 7 kun ichida qaytish (faqat qonuniy va maxfiylikka mos analitika bilan).
- Ota-onalar foydalanuvchi tajribasi bahosi.
- Frontend xatolari, API 5xx, sahifa yuklanish vaqti.
- Kontentdagi xato/nomuvofiqliklar soni.

Metrikalar bolani ko‘proq ekran qarshisida ushlab turish uchun emas, mahsulotning foydaliligi va ishlash sifatini o‘lchash uchun ishlatiladi.
