from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.utils.translation import gettext as _


class AuthenticationRequiredMixin(LoginRequiredMixin):

    access_denied_message = _('You are not authorized! Please log in.')
    access_denied_url_name = 'login'

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            messages.error(request, self.access_denied_message)
            return redirect(self.access_denied_url_name)

        return super(
            LoginRequiredMixin,
            self
            ).dispatch(
                request,
                *args,
                **kwargs
                )


class AuthorizationRequiredMixin(UserPassesTestMixin):

    permission_denied_message = _(
        'You do not have permission to update another user.'
        )
    
    def test_func(self):
        return self.kwargs.get('pk') == self.request.user.pk

    def dispatch(self, request, *args, **kwargs):
        if not self.test_func():
            messages.error(request, self.permission_denied_message)
            return redirect(self.success_url, 302)
        return super(
            UserPassesTestMixin,
            self
            ).dispatch(
                request,
                *args,
                **kwargs
                )


class ProtectionToDeleteMixin:

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(request, self.success_message)
            return redirect(self.success_url, 200)
        except ProtectedError:
            messages.error(request, self.protection_error_message)
            return redirect(self.success_url, 302)
