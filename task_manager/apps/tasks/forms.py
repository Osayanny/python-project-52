from django import forms
from django.utils.translation import gettext as _

from .models import Task


class TaskCreateForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'executor', 'labels']


class TaskUpdateForm(TaskCreateForm):
    pass