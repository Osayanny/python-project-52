from django.shortcuts import render
from django.views import View
from .models import User

class UsersIndexView(View):

    template_name = 'users/index.html'

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})