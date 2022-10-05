# Generated by Django 4.1.1 on 2022-09-28 12:08

from django.db import migrations, models

import core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.IntegerField(blank=True, null=True, validators=[core.validators.validate_unique_phone]),
        ),
    ]