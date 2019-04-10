from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from django.core.exceptions import ObjectDoesNotExist
from .forms import *
from .models import *
import datetime
from django.core.mail import send_mail
# Create your views here.


def sendmail(request):
    to_email = []
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('mail')
        message = request.POST.get('Message')
        from_email = 'ashik129603@gmail.com'
        to_email.append(email)
        if not email:
            print(len(to_email))
            return HttpResponse("<h1>email sending failed</h1>")
        else:
            print(len(to_email))
            print(to_email)
            subject = 'Welcome'
            send_mail(subject,message,from_email,to_email,fail_silently=False)
            return render(request,'sendmail.html')
    else:
        return render(request,'email send.html')


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
    else:
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


def book_list(request):
    ob = Document.objects.all()
    t_day = datetime.date.today()
    ab = datetime.date(2016,7,24)
    if ab < t_day:
        s = 'late'
    else:
        s = 'not late'
    context={
        'ob': ob,
        'dat': t_day,
        'comment': s,
        'ab': ab
    }
    return render(request,'book_list.html',context)


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/upload/')
    else:
        form = DocumentForm()
    return render(request, 'upload.html', {'form': form})