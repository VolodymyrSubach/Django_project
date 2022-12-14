# Generated by Django 4.1.2 on 2022-10-18 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(choices=[('Front-End basics', 'Front-End basics'), ('Front-End Advanced', 'Front-End Advanced'), ('HR Generalist in IT', 'HR Generalist in IT'), ('Java Basic', 'Java Basic'), ('Java Advanced', 'Java Advanced'), ('QA Manual', 'QA Manual'), ('QA Automation', 'QA Automation'), ('Python Basics', 'Python Basics'), ('Python Advanced', 'Python Advanced'), ('UI/UX Design', 'UI/UX Design'), ('UI/UX Design', 'UI/UX Design Pro')], db_column='course name', max_length=40, verbose_name='course name')),
                ('duration', models.CharField(max_length=10)),
                ('cost', models.IntegerField(blank=True, null=True)),
                ('course_description', models.CharField(blank=True, db_column='description', max_length=200, null=True)),
            ],
            options={
                'db_table': 'courses',
            },
        ),
    ]
