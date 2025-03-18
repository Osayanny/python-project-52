from django import forms
from .models import User
from django.utils.translation import gettext as _
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'password1', 'password2')

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder':f'{_('Username')}'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':f'{_('First name')}'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':f'{_('Last name')}'}),
        }

        labels = {
            'username':_('Username'),
            'first_name':_('First Name'),
            'last_name':_('Last Name'),
        }

        help_texts = {
            'username': _('Required field. No more than 150 characters. Only letters, numbers and symbols @/./+/-/_.'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({'class': 'form-control', 'placeholder':f'{_('Password')}'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control', 'placeholder':f'{_('Confirm password')}'})


class UserUpdateForm(UserRegisterForm):

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.exclude(id=self.instance.id).filter(username=username).exists():
            raise forms.ValidationError(_('This usename is already exists'))
        return username