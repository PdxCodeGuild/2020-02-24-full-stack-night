from django.shortcuts import render
from .models import User


def home(request):
  user1 = User(first_name = 'finn', last_name = 'the human', age = 12)
  user2 = User(first_name = 'bmo', last_name = '', age = 24)
  user3 = User(first_name = 'pepbut', last_name = '', age = -999)
  user4 = User(first_name = 'marceleine', last_name = 'the vampire queen', age = 1000)

  user1.save()
  user2.save()
  user3.save()
  user4.save()

  return render(request, 'index.html')

def users(request):
  users = User.objects.all()

  context = {
    'users': users,
  }

  return render(request, 'users.html', context = context)