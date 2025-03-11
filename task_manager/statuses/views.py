from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import Status
from .forms import StatusCreateForm

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from task_manager.mixins import AuthenticationRequiredMixin, AuthorizationRequiredMixin



class IndexView(AuthenticationRequiredMixin, ListView):
    
    model = Status
    template_name = 'statuses/index.html'
    permission_denied_url_name = 'statuses_index'


class CustomCreateView(AuthenticationRequiredMixin, CreateView):
    
    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/create.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status was created successfully')

class CustomUpdateView(AuthenticationRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Status
    form_class = StatusCreateForm
    template_name = 'statuses/update.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status was updated successfully')


class CustomDeleteView(AuthenticationRequiredMixin, SuccessMessageMixin, DeleteView):

    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_index')
    success_message = _('Status was deleted successfully')