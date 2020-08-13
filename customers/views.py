from django.shortcuts import render, redirect
from django.http import HttpResponse
from management.models import *
from django.contrib.auth import authenticate, login
from .models import *
# from customers.model import *
# Create your views here.


def headCart(usr):
    cartDish = add_to_cart.objects.filter(user=usr)
    total = 0
    for i in cartDish:
        total += (i.dish.price) * (i.qty)
    return cartDish, total


def home(request):
    success = False
    if request.user.is_staff:
        return redirect('AdminPanel')
    
    cat = category.objects.all()
    dishes = dish.objects.filter(avail=True)
    if request.user.is_anonymous:
        d = {'cat': cat, 'dishes': dishes}
    else:
        cartdish, total = headCart(request.user)
        print(total)
        d = {'cat': cat, 'dishes': dishes, 'cartDish': cartdish, 'total': total}
    return render(request, 'index.html', d)


def reserve(request):

    success = False
    if 'reserve' in request.POST:
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        date = request.POST['date']
        time = request.POST['time']
        guests = request.POST['guests']
        data = reservation.objects.create(
            user=request.user, name=name, email=email, mob=mobile, date=date, time=time, guests=guests)
        if data:
            success = True
    if request.user.is_anonymous:
        return redirect('account')
    else:
        cartdish, total = headCart(request.user)
        d = {'cartDish': cartdish, 'total': total, 'success': success}
    return render(request, 'reservation.html', d)


def shop_cart(request):
    if request.user.is_anonymous:
        return redirect('account')
    else:
        cartDsih, total = headCart(request.user)
    d = {'cartDish': cartDsih, 'total': total}
    return render(request, 'shop_cart.html', d)


def cartDelete(request, Oid):
    add_to_cart.objects.get(id=Oid).delete()
    return redirect('shopCart')
