from django.contrib import admin

from .models import ProductCategories, Products


@admin.register(ProductCategories)
class ProductCategoriesAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)
    search_fields = ('title',)


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'price', 'quantity', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title',)
