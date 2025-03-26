from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views.generic.base import TemplateView
from django.contrib.messages.views import SuccessMessageMixin


class IndexView(TemplateView):

    template_name = 'index.html'


class CustomLoginView(SuccessMessageMixin, LoginView):

    success_url = reverse_lazy('users_index')
    success_message = _('You are logged in')



class CustomLogoutView(LogoutView):

    success_url = 'users_index'
    success_message = _('You are logged out')

    def post(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().post(request, *args, **kwargs)