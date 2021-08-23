from django.shortcuts import render, redirect, get_object_or_404
import time

from django.views.decorators.csrf import csrf_protect

from .models import *
from .forms import *

# Create your views here.
def homeview(request):
# dependiendo del id que busques en el home deberia
# de hacer o uno u otro form, pero esto, puede causar que la pagina sea recargada
    AVf = AVform() # Accidente Vehicular
    IFf = IFform() # Incendio Forestal
    IBf = IBform() # Incendio Baldio
    IVf = IVform() # Invencio Vivienda
    IVhf = IVhform() # Incendio Vehicular
    IEf = IEform() # Incendio Electrico
    RAf = RAform() # Rescate Animal
    RCf = RCform() # Rescate Cadaver

    if request.method == "POST":
        AVf = AVform(request)
        if AVf.is_valid():
            AVf.save()


    context = {
    'AVf':AVf,
    'IFf':IFf,
    'IBf':IBf,
    'IVf':IVf,
    'IVhf': IVhf,
    'IEf':IEf,
    'RAf':RAf,
    'RCf':RCf,

}
    return render(request, "home.html", context)

@csrf_protect
def ACview(request):
    AVf = AVform()
    if request.method == "POST":
        AVf = AVform(request.POST)
        if AVf.is_valid():
            AVf.save(request)
            print("se guardo")

    context = {
        'form': AVf,
    }

    return render(request,"AV.html",context)

@csrf_protect
def IFview(request):
    IFf = IFform()
    if request.method == "POST":
        IFf = IFform(request.POST)
        if IFf.is_valid():
            IFf.save(request)
            print("se guardo")

    context = {
        'form': IFf,
    }

    return render(request,"IF.html",context)

@csrf_protect
def IBview(request):
    IBf = IBform()
    if request.method == "POST":
        IBf = IBform(request.POST)
        if IBf.is_valid():
            IBf.save(request)
            print("se guardo")

    context = {
        'form': IBf,
    }

    return render(request,"IB.html",context)

@csrf_protect
def IBview(request):
    RAf = RAform()
    if request.method == "POST":
        RAf = RAform(request.POST)
        if RAf.is_valid():
            RAf.save(request)
            print("se guardo")

    context = {
        'form': RAf,
    }

    return render(request,"RAf.html",context)