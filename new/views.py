from django.shortcuts import render, redirect
from .models import Intake
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

def nav(request):
    return render(request, 'nav.html')
def delete(request):
    if (request.method == 'GET'):
        return render(request, 'delete.html')
    else:
        context = {}
        id = request.POST['id']

        Intake.objects.filter(id=id).delete()
        intakes = Intake.objects.all()
        context['intakes'] = intakes
        return render(request, 'delete.html',context)
def insertstudent(request):
    if (request.method == 'GET'):
        return render(request, 'insertstudent.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        Intake.objects.create(username=username, email=email, password=password)
    return render(request, 'insertstudent.html')

def selectbyname(request):
    context={}
    if (request.method == 'GET'):
        return render(request, 'selectbyname.html')
    else:
         username = request.POST['username']
         intakes = Intake.objects.all().filter(username=username)
         context['intakes'] = intakes
         return render(request, 'selectbyname.html',context)
def selectall(request):
    context = {}
    intakes = Intake.objects.all()
    context['intakes'] = intakes
    return render(request, 'selectall.html',context)
def update(request):
    return render(request, 'update.html')
def homenav(request):
    return render(request, 'homenav.html')

def signup(request):
    if (request.method == 'GET'):
        return render(request, 'signup.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        Intake.objects.create(username=username, email=email, password=password)
        return  redirect("login")
def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:

        email = request.POST['email']
        password = request.POST['password']
        intakes = Intake.objects.all().filter(email=email, password=password)

        for intake in intakes:

            if intake.email==email and intake.password==password:
                return  redirect("homenav")
            else:
                return render(request, "login.html")





