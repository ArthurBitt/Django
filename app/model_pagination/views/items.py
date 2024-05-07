# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from app.model_pagination.models import Item


def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted successfully')
    return redirect('index')

def item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(
        request=request,
        template_name='model_pagination/pages/item.html',
        context= {'item':item}
    )


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(
        request=request,
        template_name='model_pagination/pages/edit_item.html',
        context={'item':item}
    )


def update_item(request):
    if request.method == 'POST':
        # pegou no authentication_model name
        item_id = request.POST.get('item_id')
        # filtrou objeto
        item = get_object_or_404(Item, pk=item_id)

        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.quantity = request.POST.get('quantity')
        # if foto in requests.FILES:
        #     foto = request.FILES['foto']
        item.save()
        messages.success(request, 'Item updtated ')
        return redirect('index')

