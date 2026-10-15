# 03 — Modullar va o‘yinlar katalogi

## 1. Katalog modeli
Har bir o‘yin quyidagi metadata bilan boshqariladi:
- `slug`, `title`, `description`, `category`
- `min_age`, `max_age`, `difficulty`
- `thumbnail`, `estimated_minutes`
- `skills`: creativity, literacy, numeracy, memory, logic, attention
- `status`: draft, review, published, archived
- `content_version`, `locale`, `accessibility_notes`

Yosh chegarasi tavsiya sifatida ishlatiladi, bolaning qobiliyati haqida qat’iy hukm emas.

## 2. MVP o‘yinlari
### A. Rasm bo‘yash
- Hayvonlar: mushuk, quyon, qush, baliq, kapalak.
- Tabiat: gul, daraxt, quyosh, bulut, tog‘, bog‘.
- Transport va uy-ro‘zg‘or buyumlari.
- Region bo‘yash: SVG regionlarni rang bilan to‘ldirish.
- Erkin chizish: brush, rang, o‘lcham, o‘chirg‘ich.
- Undo/redo, tozalashni tasdiqlash, PNG eksport.
- Saqlangan ishlar: private, ota-ona nazoratida; ommaga avtomatik chiqarilmaydi.

### B. O‘zbek alifbosi
- O‘zbek lotin alifbosi; `O‘`, `G‘`, `Sh`, `Ch`, `Ng` kabi belgilar va digraflar kontentda izchil ifodalanadi.
- Harf shaklini ko‘rsatish va audio talaffuz.
- Harfni rasm/so‘z bilan moslashtirish.
- Harf izidan yozish: pointer/touch stroke.
- Natija faqat taxminiy o‘quv feedback; yozuvni “noto‘g‘ri bola” deb baholamasin.

### C. Raqam va matematika
- 1–10 sanash, obyektlarni sanab raqamni tanlash.
- Raqam izidan yozish.
- Katta-kichik/ko‘p-kam.
- Qo‘shish/ayirish, son chizig‘i.
- Keyingi bosqich: ko‘paytirish, bo‘lish, kasrlar, matnli masalalar.
- Qiyinlik darajasi task metadata orqali boshqariladi.

### D. Xotira
- Bir xil rasmlar juftligini topish.
- Harf/raqam juftliklari.
- Ovoz yoki rasmni eslab moslashtirish.
- Qiyinlik: kartalar soni, ko‘rsatish vaqti, yordam darajasi.
- Vaqt bosimi kichik yoshdagi bolalar uchun default bo‘lmasin.

## 3. Keyingi o‘yinlar
- Shakl va ranglarni saralash.
- Labirint va yo‘l topish.
- Naqshni davom ettirish.
- Farqlarni topish.
- Pazzl va qismlarni yig‘ish.
- So‘z tuzish va bo‘g‘inlar.
- Tabiat/atrof-muhit bilimlari.
- Musiqa ritmi va tovushlarni farqlash.
- 13+ uchun mantiqiy masalalar, algoritmik fikrlash va matematik challenge.

## 4. O‘yin runtime kontrakti
Har bir o‘yin feature quyidagilarni amalga oshirsin:
- `GameConfig`: content ID, age range, difficulty, locale.
- `GameState`: serializatsiya qilinadigan minimal holat.
- `start()`, `reset()`, `pause()/resume()` agar mos bo‘lsa.
- `complete(result)`: score, completed, durationSeconds, attempts kabi oqilona maydonlar.
- `dispose()`: event listener, audio va timer resurslarini tozalash.
- Offline holatda sessiya vaqtincha lokal saqlanishi mumkin; server bilan sync strategiyasi alohida testlanadi.

O‘yinlar umumiy interfeysdan foydalansin, lekin har xil mexanikani bitta ulkan komponentga jamlamang.
