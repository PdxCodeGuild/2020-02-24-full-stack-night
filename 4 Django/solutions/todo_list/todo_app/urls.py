from django.urls import path

from . import views

urlpatterns = [
  path('', views.list_todos, name = 'todo_list'),
  path('create', views.create_todo, name = 'todo_create'),
  path('update/<int:id>', views.update_todo, name = 'todo_update'),
  path('remove/<int:id>', views.remove_todo, name = 'todo_remove'),
  path('details/<int:id>', views.details_todo, name = 'todo_details'),    
  path('remove_all', views.remove_todo_all, name = 'todo_remove_all'),
]