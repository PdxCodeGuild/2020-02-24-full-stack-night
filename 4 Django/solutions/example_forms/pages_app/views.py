from django.shortcuts import render

def home(request):
  return render(request, 'pages/index.html')

def about(request):
  return render(request, 'pages/about.html')  
