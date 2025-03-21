
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from task_manager.mixins import AuthenticationRequiredMixin

from .forms import StatusCreateForm
from .models import Status


class IndexView(AuthenticationRequiredMixin, ListView):
    
    model = Status
    template_name = 'statuses/index.html'


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