from django.shortcuts import render, redirect, get_object_or_404

from.models import *
from .forms import *

# Create your views here.
def homeview(request):
# dependiendo del id que busques en el home deberia
# de hacer o uno u otro form, pero esto, puede causar que la pagina sea recargada

    return render(request, "home.html")


