from django.urls import path
from .views import create_item, update_item, get_items

urlpatterns = [
    path('items', create_item, name='create_item'),
    path('items/<int:equipment_id>', update_item, name='update_item'),
    path('items', get_items, name='get_items'),
]
