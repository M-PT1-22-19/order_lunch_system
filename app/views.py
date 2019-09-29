from django.views import generic
from app.models import Product, Order

# Creating views here


class MenuListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'
