from django.shortcuts import render


def login(request):
    return render(request,'Login.html')


def registration(request):
    return render(request,'Registeration.html')