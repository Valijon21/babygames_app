# Antigravity’da boshlash bo‘yicha yo‘riqnoma

## 1. Arxivni ochish
Arxivni ochib, hujjatlarni yangi loyiha repozitoriysining root qismiga joylashtiring. Agar kod repozitoriy allaqachon mavjud bo‘lsa, avval backup/branch yarating va hujjatlarni `docs/` ichiga moslab ko‘chiring. `AGENTS.md` rootda tursin.

## 2. Birinchi prompt — audit, kod yozmasin
Quyidagini Antigravity agentiga yuboring:

> Sen senior full-stack architect va QA lead sifatida ishlaysan. Avval rootdagi `AGENTS.md` va barcha loyiha hujjatlarini, ayniqsa `11_SCALABILITY_AND_RELIABILITY.md` ni to‘liq o‘qi. Hozircha kod yozma va fayllarni o‘chirma. Repo holati, texnologiyalar, dependencylar, testlar, xavfsizlik va hujjat-task mosligini audit qil. `docs/IMPLEMENTATION_STATUS.md` yarat: repo holati, bajarilgan/yo‘q funksiyalar, risklar, test holati va task dependencylari. So‘ng `10_TASKS.md`dan keyingi eng kichik 3 ta taskni tavsiya qil. Taxminlarni fakt sifatida ko‘rsatma.

## 3. Ikkinchi prompt — foundation
Auditni tekshirgandan keyin:

> Audit xulosasi bilan mos ravishda faqat foundation bosqichidagi eng birinchi tayyor taskni bajar. `AGENTS.md` workflowiga rioya qil. Avval o‘zgarish rejasini ko‘rsat, keyin implementatsiya qil, testlarni ishga tushir va yakunda hisobot ber. Scope’dan tashqariga chiqma.

## 4. Keyingi ishlar
Har safar agent hisobotini tekshiring. Testlar o‘tganidan va diff review qilingandan keyin keyingi taskga ruxsat bering. Katta ishlarni bir promptda berishdan saqlaning.

## 5. Eslatma
Bu hujjatlar boshlang‘ich professional loyiha blueprintidir, tayyor ishlab turgan dastur emas. Kontent sifati, bolalar xavfsizligi, litsenziya va production konfiguratsiyasi real ishga tushirishdan oldin tekshirilishi kerak.
