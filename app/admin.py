from django.contrib import admin
from .models import Order
from django import forms


class OrderAdmin(admin.ModelAdmin):
    list_display = ('published', 'user', 'email', 'product', 'count', 'paid', 'comment')
    list_display_links = ('product', 'count', 'paid')
    search_fields = ('published', 'user')


# Register your models here.
admin.site.register(Order, OrderAdmin)