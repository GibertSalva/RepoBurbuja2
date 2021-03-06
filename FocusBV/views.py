from django.shortcuts import render, redirect, get_object_or_404
# import time,io
from django.views.decorators.csrf import csrf_protect
from .models import *
from .forms import *
from .utils import *
from django.template.loader import get_template
from django.views.generic import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.shortcuts import render
from django.db.models import Q


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
    'IVhf':IVhf,
    'IEf':IEf,
    'RAf':RAf,
    'RCf':RCf,
}
    return render(request, "home.html", context)


# --- Formulario Accidente Vehicular ---
@csrf_protect
def ACview(request):
    tipoAV = {
        ('A', 'Automovil'),
        ('B', 'Omnibus'),
        ('C', 'Camion'),
        ('D', 'Motocicleta'),
        ('E', 'Atropellado')
    }

    tiposC = {
        ('C', 'Calle'),
        ('A', 'Avenida'),
        ('R', 'Ruta'),
        ('U', 'Undefined')
    }
    AVf = AVform()
    if request.method == "POST":
        AVf = AVform(request.POST)
        if AVf.is_valid():
            av = AVf.save(request)
            request.session['dict'] = dict = {
                'Fecha':str(av.date),
                'Hora': str(av.hora),
                'Nombre': str(av.nombre),
                'Telefono': str(av.telefono),
                'Ciudad': str(av.ciudad),
                'Direccion': str(av.direccion),
                'Referencia': str(av.referencia),
                'Clase de Accidente': str(av.claseAC),
                'Corta el Transito': "Si" if str(av.corteTransito) else "No",
                'Cantidad de Vehiculos': str(av.cantVehiculos),
                'Cantidad de Personas': str(av.cantPersonas),
                'Tipo de Calle': str(av.tipoCalle),
                'Servicio de Emergencia': str(av.servEmergencia),
                'Heridos': str(av.herido),
            }
            messages.success(request, 'Form submission successful.')
            return redirect('pdf/', AVf)
        else:
            messages.error(request, 'Form submission error.')

    context = {
        'form': AVf,
    }
    return render(request, "AV.html", context)


# --- Historial Accidente Vehicular ---
@csrf_protect
def avHist(request, pk):
    av = AccidenteVehicular.objects.get(pk=pk)
    AVf = AVform(instance=av)
    if request.method == "POST":
        AVf = AVform(request.POST, instance=av)
        if AVf.is_valid():
            AVf.save(request)
            return redirect('/hi/')
    context ={
        'form': AVf,
    }
    return render(request, "AV.html", context)


# --- PDF Accidente Vehicular ---
class AVasPDF(View):
    def get(self, request, *args, **kwargs):
        dict = request.session.get('dict')
        context = {
            'dict': dict.items(),
        }
        pdf = render_to_pdf('AVpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# --- Formulario Incendio Forestal ---
@csrf_protect
def IFview(request):
    IFf = IFform()
    if request.method == "POST":
        IFf = IFform(request.POST)
        if IFf.is_valid():
            iff = IFf.save(request)
            print("se guardo")
            messages.success(request, 'Form submission successful.')
            request.session['dict'] = dict = {
                'Fecha': str(iff.date),
                'Hora': str(iff.hora),
                'Nombre': str(iff.nombre),
                'Telefono': str(iff.telefono),
                'Ciudad': str(iff.ciudad),
                'Direccion': str(iff.direccion),
                'Referencia': str(iff.referencia),
                'Sentido': str(iff.sentido),
                'Edificios': str(iff.edificios),
                'Riesgo de Propagacion': "Si" if str(iff.riesgoProp) else "No",
                'Servicio de Emergencia': str(iff.servEmergencia),
            }
            return redirect('pdf/', IFf)
        else:
            messages.error(request, 'Form submission error.')
    context = {
        'form': IFf,
    }
    return render(request, "IF.html", context)


# --- Historial Incendio Forestal ---
@csrf_protect
def ifHist(request, pk):
    ifh = IncendioForestal.objects.get(pk=pk)
    IFh = IFform(instance=ifh)
    if request.method == "POST":
        IFh = IFform(request.POST, instance=ifh)
        if IFh.is_valid():
            IFh.save(request)
            return redirect('/hi/')
    context ={
        'form': IFh,
    }
    return render(request, "IF.html", context)


# --- PDF Incendio Forestal ---
class IFasPDF(View):
    def get(self, request, *args, **kwargs):
        dict = request.session.get('dict')

        context = {
            'dict': dict.items(),
        }
        # html = template.render(context)
        pdf = render_to_pdf('IFpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# --- Formulario Auxiliar ---
@csrf_protect
def AUXview(request):
    AUX = AUXform()
    if request.method == "POST":
        AUX = AUXform(request.POST)
        if AUX.is_valid():
            auxf = AUX.save(request)
            print("se guardo")
            print(AUX)
            messages.success(request, 'Form submission successful.')
            request.session['dict'] = dict = {
                'Fecha': str(auxf.date),
                'Hora': str(auxf.hora),
                'Nombre': str(auxf.nombre),
                'Telefono': str(auxf.telefono),
                'Direccion': str(auxf.direccion),
                'Info. adicional': str(auxf.auxiliar),
            }
            return redirect('pdf/', AUX)
        else:
            messages.error(request, 'Form submission error.')
    context = {
        'form': AUX,
    }
    return render(request, "AUXf.html", context)


# --- PDF Auxiliar ---
class AUXasPDF(View):
    def get(self, request, *args, **kwargs):
        dict = request.session.get('dict')
        print(dict)
        context = {
            'dict': dict.items(),
        }
        # html = template.render(context)
        pdf = render_to_pdf('AUXpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# --- Historial Auxiliar ---
@csrf_protect
def auxHist(request, pk):
    auxh = FormularioAuxiliar.objects.get(pk=pk)
    AUXh = AUXform(instance=auxh)
    if request.method == "POST":
        AUXh = AUXform(request.POST, instance=auxh)
        if AUXh.is_valid():
            AUXh.save(request)
            return redirect('/hi/')
    context ={
        'form': AUXh,
    }
    return render(request, "AUXf.html", context)


# --- Formulario Incendio Baldio ---
@csrf_protect
def IBview(request):
    IBf = IBform()
    if request.method == "POST":
        IBf = IBform(request.POST)
        if IBf.is_valid():
            ibf = IBf.save(request)
            print("se guardo")
            messages.success(request, 'Form submission successful.')
            request.session['dict'] = dict = {
                'Fecha': str(ibf.date),
                'Hora': str(ibf.hora),
                'Nombre': str(ibf.nombre),
                'Telefono': str(ibf.telefono),
                'Ciudad': str(ibf.ciudad),
                'Direccion': str(ibf.direccion),
                'Referencia': str(ibf.referencia),
                'Entre que Calles': str(ibf.entreCalles),
                'Riesgo de Propagacion': "Si" if str(ibf.riesgoProp) else "No",
            }
            return redirect('pdf/', IBf)
        else:
            messages.error(request, 'Form submission error.')
    context = {
        'form': IBf,
    }
    return render(request, "IB.html", context)


# --- Historial Incendio Baldio ---
@csrf_protect
def ibHist(request, pk):
    ibh = IncendioBaldio.objects.get(pk=pk)
    IBh = IBform(instance=ibh)
    if request.method == "POST":
        IBh = IBform(request.POST, instance=ibh)
        if IBh.is_valid():
            IBh.save(request)
            return redirect('/hi/')
    context ={
        'form': IBh,
    }
    return render(request, "IB.html", context)


# --- PDF Incendio Baldio ---
class IBasPDF(View):
    def get(self, request, *args, **kwargs):
        dict = request.session.get('dict')

        context = {
            'dict': dict.items(),
        }
        # html = template.render(context)
        pdf = render_to_pdf('IBpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# --- Formulario Rescate Animal ---
@csrf_protect
def RAview(request):
    RAf = RAform()
    if request.method == "POST":
        RAf = RAform(request.POST)
        if RAf.is_valid():
            raf = RAf.save(request)
            print("se guardo")
            # request.session['nombre'] = RAf.cleaned_data['nombre']
            # request.session['animal'] = RAf.cleaned_data['animal']
            # request.session['telefono'] = RAf.cleaned_data['telefono']
            # request.session['direccion'] = RAf.cleaned_data['direccion']
            # request.session['referencia'] = RAf.cleaned_data['referencia']
            # request.session['condicion'] = RAf.cleaned_data['condicionAnimal']

            request.session['dict'] = dict = {
                'Fecha': str(raf.date),
                'Hora': str(raf.hora),
                'Nombre': str(raf.nombre),
                'Telefono': str(raf.telefono),
                'Ciudad': str(raf.ciudad),
                'Direccion': str(raf.direccion),
                'Referencia': str(raf.referencia),
                'Animal': str(raf.animal),
                'Condicion del Animal': str(raf.condicionAnimal),
                'Vision del Animal': "Si" if str(raf.vision) else "No",
            }

            return redirect('pdf/', RAf)
    context = {
        'form': RAf,
    }
    return render(request, "RAf.html", context)


# --- Historial Rescate Animal ---
@csrf_protect
def raHist(request, pk):
    rah = RescateAnimal.objects.get(pk=pk)
    RAh = RAform(instance=rah)
    if request.method == "POST":
        RAh = RAform(request.POST, instance=rah)
        if RAh.is_valid():
            RAh.save(request)
            return redirect('/hi/')
    context ={
        'form': RAh,
    }
    return render(request, "RAf.html", context)


# --- PDF Rescate Animal ---
class RAasPDF(View):
    def get(self, request, *args, **kwargs):
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
        return HttpResponse(pdf, content_type='application/pdf')


# --- Formulario Incencido Vivienda ---
def IVview(request):
    IVf = IVform()
    if request.method == "POST":
        IVf = IVform(request.POST)
        if IVf.is_valid():
            ivf = IVf.save(request)
            print("se guardo")
            messages.success(request, 'Form submission successful.')
            request.session['dict'] = dict = {
                'Fecha': str(ivf.date),
                'Hora': str(ivf.hora),
                'Nombre': str(ivf.nombre),
                'Telefono': str(ivf.telefono),
                'Ciudad': str(ivf.ciudad),
                'Direccion': str(ivf.direccion),
                'Referencia': str(ivf.referencia),
                'Entre que Calles': str(ivf.entreCalles),
                'Estado del Fuego': str(ivf.estadoFuego),
                'Habitantes': str(ivf.habitantes),
                'Puede ver a los propietarios?': str(ivf.localHabit),
                'Descripcion de Vivienda': str(ivf.descVivienda),
                'Pueden esperar?': "Si" if str(ivf.espera) else "No",
            }

            return redirect('pdf/', IVf)
        else:
            messages.error(request, 'Form submission error.')
    context = {
        'form': IVf,
    }
    return render(request, "IV.html", context)


# --- Historial Incencido Vivienda ---
@csrf_protect
def IVHist(request, pk):
    ivhi = IncendioVivienda.objects.get(pk=pk)
    IVhi = IVform(instance=ivhi)
    if request.method == "POST":
        IVhi = IVform(request.POST, instance=ivhi)
        if IVhi.is_valid():
            IVhi.save(request)
            return redirect('/hi/')
    context ={
        'form': IVhi,
    }
    return render(request, "IV.html", context)


# --- PDF Incendio Vivienda ---
class IVasPDF(View):
    def get(self, request, *args, **kwargs):
        dict = request.session.get('dict')

        context = {
            'dict': dict.items(),

        }
        # html = template.render(context)
        pdf = render_to_pdf('IVhpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# --- Formulario Incencido Electrico ---
@csrf_protect
def IEview(request):
    IEf = IEform()
    if request.method == "POST":
        IEf = IEform(request.POST)
        if IEf.is_valid():
            ief = IEf.save(request)
            print("se guardo")
            messages.success(request, 'Form submission successful.')
            request.session['dict'] = dict = {
                'Fecha': str(ief.date),
                'Hora': str(ief.hora),
                'Nombre': str(ief.nombre),
                'Telefono': str(ief.telefono),
                'Ciudad': str(ief.ciudad),
                'Direccion': str(ief.direccion),
                'Referencia': str(ief.referencia),
                'Donde se encuentra el desperfecto?': str(ief.desperfecto),
                'Puede ver humo o llamas?': str(ief.humoLlamas),
                'Llamaron a EPEC?': str(ief.epec),
                'Servicio de Emergencia': str(ief.servEmergencia),
            }
            return redirect('pdf/', IEf)
        else:
            messages.error(request, 'Form submission error.')
    context = {
        'form': IEf,
    }
    return render(request, "IE.html", context)


# --- Historial Incencido Electrico ---
@csrf_protect
def IEHist(request, pk):
    ieh = IncendioElectrico.objects.get(pk=pk)
    IEh = IEform(instance=ieh)
    if request.method == "POST":
        IEh = IEform(request.POST, instance=ieh)
        if IEh.is_valid():
            IEh.save(request)
            return redirect('/hi/')
    context = {
        'form': IEh,
    }
    return render(request, "IE.html", context)


# --- PDF Incencido Electrico ---
class IEasPDF(View):
    def get(self, request, *args, **kwargs):
        dict = request.session.get('dict')
        context = {
            'dict': dict.items(),
        }
        pdf = render_to_pdf('IEpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


# --- Formulario Incendio Vehiciular ---
@csrf_protect
def IVhview(request):
    IVhf = IVhform()
    if request.method == "POST":
        IVhf = IVhform(request.POST)
        if IVhf.is_valid():
            ivhf = IVhf.save(request)
            print("se guardo")
            messages.success(request, 'Form submission successful.')
            request.session['dict'] = dict = {
                'Fecha': str(ivhf.date),
                'Hora': str(ivhf.hora),
                'Nombre': str(ivhf.nombre),
                'Telefono': str(ivhf.telefono),
                'Ciudad': str(ivhf.ciudad),
                'Direccion': str(ivhf.direccion),
                'Referencia': str(ivhf.referencia),
                'Tipo de Vehiculo': str(ivhf.tipoVehiculo),
                'Puede ver humo o llamas?': str(ivhf.humoLlamas),
                'Los ocupantes se encuentran fuera del vehiculo?': "Si" if str(ivhf.vehiculoOcup) else "No",
                'Alcanza a ver si tiene tubo de GNC a la vista?': str(ivhf.gnc),
                'Riesgo de Propagacion': "Si" if str(ivhf.riesgoProp) else "No",
            }
            return redirect('pdf/', IVhf)
        else:
            messages.error(request, 'Form submission error.')
    context = {
        'form': IVhf,
    }
    return render(request, "IVh.html", context)


# --- Historial Incencido Vehicular ---
@csrf_protect
def IVhHist(request, pk):
    ivh = IncendioVehicular.objects.get(pk=pk)
    IVh = IVhform(instance=ivh)
    if request.method == "POST":
        IVh = IVhform(request.POST, instance=ivh)
        if IVh.is_valid():
            IVh.save(request)
            return redirect('/hi/')
    context = {
        'form': IVh,
    }
    return render(request, "IVh.html", context)


# --- PDF Incencido Vehicular ---
class IVhasPDF(View):
    def get(self, request, *args, **kwargs):
        dict = request.session.get('dict')
        context = {
            'dict': dict.items(),
        }
        pdf = render_to_pdf('IVhpdf.html', context)
        return HttpResponse(pdf, content_type='application/pdf')


def myfunc(e):
    print(e.date)
    return e.date


def myfunc2(e):
    return e.hora


def Histview(request):
    d = dateForm()
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

    if request.method == "GET":
        d = dateForm(request.GET)
        if d.is_valid():
            search_date = d.cleaned_data['date']
            if search_date == None:
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
            else:
                IF = IncendioForestal.objects.filter(date=search_date)
                IB = IncendioBaldio.objects.filter(date=search_date)
                IV = IncendioVivienda.objects.filter(date=search_date)
                IVh = IncendioVehicular.objects.filter(date=search_date)
                PC = PerdidaCombustible.objects.filter(date=search_date)
                EG = EscapeGas.objects.filter(date=search_date)
                IE = IncendioElectrico.objects.filter(date=search_date)
                AV = AccidenteVehicular.objects.filter(date=search_date)
                RA = RescateAnimal.objects.filter(date=search_date)
                RC = RescateCadaver.objects.filter(date=search_date)
                RP = RescatePersonaVia.objects.filter(date=search_date)
                FA = FormularioAuxiliar.objects.filter(date=search_date)

    everything = [IF, IB, IV, IVh, PC, EG, IE, AV, RA, RC, RP, FA]

    eve = []
    for queryset in everything:
        for i in queryset:
            eve.append(i)

    eve.sort(key=myfunc2, reverse=True)
    eve.sort(key=myfunc, reverse=True)

    context = {
        'arr':eve,
    }

    return render(request,"historial.html",context)