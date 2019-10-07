from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from users import views as user_views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.add_item_to_order, name='home'),
    path('order_list/', views.show_order_list, name='order_list'),
]