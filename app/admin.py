from django.contrib import admin
from .models import Order, Product
from django import forms


class OrderAdmin(admin.ModelAdmin):
    list_display = ('published', 'user', 'email', 'name_product', 'count', 'summary', 'comment')
    list_display_links = ('user', 'name_product', 'count', 'summary')
    search_fields = ('published', 'user')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name_product', 'price')
    list_display_links = ('name_product', 'price')
    search_fields = ('name_product', 'price')


# Register your models here.
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)
