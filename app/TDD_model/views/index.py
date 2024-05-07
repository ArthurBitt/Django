from django.shortcuts import render, HttpResponse
from app.TDD_model.models import *
# Create your views here.
def index(request):
    context = {'caracteristicas':Animal.objects.all()}
    return render(request,'TDD_model/pages/index.html', context)