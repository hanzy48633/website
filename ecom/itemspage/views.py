from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
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
    if request.method == 'POST':
        username = request.POST.get('username', False)
        password = request.POST.get('password', False)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(user=user)
            return redirect(reverse('index_view'))
        else:
            return render(request, 'itemspage/loginpage.html')
    return render(request, 'itemspage/loginpage.html')


def _logout(request):
    logout(request)
    return redirect(reverse('index_view'))


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

    return render(request, 'itemspage/registerpage.html')
