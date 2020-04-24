from django.urls import path

from . import views

urlpatterns = [
  path('', views.get_data, name = 'get_data'),
  path('process', views.process, name = 'process')
]