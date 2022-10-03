from datetime import date

from django.core.exceptions import ValidationError


def validate_start_date(value):
    if value < date.today():
        raise ValidationError('Incorrect group start date!')
    else:
        pass


def validate_group_description(value):
    validate_name = ['Python', 'Php', 'Java', 'Javascript', 'HR generalist',
                     'QA Manual', 'QA Automation', 'UI/UX Design']
    for name in validate_name:
        if name in value:
            pass
    else:
        raise ValidationError(f'Incorrect group description <{value}>')
