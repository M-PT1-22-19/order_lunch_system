from . import views
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('', views.add_item_to_order, name='home'),
    path('order_list/', views.show_order_list, name='order_list'),
]