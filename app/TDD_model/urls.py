from django.urls import path
from app.TDD_model.views import *

urlpatterns = [
    path('', index, name='index')
]