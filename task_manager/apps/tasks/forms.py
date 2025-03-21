from django import forms
from django.utils.translation import gettext as _

from .models import Task


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':_('Name')}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':_('Description')}),
            'status': forms.Select(attrs={'class': 'form-control', 'placeholder':_('Status')}),
            'executor': forms.Select(attrs={'class': 'form-control', 'placeholder':_('Executor')}),
            'labels': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder':_('Labels')})
        }

        labels = {
            'name': _('Name'),
            'description': _('Description'),
            'status': _('Status'),
            'executor': _('Executor'),
            'labels': _('Labels')
        }