
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('mainpage.urls', namespace='mainpage')),
    path('admin/', admin.site.urls),
]
