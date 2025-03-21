from django import forms
from django.utils.translation import gettext as _

from .models import Status


class StatusCreateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('Name')})
        }

        labels = {
            'name': _('Name'),
        }

