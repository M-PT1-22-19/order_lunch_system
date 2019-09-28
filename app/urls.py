from . import views     # импортируем все views
from django.urls import path

urlpatterns = [
    path('', views.MenuListView, name='home'),
]
