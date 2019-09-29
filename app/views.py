from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from app.models import Product, Order

# Creating views here


class MenuListView(generic.ListView):
    queryset = Product.objects.all()
    template_name = 'index.html'

# class PostDetail(generic.DetailView):
#     model = Order
#     template_name = 'order_detail.html'
#
# def add_item_to_order(request, slug):
#     order = get_object_or_404(Order, slug=slug)
#     if request.method == "POST":
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             order = form.save(commit=False)
#             order.post = order
#             order.save()
#             return redirect('order_detail', slug=order.slug)
#     else:
#         form = OrderForm()
#     return render(request, 'order_detail.html', {'form': form})

