from . import views
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView


urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.add_item_to_order, name='home'),
    path('order_list/', views.show_order_list, name='order_list'),
    path('email_sending/', TemplateView.as_view(template_name="email/email_sending.html"), name='email_sending'),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
]

