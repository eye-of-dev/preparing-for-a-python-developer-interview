from .models import ProductCategories
from mainpage.views import DetailClass


class CategoryView(DetailClass):
    template_name = 'category.html'
    model = ProductCategories
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super(CategoryView, self).get_context_data(**kwargs)
        return context
