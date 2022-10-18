from datetime import date

from core.models import BaseModel
from core.validators import validate_group_description # noqa

from django.core.validators import MinLengthValidator
from django.db import models

from faker import Faker# noqa

from groups.validators import validate_start_date

from teachers.models import Teacher

GROUPNAME = (('fe', 'Front-End'), ('hr', 'HR'), ('j', 'Java'), ('qa', 'QA Manual'), ('qaA', 'QA Automation'),
                     ('pt', 'Python'), ('ux', 'UI/UX Design'))


class Group(BaseModel):
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
        max_length=600,
        verbose_name='group description',
        db_column='group_description',
        choices=GROUPNAME,
        null=True,
        blank=True
    )
    headman = models.OneToOneField(
        'students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group')
    teachers = models.ManyToManyField(
        to=Teacher,
        null=True,
        blank=True,
        related_name='groups'
    )

    def __str__(self):
        return f'{self.group_name} {self.group_start_date}'

    class Meta:
        db_table = 'group'

    @classmethod
    def gen_group(cls):
        f = Faker()
        lst = [
            'Python',
            'Java',
            'PM',
            'Devops',
            'FrontEnd',
            'QA'
        ]

        for group in lst:
            Group.objects.create(
                group_name=group
            )
