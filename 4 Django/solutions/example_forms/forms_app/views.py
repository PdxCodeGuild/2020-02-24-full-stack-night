from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Person

def get_data(request):
  return render(request, 'forms/get_data.html')

def process(request):
  if request.method == 'POST':
    data = request.POST
    Person.objects.create(
      first_name = data['first_name'],
      last_name = data['last_name'],
      age = data['age']
    )
    return redirect('get_data')
  else:
    return HttpResponse('invalid method')
