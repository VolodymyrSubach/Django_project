import re

from django import forms

from teachers.models import Teacher


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone',
            'subject_name',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
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
