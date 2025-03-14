from django.shortcuts import render, redirect
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import User
from .forms import UserRegisterForm, UserUpdateForm

from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from task_manager.mixins import AuthenticationRequiredMixin, AuthorizationRequiredMixin
from django.db.models import ProtectedError
from django.contrib import messages



class IndexView(ListView):

    model = User
    template_name = 'users/index.html'


class CreateFormView(SuccessMessageMixin, CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User was added successfully')



class UpdateFormView(AuthenticationRequiredMixin, AuthorizationRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User was updated successfully')
    permission_denied_message = _('You do not have permission to update another user.')



class DeleteFormView(AuthenticationRequiredMixin, AuthorizationRequiredMixin, SuccessMessageMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User was deleted successfully')
    permission_denied_message = _('You do not have permission to delete another user.')


    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(request, self.success_message)
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, _('Cannot delete user because it is in use'))
            return redirect(self.success_url)
        