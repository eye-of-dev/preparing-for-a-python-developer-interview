from django.urls import path

from .views import CategoryView

app_name = 'products'

urlpatterns = [
    path('category/<int:pk>', CategoryView.as_view(), name='category_view'),
]
