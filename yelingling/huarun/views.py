from django.shortcuts import render

# Create your views here.
from huarun.models import *


def index(request):
    lunbos = Lunbo.objects.all()
    enjoycitys =Enjoycity.objects.all()

    data ={
        "lunbos": lunbos,
        "enjoycitys":enjoycitys
    }
    return render(request,'index.html',context=data)


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')


def goodcart(request):

    return render(request,'goodcart.html')


def goodsInfo(request):

    return render(request,'goodsInfo.html')