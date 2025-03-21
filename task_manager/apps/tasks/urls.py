from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='tasks_index'),
    path('create/', views.CustomCreateView.as_view(), name='tasks_create'),
    path('<int:pk>/update/', views.CustomUpdateView.as_view(), name='tasks_update'),
    path('<int:pk>/delete/', views.CustomDeleteView.as_view(), name='tasks_delete'),
    path('<int:pk>/', views.CustomDetailView.as_view(), name='tasks_detail')
]