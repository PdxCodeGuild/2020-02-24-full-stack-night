# user created urls.py file for the application

# import path from django.urls
from django.urls import path

# import the functions from our views file so we can reference them here
# the . specifies the current directory, so this is importing the views file from
# the current directory
from . import views

# MUST BE urlpatterns = []
urlpatterns = [
  # create a path for your application-level routing
  # '' refers to the 'root' of the page/application
  path('', views.hello, name = 'hello'),
]



