from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import AuthenticationRequiredMixin, ProtectionToDeleteMixin

from .forms import LabelCreateForm
from .models import Label


class IndexView(AuthenticationRequiredMixin, ListView):
    
    model = Label
    template_name = 'labels/index.html'


class CustomCreateView(AuthenticationRequiredMixin, SuccessMessageMixin, CreateView):
    
    model = Label
    form_class = LabelCreateForm
    template_name = 'labels/create.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label was created successfully')


class CustomUpdateView(AuthenticationRequiredMixin, SuccessMessageMixin, UpdateView):
    
    model = Label
    form_class = LabelCreateForm
    template_name = 'labels/update.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label was updated successfully')

class CustomDeleteView(AuthenticationRequiredMixin, SuccessMessageMixin, ProtectionToDeleteMixin, DeleteView):
    
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label was deleted successfully')
    protection_error_message = _('Cannot delete label because it is in use')