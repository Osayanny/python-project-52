from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib import messages
from django.shortcuts import redirect
from django.db.models import ProtectedError
from .models import Label
from .forms import LabelCreateForm
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from task_manager.mixins import AuthenticationRequiredMixin


class IndexView(AuthenticationRequiredMixin, ListView):
    
    model = Label
    template_name = 'labels/index.html'


class CustomCreateView(AuthenticationRequiredMixin, CreateView):
    
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

class CustomDeleteView(AuthenticationRequiredMixin, SuccessMessageMixin, DeleteView):
    
    model = Label
    template_name = 'labels/delete.html'
    success_url = reverse_lazy('labels_index')
    success_message = _('Label was deleted successfully')

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(request, self.success_message)
            return redirect(self.success_url, 200)
        except ProtectedError:
            messages.error(request, _('Cannot delete label because it is in use'))
            return redirect(self.success_url)