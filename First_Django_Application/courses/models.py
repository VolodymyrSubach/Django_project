from django.db import models

COURSE_NAMES = (('Front-End basics', 'Front-End basics'), ('Front-End Advanced', 'Front-End Advanced'),
                ('HR Generalist in IT', 'HR Generalist in IT'), ('Java Basic', 'Java Basic'),
                ('Java Advanced', 'Java Advanced'), ('QA Manual', 'QA Manual'), ('QA Automation', 'QA Automation'),
                ('Python Basics', 'Python Basics'), ('Python Advanced', 'Python Advanced'),
                ('UI/UX Design', 'UI/UX Design'), ('UI/UX Design', 'UI/UX Design Pro'))


class Course(models.Model):
    course_name = models.CharField(max_length=40, db_column='course name', verbose_name='course name',
                                   choices=COURSE_NAMES)
    duration = models.CharField(max_length=10)
    cost = models.IntegerField(null=True, blank=True)
    course_description = models.CharField(max_length=200, db_column='description', null=True, blank=True)
    group = models.OneToOneField('groups.Group', on_delete=models.SET_NULL, null=True, blank=True, related_name='group')

    def __str__(self):
        return f'{self.course_name} {self.duration} {self.cost}'

    class Meta:
        db_table = 'courses'
