from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create', views.create, name='create'),
    path('<int:pk>/delete', views.TaskDeleteView.as_view(), name='delete_task')
]