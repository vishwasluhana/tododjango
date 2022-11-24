from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('add-todo', views.add_todo, name='add-todo'),
    path('delete/<str:pk>', views.delete_todo, name='delete-todo'),
    path('edit/<str:pk>', views.edit_todo, name='edit-todo'),
]