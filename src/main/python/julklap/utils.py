import re


def validate_email_address(email: str) -> bool:
    """
    Validate an email address using a regex that works most of the time.

    Args:
        email: email address to validate.

    Returns:
        bool: True if email address is valid, False if not.
    """
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    return bool(re.fullmatch(email_regex, email))
