
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django_filters.views import FilterView

from task_manager.mixins import (
    AuthenticationRequiredMixin,
    AuthorizationRequiredMixin,
)

from .filters import TaskFilter
from .forms import TaskCreateForm
from .models import Task


class IndexView(AuthenticationRequiredMixin, FilterView):
    
    model = Task
    filterset_class = TaskFilter
    template_name = 'tasks/index.html'


class CustomCreateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    CreateView
    ):
   
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task was created successfully')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form) 


class CustomUpdateView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    UpdateView
    ):
    
    model = Task
    form_class = TaskCreateForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task was updated successfully')


class CustomDeleteView(
    AuthenticationRequiredMixin,
    AuthorizationRequiredMixin,
    SuccessMessageMixin,
    DeleteView
    ):
    
    model = Task
    template_name = 'tasks/delete.html'
    success_url = reverse_lazy('tasks_index')
    success_message = _('Task was deleted successfully')
    permission_denied_message = _('A task can only be deleted by its author.')

    def test_func(self):
        task_id = self.kwargs.get('pk')
        task_author = Task.objects.get(pk=task_id).author
        return task_author == self.request.user


class CustomDetailView(
    AuthenticationRequiredMixin,
    SuccessMessageMixin,
    DetailView
    ):
    
    model = Task
    template_name = 'tasks/detail.html'
