from django.shortcuts import render, redirect
from app.models import Product, Order
from .forms import OrderForm, OrderListForm, AdminRegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.utils import timezone
from datetime import datetime

# Creating views here
now = timezone.now()


# currentDT = datetime.datetime.now()


def add_item_to_order(request):
    hour = int(datetime.strftime(datetime.now(), "%H"))
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
            order.comment = "" + order.comment
            order.save()

        return render(request, 'app/base.html', {'product_list': queryset})
    else:
        return render(request, 'app/base.html', {'product_list': queryset, 'hour': hour})


def register(request):
    if request.method == 'POST':
        form = AdminRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            if request.user.is_authenticated:
                return redirect('/order_list')
            else:
                return redirect('/login')
        else:
            return redirect('/register')
    else:
        if request.user.is_authenticated:
            return redirect('/order_list')
        else:
            form = AdminRegisterForm()
            return render(request, 'registration/register.html', {'form': form})



# show_checklist renamed to show_order_list
def show_order_list(request):
    if request.user.is_authenticated:
        queryset = Order.objects.all()
        total = 0
        total_count = 0
        for item in queryset:
            total = total + item.summary
            total_count = total_count + item.count
        return render(request, 'app/order_list.html', {'order_list': queryset, 'total': total,
                                                       'total_count': total_count})
    else:
        return redirect('/register')


def logout_view(request):
    x = request.user.is_authenticated
    if logout(request=True):
        x = False
        return redirect('/home')

