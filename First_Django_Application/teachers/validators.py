from django.core.exceptions import ValidationError

import teachers.models


def valid_email_domains(value):
    valid_domains = ['@gmail.com', '@yahoo.com']
    for domain in valid_domains:
        if domain in value:
            break
    else:
        raise ValidationError(f'Email <{value}> is incorrect address.')


def validate_unique_email(value):
    if teachers.models.Teacher.objects.filter(email=value):
        raise ValidationError(f'Your email <{value}> already exist.')
    else:
        pass


def validate_unique_phone(value):
    if teachers.models.Teacher.objects.filter(phone=value):
        raise ValidationError(f'Your phone number <{value}> already exist.')
    else:
        pass


def validate_group_description(value):
    validate_name = ['Python', 'Php', 'Java', 'Javascript', 'HR generalist',
                     'QA Manual', 'QA Automation', 'UI/UX Design']
    for description in validate_name:
        if description in value:
            break
    else:
        raise ValidationError(f'Incorrect group description <{value}>')
