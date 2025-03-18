from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name= 'labels_index'),
    path('create/', views.CustomCreateView.as_view(), name='labels_create'),
    path('<int:pk>/update/', views.CustomUpdateView.as_view(), name='labels_update'),
    path('<int:pk>/delete/', views.CustomDeleteView.as_view(), name='labels_delete'),
]
