from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

import students.models


def valid_email_domains(value):
    valid_domains = ['@gmail.com', '@yahoo.com']
    for domain in valid_domains:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email <{value}> is incorrect address.')


@deconstructible
class ValidEmailDomain:
    def __init__(self, *domains):
        self.domains = list(domains)

    def __call__(self, *args, **kwargs):
        for domain in self.domains:
            if args[0].endswith(domain):
                break
        else:
            raise ValidationError(f'Invalid email address. The domain <{args[0].split("@")[1]}> not valid')


def validate_unique_email(value):
    if students.models.Student.objects.filter(email=value):
        raise ValidationError(f'Your email <{value}> already exist.')
    else:
        pass


def validate_unique_phone(value):
    if students.models.Student.objects.filter(phone=value):
        raise ValidationError(f'Your phone number <{value}> already exist.')
    else:
        pass
