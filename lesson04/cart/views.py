from django.shortcuts import get_object_or_404, redirect

from products.models import Products

from .models import Cart

from mainpage.views import TemplateClass


class CartView(TemplateClass):
    template_name = 'cart.html'
    title = 'корзина'


def add_action(request, pk):
    cart_uuid = request.COOKIES.get('cart_uuid')

    product = get_object_or_404(Products, pk=pk)
    cart = Cart.objects.filter(cart_uuid=cart_uuid, product=product).first()

    if not cart:
        cart = Cart(cart_uuid=cart_uuid, product=product)

    cart.quantity += 1
    cart.price = product.price
    cart.save()

    return redirect(request.META.get('HTTP_REFERER'))


