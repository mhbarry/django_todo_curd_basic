from django.contrib import admin
from django.urls import path, include
from todo_app.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('todo/', include('todo_app.urls')),
    path('mail/', include('sent_mail.urls')),
]
