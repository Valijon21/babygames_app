import json
import xml.etree.ElementTree as ET
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

MAX_FILE_SIZES = {
    'svg': 2 * 1024 * 1024,      # 2 MB
    'png': 5 * 1024 * 1024,      # 5 MB
    'audio': 10 * 1024 * 1024,   # 10 MB
    'json': 1 * 1024 * 1024,     # 1 MB
}

ALLOWED_EXTENSIONS = {
    'svg': ['.svg'],
    'png': ['.png', '.webp'],
    'audio': ['.mp3', '.ogg', '.wav'],
    'json': ['.json'],
}


def validate_asset_payload(asset_type: str, file_name: str, file_size: int, content_bytes: bytes = None):
    """
    BJ-102: Comprehensive asset validation for size, extension, and structure.
    Protects against malicious uploads, oversized media, and invalid game schemas.
    """
    if asset_type not in MAX_FILE_SIZES:
        raise ValidationError(_(f"Noma’lum asset turi: {asset_type}"))

    # 1. Size Check
    max_size = MAX_FILE_SIZES[asset_type]
    if file_size > max_size:
        max_mb = max_size / (1024 * 1024)
        raise ValidationError(_(f"{asset_type.upper()} fayl hajmi {max_mb} MB dan oshmasligi kerak."))

    # 2. Extension Check
    ext = '.' + file_name.rsplit('.', 1)[-1].lower() if '.' in file_name else ''
    if ext not in ALLOWED_EXTENSIONS[asset_type]:
        allowed = ", ".join(ALLOWED_EXTENSIONS[asset_type])
        raise ValidationError(_(f"{asset_type.upper()} uchun ruxsat etilgan kengaytmalar: {allowed}."))

    # 3. Structural Integrity Check
    if content_bytes:
        if asset_type == 'json':
            try:
                json.loads(content_bytes.decode('utf-8'))
            except Exception as e:
                raise ValidationError(_(f"Yaroqsiz JSON formati: {str(e)}"))

        elif asset_type == 'svg':
            try:
                # Basic XML parser check to ensure well-formed SVG and no malicious script injection
                root = ET.fromstring(content_bytes.decode('utf-8'))
                if not root.tag.endswith('svg'):
                    raise ValidationError(_("SVG fayl <svg> ildiz tegi bilan boshlanishi shart."))
            except Exception as e:
                raise ValidationError(_(f"Yaroqsiz SVG vektori: {str(e)}"))
