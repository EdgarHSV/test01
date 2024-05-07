from django.http import HttpResponse
from random import randint
from django.shortcuts import render
from random import randint

# Create your views here.

def fvLoopFor(request):
    ltStepsGitHubPush= ("--- From PC to WEB ---", 
                        "git status", 
                        "git add .", 
                        "git -m commit [own message]", 
                        "git push origin main", 
                        "--- From WEB to PC ---", 
                        "git pull [url] main")
    return render(request, "loop.html", {"ltSteps": ltStepsGitHubPush})

def fvConditionIf(request):
    nRandomIntNumber = randint(1,20)
    return render(request, "conditional.html", {"iNumber": nRandomIntNumber})

def fvVariable(request):
    sName= "Shaman Dad"
    return render(request, "variable.html", {"sName": sName})

def fvInicio(request):
    return render(request, 'index.html')

def fvNumber(request):
    iNumber = randint(1,15)
    return HttpResponse(f"Su número es {iNumber}")

def fvHello(request):
    return HttpResponse('Welcome to my first test application (ES).')

def fvGreeting (request, sPersonName):
    return HttpResponse(sPersonName + ', welcome to my first test application.')