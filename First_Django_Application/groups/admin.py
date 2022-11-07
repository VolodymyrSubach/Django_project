from django.contrib import admin

from groups.models import Group


class StudentInlineTable(admin.TabularInline):
    from students.models import Student
    model = Student
    fields = ('first_name', 'last_name', 'email')
    extra = 0
    readonly_fields = ('first_name', 'last_name', 'email')

    # show_change_link = True

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
    list_display = ('group_name', 'group_start_date')

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

        return form

    inlines = [StudentInlineTable, TeacherInlineTable, ]
