from .views import fvHello, fvGreeting, fvNumber, fvInicio, fvVariable, fvConditionIf, fvLoopFor
from django.urls import path

urlpatterns = [
    # path('', fvHello, name = 'vHello'),
    # path('greeting/<str:sPersonName>/', fvGreeting, name = 'vGreeting'),
    # path('number/', fvNumber, name= 'vNumber'),
    path('inicio/', fvInicio, name='vInicio'),
    path('variable/', fvVariable, name= 'vVariable'),
    path('conditional/', fvConditionIf, name= 'vConditionIf'),
    path('loop/', fvLoopFor, name= 'vLoopFor'),
]