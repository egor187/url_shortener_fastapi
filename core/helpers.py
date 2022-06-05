import secrets
import string


DEFAULT_SHORT_CODE_LENGTH = 7


def get_short_code():
    chars = string.ascii_uppercase + string.digits
    return ''.join(secrets.choice(chars) for _ in range(DEFAULT_SHORT_CODE_LENGTH))
