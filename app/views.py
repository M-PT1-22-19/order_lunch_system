from django.shortcuts import render, redirect
from app.models import Product, CheckList
from .forms import OrderForm, CheckListForm, AdminRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Creating views here


def add_item_to_order(request):
    queryset = Product.objects.all()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            product_uid = form.data['product_uid']
            product_count = int(request.POST[product_uid])
            product = Product.objects.get(slug__iexact=product_uid)
            order = form.save(commit=False)
            order.name_product = product
            order.count = product_count
            order.summary = product_count * product.price
            order.comment = "введен при заказе"
            order.save()

        return render(request, 'base.html', {'product_list': queryset})
    else:
        return render(request, 'base.html', {'product_list': queryset})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}!')
            return redirect('/admin/')
    else:
        form = AdminRegisterForm()
    return render(request, 'app/register.html', {'form': form})


# def show_checklist(request):
#     queryset = CheckList.objects.all()
#     if request.method == 'POST':
#         form = CheckListForm(request.POST)
#         if form.is_valid():
#             table = form.save(commit=False)
#             table.name_product = form.name_product
#             table.user = form.user
#             table.summury = form.summary
#             table.comment = form.comment
#         return render(request, 'order.html', {'order_list': queryset})
#     else:
#         return render(request, 'order.html', {'order_list': queryset})
