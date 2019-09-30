from django import forms
from .models import Product, Order


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'price',)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('user', 'email')