from django.shortcuts import get_object_or_404, redirect, render
from django.views import generic
from app.models import Product, Order
from .forms import ProductForm, OrderForm

# Creating views here


# class MenuListView(generic.ListView):
#     queryset = Product.objects.all()
#     template_name = 'index.html'

## Детализация пункта меню
# class ProductDetail(generic.DetailView):
#     model = Order
#     template_name = 'product_detail.html'

# Вот эту вьюху надо запускать
def add_item_to_order(request):
    queryset = Product.objects.all()
    if request.method == "POST":    # при начальном открытии "GET"
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = form.user
            order.email = form.email
#             # order.summary = order.count * order.name_product.price
#             # order.save()
        return render(request, 'index.html', {'product_list': queryset})
    else:                             # при начальном открытии "GET"
        return render(request, 'index.html', {'product_list': queryset})


## выдрано из другого проекта
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             return_result = None                # сюда вставим результирующий словарь
#             post = form.save(commit=False)
#             if 'btn1' in request.POST:
#                 content = post.Content
#                 vowel_list = ['a', 'e', 'i', 'o', 'u', 'y']
#                 consonant_list = []
#                 count_vowel = 0
#                 count_consonant = 0
#                 for s in content:
#                     if s in vowel_list:
#                         count_vowel += 1
#                     else:
#                         count_consonant += 1
#                 post.Count_vowel = count_vowel
#                 post.Count_consonant = count_consonant
#                 # post.save()                               # закомментировал, т.к. модель меня не интересует
#                                                             # если надо сохранять объект, то коммент снять
#                 return_result = {'form': form, 'Count_vowel': post.Count_vowel, 'Count_consonant': count_consonant}
#                 # ключи этого словаря вставляются в результирующую страницу, в данном случае - index.html
#
#             elif 'btn2' in request.POST:
#                 return_result = {'form': form, 'Some_other_result': 'xxxxxxxxx'}
#
#             return render(request, 'index.html', return_result)
#     else:
#         form = PostForm()