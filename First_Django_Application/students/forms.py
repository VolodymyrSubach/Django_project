import re

from django import forms

from django_filters import FilterSet

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]

        widgets = {
            'first_name': forms.DateInput(attrs={'class': 'form-control'}),
            'last_name': forms.DateInput(attrs={'class': 'form-control'}),
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'email': forms.DateInput(attrs={'class': 'form-control'}),
            'phone': forms.DateInput(attrs={'class': 'form-control'}),
        }

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name').lower().title()

        return value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name').lower().title()

        return value

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        if value is not None:
            value = re.sub(r'[a-z]', '', value)
            value = re.sub(r'[!\"#$%&\'*+,./:;<=>?@\[\]^_`{|}~]', '', value)

            return value
        else:
            pass


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'first_name': forms.DateInput(attrs={'class': 'form-control'}),
            'last_name': forms.DateInput(attrs={'class': 'form-control'}),
            'phone': forms.DateInput(attrs={'class': 'form-control'}),
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name').lower().title()

        return value

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name').lower().title()

        return value

    def clean_phone(self):
        value = self.cleaned_data.get('phone')
        if value is not None:
            value = re.sub(r'[a-z]', '', value)
            value = re.sub(r'[!\"#$%&\'*+,./:;<=>?@\[\]^_`{|}~]', '', value)

            return value
        else:
            pass


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith']
        }
