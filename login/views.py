from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def log(request):
    if request.method=='POST':
        us=request.POST['username']
        psw=request.POST['password']
        user=auth.authenticate(username=us,password=psw)

        if user is not None:
            auth.login(request,user)
            return redirect('/')

        else:
            messages.info(request,'invalid' )
            return render(request,'log.html')



    return render(request,'log.html')


def register(request):
    if request.method=='POST':
        u=request.POST['username']
        n1= request.POST['name1']
        n2= request.POST['name2']
        e = request.POST['email']
        p1= request.POST['password1']
        p2= request.POST['password2']
        if p1==p2:
            if User.objects.filter(username=u).exists():
                messages.info(request,"username taken")
                return redirect('register')
            elif User.objects.filter(email=e).exists():
                messages.info(request,'eamil taken')
                return redirect('register')
            else:

                user=User.objects.create_user(username=u,password=p1,first_name=n1,last_name=n2,email=e)
                user.save();
                return redirect('log')

        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')

    return   render(request,'login.html')


def detail(request):
    return render(request,'detail.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
