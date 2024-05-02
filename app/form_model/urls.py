from django.urls import path
from app.form_model.views.form_view import *

urlpatterns = [
    path('', login, name='login'),
    path('signin/', signin, name='signin'),
    path('dashboard/', dashboard, name='dashboard')
]