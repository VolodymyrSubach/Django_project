from datetime import date

from django.core.validators import MinLengthValidator
from django.db import models


class Group(models.Model):
    group_name = models.CharField(
        max_length=100,
        verbose_name='group name',
        db_column='group_name',
        validators=[MinLengthValidator(2, '"group_name" field value less than two symbols')]
    )
    group_start_date = models.DateField(
        default=date.today,
        null=True,
        blank=True,
        verbose_name='group start date',
        db_column='group_start_date')

    group_description = models.CharField(
        max_length=600,
        verbose_name='group description',
        db_column='group_description',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.group_name} {self.group_start_date}'
