from datetime import date

from core.validators import validate_group_description

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker

from groups.validators import validate_start_date

GROUPNAME = ['Python', 'Php', 'Java', 'Javascript', 'HR generalist',
             'QA Manual', 'QA Automation', 'UI/UX Design']


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        verbose_name='group name',
        db_column='group_name',
        validators=[MinLengthValidator(2, '"group_name" field value less than two symbols')]
    )
    group_start_date = models.DateField(
        validators=[validate_start_date],
        default=date.today,
        verbose_name='group start date',
        db_column='group_start_date')

    group_description = models.CharField(
        validators=[validate_group_description],
        max_length=600,
        verbose_name='group description',
        db_column='group_description',
        default='test',
    )

    def __str__(self):
        return f'{self.group_name} {self.group_start_date}'

    class Meta:
        db_table = 'group'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()

        for _ in range(cnt):
            group_start_date = f.date()
            group_description = f'{f.random.choice(GROUPNAME)}'
            group_name = f'{group_description}_{group_start_date}'
            st = cls(group_name=group_name, group_start_date=group_start_date, group_description=group_description)
            try:
                st.full_clean()
                st.save()
            except:
                print(f'Incorrect data {group_name}, {group_start_date}, {group_description}')
