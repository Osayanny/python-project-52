from django.urls import path
from task_manager.statuses import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='statuses_index'),
    path('create/', views.CustomCreateView.as_view(), name='statuses_create'),
    path('<int:pk>/update/', views.CustomUpdateView.as_view(), name='statuses_update'),
    path('<int:pk>/delete/', views.CustomDeleteView.as_view(), name='statuses_delete')
]