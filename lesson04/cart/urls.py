from django.urls import path

from . import views
from .views import CartView

app_name = 'cart'

urlpatterns = [
    path('', CartView.as_view(), name='cart_index'),
    path('add/<int:pk>', views.add_action, name='add'),
    path('update/<int:pk>/<int:quantity>', views.update_action, name='update'),
    path('delete/<int:pk>', views.delete_action, name='delete'),
]