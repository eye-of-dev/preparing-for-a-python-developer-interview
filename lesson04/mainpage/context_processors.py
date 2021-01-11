from cart.models import CartCommon


def cart(request):
    return {
        'cart': CartCommon(request.COOKIES.get('cart_uuid'))
    }
