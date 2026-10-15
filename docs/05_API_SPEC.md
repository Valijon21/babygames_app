# 05 — REST API Specification

## Umumiy
Base path: `/api/v1/`. Barcha endpointlar JSON. API schema OpenAPI orqali hujjatlashtirilsin. Pagination va filter formatlari bir xil bo‘lsin. Endpointlar ishlab chiqish vaqtida tasdiqlanadi; quyidagi ro‘yxat MVP uchun shartnoma loyihasi.

## Public katalog
- `GET /api/v1/health/` — health check, shaxsiy konfiguratsiya chiqarmaydi.
- `GET /api/v1/categories/` — faol kategoriyalar.
- `GET /api/v1/games/` — `category`, `age`, `difficulty`, `skill`, `search`, `page` filtrlari.
- `GET /api/v1/games/{slug}/` — faqat published o‘yin metadata.
- `GET /api/v1/games/{slug}/content/` — published va versionlangan o‘yin kontenti.
- `GET /api/v1/alphabet/` — o‘zbek alifbosi elementlari va mavjud audio assetlari.
- `GET /api/v1/math/tasks/` — yosh/qiyinlik/ko‘nikma bo‘yicha tasklar; javoblarni mijozga oshkor qilish strategiyasi o‘yin formatiga qarab ko‘rib chiqilsin.

## Auth va bola profili
- `POST /api/v1/auth/register/`
- `POST /api/v1/auth/login/`
- `POST /api/v1/auth/logout/`
- `POST /api/v1/auth/refresh/` (JWT tanlansa)
- `GET /api/v1/me/`
- `GET /api/v1/children/`
- `POST /api/v1/children/`
- `GET /api/v1/children/{id}/`
- `PATCH /api/v1/children/{id}/`
- `DELETE /api/v1/children/{id}/` — account/child data deletion policy bilan.

## O‘yin sessiyalari va progress
- `POST /api/v1/sessions/` — sessiya boshlash; game published ekanligi tekshiriladi.
- `POST /api/v1/sessions/{id}/complete/` — natija yuborish; duration/score/payload serverda validate qilinadi.
- `GET /api/v1/children/{id}/progress/`
- `GET /api/v1/children/{id}/activity/`
- `POST /api/v1/artworks/` va `GET /api/v1/artworks/` — faqat artwork saqlash funksiyasi MVPga kiritilsa.

## Admin
Ichki kontent boshqaruvi uchun avval Django Admin ishlatilsin. Alohida React admin panel zarurati tasdiqlangandan keyin qo‘shiladi.
- Keyingi versiyada `/api/v1/admin/content/...` endpoints role-based permissions, audit log va serializer validation bilan.
- Admin API hech qachon faqat frontend route yashirishga tayanmasin.

## Misol: o‘yin sessiyasini yakunlash
Request:
```json
{
  "completed": true,
  "duration_seconds": 95,
  "score": 8,
  "attempts": 10,
  "content_version": 1
}
```
Response:
```json
{
  "id": "uuid",
  "status": "completed",
  "score": 8,
  "progress_updated": true
}
```

## Standart xato
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Ma’lumotlarni tekshiring.",
    "details": {"duration_seconds": ["Manfiy bo‘lishi mumkin emas."]}
  }
}
```

## API xavfsizligi
- Object-level authorization: child IDni taxmin qilish orqali boshqa oilaning ma’lumotiga kira olmasin.
- Throttling: auth, session complete va upload endpointlari.
- Pagination va maksimal page size.
- Upload uchun size/type/rate limit.
- CORS faqat kerakli originlar.
- Productionda browsable API va debug traceback siyosati ongli tanlansin.
