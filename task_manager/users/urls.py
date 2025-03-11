from django.urls import path, include
from task_manager.users import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='users_index'),
    path('create/', views.CreateFormView.as_view(), name='users_create'),
    path('<int:pk>/update', views.UpdateFormView.as_view(), name='users_update'),
    path('<int:pk>/delete', views.DeleteFormView.as_view(), name='users_delete'),
]