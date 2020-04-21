from django.shortcuts import render

# create views that you referenced in urls.py

# django views always take request as an argument
def hello(request):
  return render(request, 'index.html')
