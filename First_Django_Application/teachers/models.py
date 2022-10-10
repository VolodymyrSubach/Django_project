from datetime import date

from core.validators import valid_email_domains, validate_group_description, validate_unique_email, \
    validate_unique_phone

from dateutil.relativedelta import relativedelta

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.models import GROUPNAME

from students.models import VALID_DOMAIN_LIST

validate_name = ['Python', 'Php', 'Java', 'Javascript', 'HR generalist',
                 'QA Manual', 'QA Automation', 'UI/UX Design']


class Teacher(models.Model):
    first_name = models.CharField(
        max_length=100,
        verbose_name='first name',
        db_column='first_name_column',
        validators=[MinLengthValidator(2, '"first_name" field value less than two symbols')]
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='last name',
        db_column='last_name_column',
        validators=[MinLengthValidator(2)],
        error_messages={'min_length': '"last_name" field value less than two symbols'}
    )
    birthday = models.DateField(default=date.today, null=True, blank=True)

    email = models.EmailField(validators=[valid_email_domains, validate_unique_email])

    phone = models.CharField(max_length=20, validators=[validate_unique_phone], null=True, blank=True)

    subject_name = models.CharField(max_length=13, validators=[validate_group_description])

    def __str__(self):
        return f'{self.pk}{self.first_name} {self.last_name}'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            first_name = f.first_name()
            last_name = f.last_name()
            email = f'{first_name}.{last_name}{f.random.choice(VALID_DOMAIN_LIST)}'
            # phone = f.phone_number
            birthday = f.date()
            subject_name = f'{f.random.choice(GROUPNAME)}'
            st = cls(first_name=first_name, last_name=last_name, birthday=birthday, email=email,
                     subject_name=subject_name)
            try:
                st.full_clean()
                st.save()
            except:
                print(f'Incorrect data {first_name}, {last_name}, {birthday}, {email}, {subject_name}')

    def get_age(self):
        return relativedelta(date.today(), self.birthday).years
