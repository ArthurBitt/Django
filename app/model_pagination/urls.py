from django.urls import path
from app.model_pagination.views import *

urlpatterns = [
    path('delete/<int:item_id>', delete_item, name='delete_item'),
    path('', index, name='index'),
    path('item/<int:item_id>', item, name='item'),
    path('edit/<int:item_id>', edit_item, name='edit_item'),
    path('update/', update_item, name='update_item'),
]