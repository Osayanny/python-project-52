import django_filters
from django import forms
from .models import Task
from ..labels.models import Label
from ..users.models import User
from ..statuses.models import Status
from django.utils.translation import gettext_lazy as _

class TaskFilter(django_filters.FilterSet):

    def show_self_tasks(self, queryset, arg, value):
        if value:
            return queryset.filter(author=self.request.user)
        return queryset


    own_tasks = django_filters.BooleanFilter(
        method='show_self_tasks',
        widget=forms.CheckboxInput,
        label=_('Show self tasks')
    )

    labels = django_filters.ModelChoiceFilter(
        queryset=Label.objects.all(),
        widget=forms.Select,
        label = _('Labels')
    )

    executor = django_filters.ModelChoiceFilter(
        queryset = User.objects.all(),
        widget = forms.Select,
        label = _('Executor')
    )

    status = django_filters.ModelChoiceFilter(
        queryset = Status.objects.all(),
        widget = forms.Select,
        label = _('Status')
    )

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
        