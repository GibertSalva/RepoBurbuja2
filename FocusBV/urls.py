from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('', views.homeview, name = "home"),
    path('av/',views.ACview , name = "AC"),
    path('if/',views.IFview , name = "IF"),
    path('ra/',views.IBview , name = "RA"),
    path('ib/',views.IBview , name = "IB"),
    path('ivh/',views.IVhview , name="IVh"),
    path('iv/',views.IVview , name = "IV"),
    path('ie/',views.IEview , name = "IE"),
]