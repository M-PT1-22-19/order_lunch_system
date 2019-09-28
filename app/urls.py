from . import views     # импортируем все views
from django.urls import path, include

urlpatterns = [
    path('', views.MenuListView.as_view(), name='home'),
]