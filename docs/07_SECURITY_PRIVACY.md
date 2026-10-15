# 07 — Security, Privacy & Child Safety

## Asosiy qoida
Platforma bolalar bilan ishlaydi. Shuning uchun “keyin qo‘shamiz” deyishdan oldin ma’lumot minimallashtirish, xavfsiz defaultlar va ota-ona nazoratini MVP arxitekturasiga kiritish kerak. Ishga tushirishdan oldin O‘zbekiston qonunchiligi hamda maqsadli boshqa hududlarning bolalar ma’lumotlari va maxfiylik talablarini mutaxassis bilan tekshirish lozim.

## Ma’lumot minimallashtirish
- Boladan to‘liq ism, aniq tug‘ilgan sana, manzil, telefon, surat yoki joylashuvni so‘ramang.
- Profil uchun taxallus, oldindan belgilangan avatar va yosh diapazoni yetarli bo‘lishi mumkin.
- Ommaviy profil, ochiq chat, geolokatsiya va user-generated public content MVPda bo‘lmasin.
- Analytics faqat zarur, agregat va retention muddati belgilangan bo‘lsin.
- Ota-ona ma’lumotni ko‘rish/o‘chirish imkoniga ega bo‘lsin.

## Texnik himoya
- HTTPS; production secretlar repozitoriyga yozilmaydi.
- Django `DEBUG=False`, secure cookies, CSRF, aniq CORS, security headers.
- DRF permissions va object-level ownership tests.
- Rate limiting, login throttling, upload validation.
- Fayl kengaytmasiga emas, MIME/signature va hajmga ham qarash.
- SQL injection/XSS/CSRF/IDOR testlari.
- Admin uchun alohida ruxsat, minimal rol, kuchli parol va imkon bo‘lsa MFA.
- Dependency scanning va muntazam yangilash.
- Backup shifrlanishi, restore sinovi, retention va deletion siyosati.
- Loglarda access token, parol, bolaning profil nomi yoki to‘liq request payloadi yozilmasin.

## Bolaga mos dizayn
- Manipulyativ streak, uyaltiruvchi reyting va real pul mukofoti yo‘q.
- Xato javobda jazolovchi matn emas, foydali va muloyim feedback.
- O‘yin davomiyligi haqida ota-onaga sozlama/maslahat berish mumkin; bolaning ekran vaqtini yashirin kuzatish yo‘q.
- Tashqi linklar va xaridlar bola rejimida cheklansin.
- Audio/animatsiyani o‘chirish va reduced-motion imkoniyati.

## Release oldidan tekshiruv
- Privacy notice va ota-ona roziligi kerakligi yurist bilan baholangan.
- Data map, retention va deletion jarayoni hujjatlashtirilgan.
- Productionga demo akkauntlar/parollar chiqmagan.
- Security tests va backup restore sinovi o‘tgan.
