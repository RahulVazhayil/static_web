from django.http import HttpResponse
from django.shortcuts import render
from . models import Place

from . models import People
from . models import About_us
from . models import Footer

# Create your views here.
def home(request):
    obj=Place.objects.all()
    obj1=People.objects.all()
    obj2=About_us.objects.all()
    obj3=Footer.objects.all()

    return   render(request,'index.html',{'result':obj,'results':obj1,'img':obj2,'ftimg':obj3})


def details(request,place_id):
    obj=Place.objects.get(id=place_id)

    return render(request,'details.html',{'result':obj})


