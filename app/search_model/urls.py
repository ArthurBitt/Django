from django.urls import path
from app.search_model.views.search_view import *

urlpatterns = [
    path('', search_books_view, name='search_books'),
    path('digital_library/', library_view, name='library_view')
]