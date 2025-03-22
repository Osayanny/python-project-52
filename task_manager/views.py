from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.translation import gettext as _
from django.views import View


class IndexView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CustomLoginView(LoginView):

    success_url = reverse_lazy('users_index')
    success_message = _('You are logged in')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, self.success_message)
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class CustomLogoutView(LogoutView):

    success_url = 'users_index'
    success_message = _('You are logged out')

    def post(self, request, *args, **kwargs):
        messages.success(request, self.success_message)
        return super().post(request, *args, **kwargs)