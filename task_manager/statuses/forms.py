from django import forms
from .models import Status
from django.utils.translation import gettext as _


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':f'{_('Name')}'})
        }

        labels = {
            'name': _('Name'),
        }

