from django.contrib import admin  # noqa

from .forms import SUBJECT_NAME
from .models import Teacher


class TeacherListFilter(admin.SimpleListFilter):
    title = 'subject filter'
    parameter_name = 'subject_filter'

    def lookups(self, request, model_admin):
        lst = [subject for subject in SUBJECT_NAME]
        lst.insert(0, (0, 'No subject'))

        return tuple(lst)

    def queryset(self, request, queryset):
        match self.value():
            case None:
                return Teacher.objects.all()
            case '0':
                return Teacher.objects.filter(subject_name='')
            case _:
                return Teacher.objects.filter(subject_name=self.value())


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'subject_name')
    list_display_links = list_display
    list_per_page = 10
    list_filter = (TeacherListFilter,)

    fields = (
        ('first_name', 'last_name'),
        'email',
        'subject_name',
        ('create_datetime', 'update_datetime'),
    )
    readonly_fields = ('create_datetime', 'update_datetime')


admin.site.register(Teacher, TeacherAdmin)
