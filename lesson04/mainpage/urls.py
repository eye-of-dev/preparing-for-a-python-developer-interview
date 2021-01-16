from django.urls import path

from .views import MainPage

app_name = 'mainpage'

urlpatterns = [
    path('', MainPage.as_view(), name='mainpage_index')
]