from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages_app.urls')),
    path('todos/', include('todo_app.urls')),
]
