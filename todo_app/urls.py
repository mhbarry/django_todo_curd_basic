from django.urls import path, include
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:todo_id>', views.edit, name='edit'),
    path('delete/<int:todo_id>', views.delete, name='delete'),
]
