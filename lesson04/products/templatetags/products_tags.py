from django import template

from ..models import ProductCategories

register = template.Library()


@register.inclusion_tag('products/category/sidebar_list.html')
def show_sidebar_category_nav():
    categories = ProductCategories.published.order_by('id')
    return {'categories': categories}




