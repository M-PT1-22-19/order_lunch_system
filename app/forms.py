from django import forms
from .models import Product, Order, CheckList
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('slug', 'name_product', 'count', 'price',)


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('user', 'email',)


class CheckListForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ('name_product', 'user', 'summary', 'comment',)


class AdminRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2',]