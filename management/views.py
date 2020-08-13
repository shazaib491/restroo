from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *
from customers.models import *
from customers.models import dish as dis
from customers.models import dish as dished
from customers.models import reservation as subject
from customers.views import *
from management.models import category as cat
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.contrib import messages
# Create your views here.


def about(request):
    teams = team.objects.all()
    dishes = dish.objects.filter(avail=True)
    if request.user.is_anonymous:
        d = {'team': teams}
    else:
        cartDish, total = headCart(request.user)
        d = {'team': teams, 'cartDish': cartDish, 'total': total}
    return render(request, 'about.html', d)


def menu(request):
    cat = category.objects.all()
    dishes = dish.objects.filter(avail=True)
    if request.user.is_anonymous:
        d = {"dish": dishes, "cat": cat}
    else:
        cartDish, total = headCart(request.user)
        d = {"dish": dishes, "cat": cat, 'cartDish': cartDish, 'total': total}
    return render(request, 'menu.html', d)


def menusingle(request, dishid):
    dishes = dish.objects.filter(id=dishid).first()
    if request.user.is_anonymous:
        return redirect('account')
    else:
        cartDish, total = headCart(request.user)
    if request.POST:
        if not request.user.is_authenticated:
            return redirect('account')
        data = add_to_cart.objects.filter(user=request.user, dish=dishes)
        if data:
            data.update(qty=request.POST['qty'])
        else:
            add_to_cart.objects.create(
                user=request.user, dish=dishes, qty=request.POST['qty'])

    d = {'dish': dishes, 'cartDish': cartDish, 'total': total}
    return render(request, 'menu-single.html', d)


def reservation(request):
    errorL = False
    errPass = False
    errUn = False
    if 'login' in request.POST:
        un = request.POST['un']
        pss = request.POST['pass']
        user = authenticate(username=un, password=pss)
        if user:
            login(request, user)
            if request.user.is_staff:
                return redirect('AdminPanel')
            return redirect('home')
        else:
            errorL = True

    if 'singup' in request.POST:
        email = request.POST['e']
        un = request.POST['un']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        check = User.objects.filter(username=un)
        if pwd1 != pwd2:
            errPass = True
        elif check:
            errUn = True
        else:
            User.objects.create_user(
                username=un, email=email, password=pwd1, is_staff=False)
            user = authenticate(username=un, password=pwd1)
            login(request, user)
            return redirect('home')
    d = {'errorL': errorL, 'errPass': errPass, 'errUn': errUn}
    return render(request, 'account.html', d)


def Logout(request):
    logout(request)
    return redirect('home')


def AdminPanel(request):
    res = subject.objects.all()
    orders = add_to_cart.objects.all()
    if 'deleteOrder' in request.POST:
        add_to_cart.objects.filter(id=request.POST['deleteOrder']).delete()
    if 'confirmOrder' in request.POST:
        add_to_cart.objects.filter(
            id=request.POST['confirmOrder']).update(confirm=True)
    if 'delete' in request.POST:
        subject.objects.get(id=request.POST['delete']).delete()
    if 'confirm' in request.POST:
        subject.objects.filter(id=request.POST['confirm']).update(confirm=True)
        r = subject.objects.get(id=request.POST['confirm'])
        sub = "Reservation confirm at Tomato"
        from_email = settings.EMAIL_HOST_USER
        data = {'name': r.name, 'email': r.email,
                'guests': r.guests, 'date': r.date, 'time': r.time}
        html = get_template('mail.html').render(data)
        msg = EmailMultiAlternatives(sub, '', from_email, [r.email])
        msg.attach_alternative(html, 'text/html')
        msg.send()

    d = {'res': res, 'orders': orders}
    return render(request, 'index2.html', d)


def editCat(request):
    category = cat.objects.all()
    d = {'cat': category}
    if 'deleteCat' in request.POST:
        cat.objects.filter(id=request.POST['deleteCat']).delete()
    if 'addCategory' in request.POST:
        category = cat.objects.create(name=request.POST['cat'])
    return render(request, 'editCat.html', d)


def editDish(request):
    category = cat.objects.all()
    dish = dis.objects.all()
    d = {'cat': category, 'dish': dish}
    if 'avail' in request.POST:
        dis.objects.filter(id=request.POST['avail']).update(avail=True)
    if 'unavail' in request.POST:
        dis.objects.filter(id=request.POST['unavail']).update(avail=False)
    if 'deleteDish' in request.POST:
        dis.objects.filter(id=request.POST['deleteDish']).delete()
    if 'addDish' in request.POST:
        cats = request.POST['cat']
        dash = cat.objects.get(id=request.POST['cat'])
        title = request.POST['title']
        mrp = request.POST['mrp']
        price = request.POST['price']
        dish = request.POST['dis']
        img = request.FILES['img']
        img1 = request.FILES['img2']
        img2 = request.FILES['img3']
        dished.objects.create(cat=dash, title=title, mrp=mrp,
                              price=price, dis=dish, img=img, img1=img1, img2=img2)
    return render(request, 'editDish.html', d)


def editTeams(request):
    teams = team.objects.all()
    d = {'team': teams}
    if 'teamdel' in request.POST:
        messages.error(request, 'Team member Deleted.')
        team.objects.filter(id=request.POST['teamdel']).delete()
    if 'addTeam' in request.POST:
        data = request.POST
        name = data['name']
        designation = data['dest']
        fb = data['fb']
        twt = data['twt']
        insta = data['insta']
        file = request.FILES['file']
        team.objects.create(name=name, designation=designation,
                            fb=fb, twt=twt, insta=insta, img=file)
        messages.success(request, 'Team details updated.')
    return render(request, 'editTeams.html', d)

def contactsUs(request):
    if 'contacts' in request.POST:
        data = request.POST
        name = data['name']
        email = data['email']
        subject = data['subject']
        msg = data['message']
        contacts.objects.create(name=name, email=email,
                                subject=subject, message=msg)
    return render(request, 'contacts.html')
