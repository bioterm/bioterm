import re


def validate_email(email: str):
    """Validate the email address using a regular expression."""
    pattern = r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$"
    return re.match(pattern, email)


def validate_domain(domain: str):
    """Check if the provided string is a valid domain using a regular expression."""
    if not domain:
        return None

    if domain.startswith("http://") or domain.startswith("https://"):
        return None

    # Regular expression pattern for validating domain
    pattern = r"^([a-zA-Z0-9][a-zA-Z0-9\-]{1,61}[a-zA-Z0-9]\.)+[a-zA-Z]{2,}$"

    # Check if the domain matches the pattern
    return re.match(pattern, domain)
