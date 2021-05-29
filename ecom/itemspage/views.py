from django.shortcuts import render
from .models import Item


def index(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'itemspage/mainpage.html', context)


def productDetail(request, _id):
    context = {
        'item': Item.objects.get(id=_id)
    }

    return render(request, 'itemspage/productpage.html', context)


def login(request):
    return render(request, 'itemspage/loginpage.html')
