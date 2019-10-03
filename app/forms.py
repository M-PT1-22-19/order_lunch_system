from django import forms
from .models import Product, Order, CheckList


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name_product', 'price',)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('user', 'email',)


class CheckListForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name_product', 'user', 'summary', 'comment',)
