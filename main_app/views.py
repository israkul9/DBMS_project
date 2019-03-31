from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
# Create your views here.


def admin_user_login(request):
    return render(request,'first_page.html')


def log1(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            if user.username == 'SI':
                return render(request, 'samsu.html')
            else:
                return HttpResponse("<h1>Admin not found!!!!!</h1>")
        else:
            return HttpResponse("<h1>Username or password incorrect</h1>")
    return render(request, 'login.html')


def log2(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return render(request,'naser.html')
        else:
            return HttpResponse("<h1>Username or password incorrect</h1>")
    return render(request, 'login1.html')


def logou(request):
    auth.logout(request)
    return render(request,'login.html')


def logou2(request):
    auth.logout(request)
    return render(request,'login1.html')


def create(request):
    if request.method == 'POST':
        a=Createu(request.POST)
        a.save()
        messages.success(request,'user create successfully')
        return HttpResponseRedirect('/create_user/')
    else:
        a = Createu()
        return render(request,'createform.html',{'form':a})


def commety(request):
    a = User.objects.all()
    return render(request,'sirlist.html',{'a':a})