from django.views import generic
from app.models import Order

# Creating views here


class MenuListView(generic.ListView):
    queryset = Order.objects
    template_name = 'index.html'
