from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from django.utils.http import urlencode

from groups.models import Group


class StudentInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email')
    extra = 0
    readonly_fields = fields

    # show_change_link = True

    def get_queryset(self, request):
        queryset = self.model.objects.filter(
            group_id=int(request.resolver_match.kwargs['object_id'])
        ).select_related('group')

        return queryset

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False


class TeacherInlineTable(admin.TabularInline):
    from teachers.models import Teacher
    model = Teacher.groups.through
    fields = ['first_name', 'last_name', 'email', 'subject_name']
    extra = 0
    readonly_fields = ['first_name', 'last_name', 'email', 'subject_name']
    exclude = [model]

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj=None):
        return False

    def first_name(self, obj):
        return obj.teacher.first_name

    def last_name(self, obj):
        return obj.teacher.last_name

    def email(self, obj):
        return obj.teacher.email

    def subject_name(self, obj):
        return obj.teacher.subject_name


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_start_date', 'count_of_students_link')

    def count_of_students_link(self, obj):
        count = obj.students.count()
        url = (
           reverse('admin:students_student_changelist') + '?' + urlencode({'group_id': f'{obj.pk}'})
        )
        return format_html('<a href="{}">{} student(s)</a>', url, count)

    count_of_students_link.short_description = 'Students'
    fields = (
        'group_name',
        'headman',
        ('create_datetime', 'update_datetime'),
    )
    readonly_fields = ('create_datetime', 'update_datetime')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        form.base_fields['headman'].widget.can_add_related = False
        form.base_fields['headman'].widget.can_change_related = False
        form.base_fields['headman'].widget.can_delete_related = False
        form.base_fields['headman'].widget.can_view_related = False
        form.base_fields['headman'].queryset = obj.students.all()

        return form

    inlines = [StudentInlineTable, TeacherInlineTable, ]
