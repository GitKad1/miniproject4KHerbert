from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .models import Order, Pizza
import datetime


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('../')  # Replace 'home' with the URL name of your home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('orderIndex')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})


@login_required
def order_index(request):
    orders = Order.objects.filter(user=request.user).order_by('-date')
    return render(request, 'orderIndex.html', {'orders': orders})


@login_required
def order_pizza(request):
    pizzas = Pizza.objects.all()
    return render(request, 'orderPizza.html', {'pizzas': pizzas})


@login_required
def place_order(request):
    if request.method == 'POST':
        choice = request.POST.get('pizza')
        pizza = Pizza.objects.get(topping=choice)

        # Create an Order object
        order = Order.objects.create(user=request.user, topping=pizza.topping, price=pizza.price)
        order.save()

    return redirect('orderIndex')


def user_logout(request):
    logout(request)
    return redirect('../')


