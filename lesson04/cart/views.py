from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.template.loader import render_to_string

from products.models import Products

from .models import Cart, CartCommon

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


def update_action(request, pk, quantity):
    if request.is_ajax():
        product = get_object_or_404(Cart, pk=pk)
        product.quantity = quantity
        product.save()

        cart = CartCommon(request.COOKIES.get('cart_uuid'))
        result = render_to_string('includes/cart_data.html', {'cart': cart})

        return JsonResponse({'result': result})


def delete_action(request, pk):
    if request.is_ajax():
        product = get_object_or_404(Cart, pk=pk)
        product.delete()

        cart = CartCommon(request.COOKIES.get('cart_uuid'))
        result = render_to_string('includes/cart_data.html', {'cart': cart})

        return JsonResponse({'result': result})
