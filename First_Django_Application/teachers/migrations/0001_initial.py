# Generated by Django 4.1.1 on 2022-09-30 13:34

import datetime
import django.core.validators
from django.db import migrations, models

import core.validators



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='first_name_column', max_length=100, validators=[django.core.validators.MinLengthValidator(2, '"first_name" field value less than two symbols')], verbose_name='first name')),
                ('last_name', models.CharField(db_column='last_name_column', error_messages={'min_length': '"last_name" field value less than two symbols'}, max_length=100, validators=[django.core.validators.MinLengthValidator(2)], verbose_name='last name')),
                ('birthday', models.DateField(blank=True, default=datetime.date.today, null=True)),
                ('email', models.EmailField(max_length=254, validators=[core.validators.valid_email_domains, core.validators.validate_unique_email])),
                ('phone', models.CharField(blank=True, max_length=20, null=True, validators=[core.validators.validate_unique_phone])),
                ('subject_name', models.CharField(max_length=13, validators=[core.validators.validate_group_description])),
            ],
            options={
                'db_table': 'teachers',
            },
        ),
    ]
