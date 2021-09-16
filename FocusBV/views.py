from django.shortcuts import render, redirect, get_object_or_404
# import time,io
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import *
from .utils import *
from django.template.loader import get_template
from django.views.generic import View
from django.core.paginator import Paginator


# Create your views here.
def homeview(request):
# dependiendo del id que busques en el home deberia
# de hacer o uno u otro form, pero esto, puede causar que la pagina sea recargada
    AVf = AVform() # Accidente Vehicular
    IFf = IFform() # Incendio Forestal
    IBf = IBform() # Incendio Baldio
    IVf = IVform() # Incendio Vivienda
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
    print("hola")
    AVf = AVform()
    if request.method == "POST":
        AVf = AVform(request.POST)
        print("q")
        if AVf.is_valid():
            AVf.save(request)
            print("se guardo")
        else:
            print("e")

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

####PRUEBA DE TINYMCE

@csrf_protect
def AUXview(request):
    AUX = AUXform()
    if request.method == "POST":
        AUX = AUXform(request.POST)
        if AUX.is_valid():
            AUX.save(request)
            print("se guardo")
        else:
            print("aguante del caño")

    context = {
        'form': AUX,
    }

    return render(request,"AUXf.html",context)


####PRUEBA DE TINYMCE

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
def RAview(request):
    RAf = RAform()
    if request.method == "POST":
        RAf = RAform(request.POST)
        if RAf.is_valid():
            RAf.save(request)
            print("se guardo")
            # request.session['nombre'] = RAf.cleaned_data['nombre']
            # request.session['animal'] = RAf.cleaned_data['animal']
            # request.session['telefono'] = RAf.cleaned_data['telefono']
            # request.session['direccion'] = RAf.cleaned_data['direccion']
            # request.session['referencia'] = RAf.cleaned_data['referencia']
            # request.session['condicion'] = RAf.cleaned_data['condicionAnimal']

            request.session['dict'] = dict = {
                'nombre': RAf.cleaned_data['nombre'],
                'animal': RAf.cleaned_data['animal'],
                'telefono': RAf.cleaned_data['telefono'],
                'direccion': RAf.cleaned_data['direccion'],
                'referencia': RAf.cleaned_data['referencia'],
                'condicion': RAf.cleaned_data['condicionAnimal']
            }

            return redirect('pdf/',RAf)
    
    context = {
        'form': RAf,
    }        
    
    return render(request,"RAf.html",context)

class RAasPDF(View):
    def get(self,request,*args,**kwargs):
        dict = request.session.get('dict')
        # nombre = request.session.get('nombre')
        # animal = request.session.get('animal')
        # telefono = request.session.get('telefono')
        # direccion = request.session.get('direccion')
        # referencia = request.session.get('referencia')
        # condicion = request.session.get('condicion')

        context = {
            'dict': dict.items(),
            # 'nombre': dict['nombre'],
            # 'animal': dict['animal'],
            # 'telefono': dict['telefono'],
            # 'direccion': dict['direccion'],
            # 'referencia': dict['referencia'],
            # 'condicion': dict['condicion'],
        }
        # html = template.render(context)
        pdf = render_to_pdf('RApdf.html', context)
        return HttpResponse(pdf,content_type='application/pdf')

def IVview(request):
    IVf = IVform()
    if request.method == "POST":
        IVf = IVform(request.POST)
        if IVf.is_valid():
            IVf.save(request)
            print("se guardo")

    context = {
        'form': IVf,
    }

    return render(request,"IV.html",context)

@csrf_protect
def IEview(request):
    IEf = IEform()
    if request.method == "POST":
        IEf = IEform(request.POST)
        if IEf.is_valid():
            IEf.save(request)
            print("se guardo")

    context = {
        'form': IEf,
    }

    return render(request,"IE.html",context)

@csrf_protect
def IVhview(request):
    IVhf = IVhform()
    if request.method == "POST":
        IVhf = IVhform(request.POST)
        if IVhf.is_valid():
            IVhf.save(request)
            print("se guardo")

    context = {
        'form': IVhf,
    }

    return render(request,"IVh.html",context)


def myfunc(e):
    return e.date
    
def Histview(request):
    IF = IncendioForestal.objects.all()
    IB = IncendioBaldio.objects.all()
    IV = IncendioVivienda.objects.all()
    IVh = IncendioVehicular.objects.all()
    PC = PerdidaCombustible.objects.all()
    EG = EscapeGas.objects.all()
    IE = IncendioElectrico.objects.all()
    AV = AccidenteVehicular.objects.all()
    RA = RescateAnimal.objects.all()
    RC = RescateCadaver.objects.all()
    RP = RescatePersonaVia.objects.all()
    FA = FormularioAuxiliar.objects.all()

    everything = [IF,IB,IV,IVh,PC,EG,IE,AV,RA,RC,RP,FA]

    eve = []
    for queryset in everything:
        for i in queryset:
            eve.append(i)
            print(type(i))
    eve.sort(key=myfunc, reverse=True)

    paginator = Paginator(eve, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
    }
    return render(request,"historial.html",context)