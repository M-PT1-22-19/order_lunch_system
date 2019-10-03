from . import views
from django.urls import path

urlpatterns = [
    path('', views.add_item_to_order, name='home'),
    path('register/', views.register, name='register'),
]
