from django.urls import path
from app.form_model.views import *

urlpatterns = [
    path('', index, name='index'),
    path('results/', results, name='results')
]