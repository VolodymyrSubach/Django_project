import re

from django import forms

from teachers.models import Teacher

SUBJECT_NAME = (('Python', 'Python'), ('Php', 'Php'), ('Java', 'Java'), ('Javacsript', 'Javacsript'),
                ('HR generalist', 'HR generalist'),
                ('QA Manual', 'QA Manual'), ('QA Automation', 'QA Automation'), ('UI/UX Design', 'UI/UX Design'))


class CreateTeacherForm(forms.ModelForm):
    subject_name = forms.ChoiceField(
        choices=SUBJECT_NAME,
        label='Subject',
        required=False,
    )
    subject_name.choices.insert(0, (0, '--------'))

    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
            'subject_name',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
        }


class UpdateTeacherForm(forms.ModelForm):
    subject_name = forms.ChoiceField(
        choices=SUBJECT_NAME,
        label='Subject',
        required=False,
    )
    subject_name.choices.insert(0, (0, '--------'))

    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthday',
            'phone',
            'subject_name'

        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'}),
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
