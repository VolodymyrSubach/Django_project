from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(value):
    if value < date.today():
        raise ValidationError('Incorrect group start date!')
    else:
        pass
