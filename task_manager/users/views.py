from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, UpdateView, DeleteView, ListView

from .models import User
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext as _



class CustomLoginRequiredMixin(LoginRequiredMixin):

    access_denied_message = _('You are not authorized! Please log in.')

    def dispatch(self, request, *args, **kwargs):
        current_user = self.get_object()

        if not request.user.is_authenticated:
            messages.error(request, self.access_denied_message)
            return redirect('login')
        
        if request.user.username != current_user.username:
            messages.error(request, self.permission_denied_message)
            return redirect('users_index')
            
        return super().dispatch(request, *args, **kwargs)

class UsersIndexView(ListView):

    model = User
    template_name = 'users/index.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})


class UsersCreateFormView(SuccessMessageMixin, CreateView):

    model = User
    form_class = UserRegisterForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')
    success_message = _('User was added successfully')
    


class UserUpdateFormView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    form_class = UserUpdateForm
    template_name = 'users/update.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User was updated successfully')
    permission_denied_message = _('You do not have permission to update another user.')


class UserDeleteFormView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):

    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_index')
    success_message = _('User was deleted successfully')
    permission_denied_message = _('You do not have permission to delete another user.')
