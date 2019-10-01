from . import views
from django.urls import path

urlpatterns = [
    path('', views.add_item_to_order, name='home'),
    path('items', views.add_item_to_order, name='add_item_to_order'),
    path('order', views.show_checklist, name='show_checklist')
]
