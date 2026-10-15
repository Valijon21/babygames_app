"""
BJ-113: Production Settings for Bolajon Platform.
Enforces strict security headers, SSL/TLS redirection, secure cookies, and restricted origins.
"""

import os
from .settings import *  # noqa: F401, F403

# 1. Debug strictly disabled in production
DEBUG = False

# 2. Host and Domain Security
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', 'bolajon.uz,api.bolajon.uz').split(',')

# 3. SSL / HTTPS Enforcement
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'True').lower() == 'true'
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# 4. Secure Cookies (Prevents session sniffing over unencrypted channels)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = False  # Required if frontend reads CSRF token, otherwise True with API headers
SESSION_COOKIE_SAMESITE = 'Lax'
CSRF_COOKIE_SAMESITE = 'Lax'

# 5. HTTP Strict Transport Security (HSTS)
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', 31536000))  # 1 Year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# 6. Clickjacking and MIME protection
X_FRAME_OPTIONS = 'DENY'
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_REFERRER_POLICY = 'strict-origin-when-cross-origin'

# 7. Cross-Origin Resource Sharing (CORS) & CSRF Trusted Origins
CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        'CORS_ALLOWED_ORIGINS',
        'https://bolajon.uz,https://www.bolajon.uz'
    ).split(',')
    if origin.strip()
]
CSRF_TRUSTED_ORIGINS = [
    origin.strip()
    for origin in os.environ.get(
        'CSRF_TRUSTED_ORIGINS',
        'https://bolajon.uz,https://api.bolajon.uz'
    ).split(',')
    if origin.strip()
]
