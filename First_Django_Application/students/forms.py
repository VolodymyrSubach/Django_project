from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__',
            'first_name',
            'last_name',
            'birthday',
            'email',
        ]

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value
