from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from.import views

urlpatterns = [
    path('', views.homeview, name = "home"),
]