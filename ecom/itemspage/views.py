from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import logout
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


def _login(request):
    
    
    return render(request, 'itemspage/loginpage.html')


def _logout(request):
    logout(request)
    return redirect(reverse('index_view'))


def register(request):
    return render(request, 'itemspage/registerpage.html')
