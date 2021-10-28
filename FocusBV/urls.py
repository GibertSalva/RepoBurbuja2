from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('', views.AUXview  , name = "AUXf"),
    path('av/',views.ACview , name = "AC"),
    path('if/',views.IFview , name = "IF"),
    path('ra/',views.RAview , name = "RA"),
    path('ib/',views.IBview , name = "IB"),
    path('ivh/',views.IVhview , name="IVh"),
    path('iv/',views.IVview , name = "IV"),
    path('ie/',views.IEview , name = "IE"),
    path('hi/',views.Histview , name = "HI"),

    # Links historial
    path('hi/Formulario Auxiliar/<int:pk>/', views.auxHist, name="AUXH"),
    path('hi/Accidente Vehicular/<int:pk>/', views.avHist, name="AVH"),
    path('hi/Incendio Forestal/<int:pk>/', views.ifHist, name="IFH"),
    path('hi/Incendio de Baldio/<int:pk>/', views.ibHist, name="IBH"),
    path('hi/Rescate Animal/<int:pk>/', views.raHist, name="RAH"),
    path('hi/Incendio de Vivienda/<int:pk>/', views.IVHist, name="IVHI"),
    path('hi/Incendio Electrico/<int:pk>/', views.IEHist, name="IEH"),
    path('hi/Incendio Vehicular/<int:pk>/', views.IVhHist, name="IVhH"),

    # Links pdf
    path('if/pdf/', IFasPDF.as_view()),
    path('ib/pdf/', IBasPDF.as_view()),
    path('iv/pdf/', IVasPDF.as_view()),
    path('ra/pdf/', RAasPDF.as_view()),
    path('av/pdf/', AVasPDF.as_view()),
    path('ie/pdf/', IEasPDF.as_view()),
    path('ivh/pdf/', IVhasPDF.as_view()),
    


]