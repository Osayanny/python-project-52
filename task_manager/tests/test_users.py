from django.forms.models import model_to_dict
from django.test import TestCase
from django.urls import reverse_lazy

from task_manager.apps.users.forms import UserRegisterForm
from task_manager.apps.users.models import User

# Create your tests here.

class UserTestCase(TestCase):

    fixtures = ['users_for_tests']

    def test_user_create(self):
        #get request 
        response = self.client.get('/users/create/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

        #Post request with right data
        response = self.client.post(
            '/users/create/',
            {
            'first_name': 'new_firstname',
            'last_name': 'new_lastname',
            'username': 'new_username',
            'password1': 'new_password',
            'password2': 'new_password'
            }
        )
        user = User.objects.last()
        self.assertEqual(user.username, 'new_username')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse_lazy('login'))

        #Post request with wrong data
        user_dict = model_to_dict(user, ['fist_name', 'last_name', 'username', 'password'])
        response = self.client.post('/users/create/', user_dict)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/create.html')

        form = UserRegisterForm(data=user_dict)
        self.assertFormError(form=form, field='username', errors='Пользователь с таким именем уже существует.')

    def test_user_read(self):
        response = self.client.get('/users/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/index.html')
        self.assertTrue(len(response.context['object_list'])==2)

    def test_user_update(self):
        #update for anonymous user
        response = self.client.get('/users/1/update')
        self.assertRedirects(response, reverse_lazy('login'))

        #update for another user
        user = User.objects.get(id=1)
        self.client.force_login(user)
        response = self.client.get('/users/2/update')
        self.assertRedirects(response, reverse_lazy('users_index'))
        self.assertRaisesMessage(PermissionError, 'You do not have permission to update another user.')

        #update for current user
        response = self.client.get(f'/users/{user.id}/update')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/update.html')

    
    def test_user_delete(self):
        #delete for anonymous user
        response = self.client.get('/users/1/delete')
        self.assertRedirects(response, reverse_lazy('login'))

        #delete for another user
        user = User.objects.get(id=1)
        self.client.force_login(user)
        response = self.client.get('/users/2/delete')
        self.assertRedirects(response, reverse_lazy('users_index'))
        self.assertRaisesMessage(PermissionError, 'You do not have permission to delete another user.')

        #delete for current user
        response = self.client.get(f'/users/{user.id}/delete')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('users/delete.html')
