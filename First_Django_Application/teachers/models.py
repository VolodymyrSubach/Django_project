from datetime import date # noqa
from random import randint

from core.models import PersonModel
from core.validators import validate_group_description

from dateutil.relativedelta import relativedelta # noqa

from django.db import models

from faker import Faker # noqa


validate_name = ['Python', 'Php', 'Java', 'Javascript', 'HR generalist',
                 'QA Manual', 'QA Automation', 'UI/UX Design']


class Teacher(PersonModel):
    subject_name = models.CharField(max_length=13, validators=[validate_group_description])

    salary = models.PositiveIntegerField(default=10_000)

    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.salary}$'

    class Meta:
        db_table = 'teachers'

    @classmethod
    def _generate(cls):
        obj = super()._generate()
        obj.salary = randint(10_000, 100_000)
        obj.save()
