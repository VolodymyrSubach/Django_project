# Generated by Django 4.1.1 on 2022-09-30 09:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_group_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_start_date',
            field=models.DateField(blank=True, db_column='group_start_date', default=datetime.date.today, null=True, verbose_name='group start date'),
        ),
    ]