from django import forms

from groups.models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'group_name': forms.DateInput(attrs={'class': 'form-control'}),
            'group_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'group_description': forms.DateInput(attrs={'class': 'form-control'})
        }


class CreateGroupForm(GroupBaseForm):
    from students.models import Student
    students = forms.ModelMultipleChoiceField(queryset=Student.objects.select_related('group'), required=False)
    # students = forms.ModelMultipleChoiceField(queryset=Student.objects.filter(group__isnull=True), required=False)

    def save(self, commit=True):
        group = super().save(commit)
        students = self.cleaned_data['students']
        for student in students:
            student.group = group
            student.save()

    class Meta(GroupBaseForm.Meta):
        pass


class UpdateGroupForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'group_start_date'
        ]
