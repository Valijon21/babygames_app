from rest_framework.views import exception_handler
from rest_framework import status


def custom_exception_handler(exc, context):
    """
    Standardized API error response handler adhering to Bolajon API Spec:
    {
      "error": {
        "code": "<ERROR_CODE>",
        "message": "<Human readable description>",
        "details": { ... }
      }
    }
    """
    response = exception_handler(exc, context)

    if response is not None:
        # Determine error code based on HTTP status code
        error_code = 'SERVER_ERROR'
        message = 'An unexpected error occurred.'

        if response.status_code == status.HTTP_400_BAD_REQUEST:
            error_code = 'VALIDATION_ERROR'
            message = 'Ma’lumotlarni tekshiring.'
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            error_code = 'UNAUTHORIZED'
            message = 'Tizimga kirish talab etiladi.'
        elif response.status_code == status.HTTP_403_FORBIDDEN:
            error_code = 'FORBIDDEN'
            message = 'Ushbu amalni bajarish uchun ruxsat yo‘q.'
        elif response.status_code == status.HTTP_404_NOT_FOUND:
            error_code = 'NOT_FOUND'
            message = 'So‘ralgan ma’lumot topilmadi.'
        elif response.status_code == status.HTTP_429_TOO_MANY_REQUESTS:
            error_code = 'RATE_LIMITED'
            message = 'So‘rovlar soni me’yordan oshdi. Birozdan so‘ng qayta urinib ko‘ring.'

        details = response.data
        if isinstance(details, dict) and 'detail' in details:
            message = str(details.pop('detail'))

        response.data = {
            'error': {
                'code': error_code,
                'message': message,
                'details': details if details else {}
            }
        }

    return response
