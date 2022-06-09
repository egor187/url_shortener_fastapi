import secrets
import string

from core.settings import get_settings

settings = get_settings()


def get_short_code():
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(settings.DEFAULT_SHORT_CODE_LENGTH))
