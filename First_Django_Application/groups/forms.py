from django import forms

from groups.models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_date',
            'group_description',
        ]

        widgets = {
            'group_start_date': forms.DateInput(attrs={'type': 'date'})
        }


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name',
            'group_start_date',
            'group_description',
        ]

        widgets = {
            'group_name': forms.DateInput(attrs={'class': 'form-control'}),
            'group_start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'group_description': forms.DateInput(attrs={'class': 'form-control'})
        }


class UpdateGroupForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'group_start_date'
        ]

        widgets = {
            'group_name': forms.DateInput(attrs={'class': 'form-control'}),
            'group_description': forms.DateInput(attrs={'class': 'form-control'})
        }
