from courses.models import Course

from django import forms


from django_filters import FilterSet


class CourseBaseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'


class CreateCourseForm(CourseBaseForm):
    from groups.models import Group

    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.select_related('group'), required=False)

    def save(self, commit=True):
        course = super().save(commit)
        groups = self.cleaned_data['groups']
        for group in groups:
            group.course = course
            group.save()

    class Meta(CourseBaseForm.Meta):
        exclude = [
            'group',
        ]
        # widgets = {
        #     'course_name': forms.ChoiceField(CO)
        # }


class UpdateCourseForm(CourseBaseForm):
    class Meta(CourseBaseForm.Meta):
        exclude = [
            'group',
        ]


class CourseFilterForm(FilterSet):
    class Meta:
        model = Course
        fields = {
            'course_name': ['exact', 'icontains'],
        }
