from django import forms
from .models import Label
from django.utils.translation import gettext as _


class LabelCreateForm(forms.ModelForm):

    class Meta:
        model = Label
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('Name')})
        }

        labels = {
            'name': _('Name'),
        }
