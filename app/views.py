from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic                                            # импортируем класс generic
# from app.forms import OrderForm
from app.models import Order

# Creating views here


class MenuListView(generic.ListView):
    queryset = Order.objects
    template_name = 'index.html'
