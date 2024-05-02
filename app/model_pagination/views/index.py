from django.shortcuts import render
from app.model_pagination.models import Item
from django.core.paginator import Paginator


# Create your views here.
def index(request):

    item = Item.objects.all()
    paginator = Paginator(item, 1)
    page = request.GET.get('page')
    items_per_page = paginator.get_page(page)

    return render(
        request=request,
        template_name='model_pagination/pages/index.html',
        context= {'items':items_per_page}
    )