from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Todo

def list_todos(request):
  context = {'todos': Todo.objects.all()}
  return render(request, 'todo/todo_list.html', context = context)


def create_todo(request):
  if request.method == 'POST':
    data = request.POST

    Todo.objects.create(
      text = data['todoText'],
      due_date = datetime.strptime(data['dueDate'], '%Y-%m-%d').date(),
      completed = True if data.get('todoCompleted', '') == 'on' else False,
    )
    return redirect('todo_create')
  else:
    return render(request, 'todo/todo_create.html')


def update_todo(request, id):
  if request.method == 'GET':
    todo_item = get_object_or_404(Todo, pk=id)
    todo_item.due_date = todo_item.due_date.strftime('%Y-%m-%d') # must use this format or it won't display in the browser
    todo_item.completed = str(todo_item.completed).lower()
    
    return render(request, 'todo/todo_update.html', {'todo': todo_item})

  elif request.method == 'POST':
    todo_item = Todo.objects.get(pk=id)
    data = request.POST
    todo_item.text = data['todoText'],
    todo_item.due_date = datetime.strptime(data['dueDate'], '%Y-%m-%d').date(),
    # todo_item.completed = True if data.get('todoCompleted', '') == 'on' else False,
    
    todo_item.save()

    return redirect('todo_list')



def remove_todo(request):
  pass

def details_todo(request, id):
  Todo.objects.get(pk=id)
  return render(request, 'todo/todo_update.html', context = {'todo': Todo.objects.get(pk=id)})

def remove_todo_all(request):
  pass
