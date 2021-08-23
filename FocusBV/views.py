from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import *

# Create your views here.
def homeview(request):
# dependiendo del id que busques en el home deberia
# de hacer o uno u otro form, pero esto, puede causar que la pagina sea recargada
    AVf = AVform()
    IFf = IFform()
    IBf = IBform()
    IVf = IVform()
    IVhf = IVhform()
    IEf = IEform()
    RAf = RAform()
    RCf = RCform()

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

def ACview(request):
    AVf = AVform()
    if request.method == "POST":
        AVf = AVform(request.POST)

        if AVf.is_valid():
            print("hola")
            AVf.save(request)
        else:
            print("NOOOO")

    context = {
        'form': AVf,
    }

    return render(request,"AV.html",context)


def IFview(request):
    IFf = IFform()
    if request.method == "POST":
        IFf = IFform(request.POST)

        if IFf.is_valid():
            print("hola")
            IFf.save(request)
        else:
            print("NOOOO")

    context = {
        'form': IFf,
    }

    return render(request,"IF.html",context)


