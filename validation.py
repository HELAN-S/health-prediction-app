from email_validator import validate_email, EmailNotValidError
from datetime import date


def is_valid_email(email):
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def is_valid_dob(dob):
    return dob <= date.today()


def is_valid_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False