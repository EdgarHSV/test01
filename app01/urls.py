from .views import fvHello, fvGreeting, fvNumber, fvInicio
from django.urls import path

urlpatterns = [
    path('', fvHello, name = 'vHello'),
    path('greeting/<str:sPersonName>/', fvGreeting, name = 'vGreeting'),
    path('number/', fvNumber, name= 'vNumber'),
    path('inicio/', fvInicio, name='vInicio')
]