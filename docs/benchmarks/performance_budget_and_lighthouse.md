# Performance Budget & Lighthouse Baseline (BJ-112)

## 1. Core Web Vitals Targets

| Metric | Target | Warning Threshold | Critical Limit | Rationale for Children Platform |
| :--- | :--- | :--- | :--- | :--- |
| **LCP** (Largest Contentful Paint) | < 1.2s | 1.8s | 2.5s | Toddlers lose interest immediately if games don't display instantly |
| **INP** (Interaction to Next Paint) | < 50ms | 100ms | 200ms | Immediate audio/visual feedback on screen taps |
| **CLS** (Cumulative Layout Shift) | 0.00 | 0.05 | 0.10 | Zero shifting prevents accidental incorrect taps |
| **FCP** (First Contentful Paint) | < 0.8s | 1.2s | 1.8s | Instant visual rendering on mobile screens |
| **TTFB** (Time to First Byte) | < 80ms | 150ms | 300ms | Fast edge response from CDN / API |

---

## 2. Asset Payload Budget vs Actuals

| Asset Category | Maximum Budget (Gzip) | Actual Build (Gzip) | Status |
| :--- | :--- | :--- | :--- |
| **JavaScript Bundle** | 300 KB | **89.17 KB** | PASS (69% under budget) |
| **CSS Stylesheet** | 50 KB | **7.95 KB** | PASS (84% under budget) |
| **HTML Shell** | 5 KB | **0.29 KB** | PASS |
| **SVG Game Assets** | 100 KB / game | **< 15 KB** / template | PASS |
| **Audio Phonics Clips**| 80 KB / letter | **< 40 KB** / letter | PASS |

---

## 3. Lighthouse Baseline Targets
- **Performance:** ≥ 95 / 100
- **Accessibility:** 100 / 100 (Compliant with 44x44px minimum tap targets, high-contrast text, ARIA landmarks)
- **Best Practices:** 100 / 100 (HTTPS only, no console errors, modern image formats)
- **SEO:** 100 / 100 (Clean meta tags, OpenGraph previews, semantic HTML5)
