from django.http import HttpResponse
from random import randint
from django.shortcuts import render

# Create your views here.
def fvInicio(request):
    return render(request, 'index.html')

def fvNumber(request):
    iNumber = randint(1,15)
    return HttpResponse(f"Su número es {iNumber}")

def fvHello(request):
    return HttpResponse('Welcome to my first test application (ES).')

def fvGreeting (request, sPersonName):
    return HttpResponse(sPersonName + ', welcome to my first test application.')